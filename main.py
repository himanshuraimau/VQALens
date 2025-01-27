from model import model_pipeline
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import Union
from PIL import Image
import io

app = FastAPI(
    title="VQALens",
    description="Visual Question Answering API powered by ViLT model",
    version="1.0.0"
)

@app.post("/ask", 
    summary="Ask a question about an image",
    response_description="The answer to the question about the image")
async def ask(text: str, image: UploadFile):
    if not image.content_type or not image.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")
        
    try:
        content = await image.read()
        img = Image.open(io.BytesIO(content))
        
        result = model_pipeline(text, img)
        return {"answer": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Visual Question Answering API. Use /ask endpoint for questions."}
