from fastapi.middleware.cors import CORSMiddleware
from model import model_pipeline
from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Response
from fastapi.responses import JSONResponse
from typing import Union
from PIL import Image
import io

app = FastAPI(
    title="VQALens",
    description="Visual Question Answering API powered by ViLT model",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.post("/ask", response_class=JSONResponse)
async def ask(
    response: Response,
    text: str = Form(...),
    image: UploadFile = File(...),
):
    response.headers["Access-Control-Allow-Origin"] = "*"
    # Validate input
    if not text.strip():
        raise HTTPException(status_code=400, detail="Question text cannot be empty")
    
    if not image.filename or not image.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid image file")
    
    try:
        # Read the image content
        content = await image.read()
        img = Image.open(io.BytesIO(content))
        
        # Process the image and question
        result = model_pipeline(text, img)
        
        return {
            "status": "success",
            "answer": result,
            "question": text
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"status": "error", "message": str(e)}
        )

# Add OPTIONS endpoint for CORS preflight
@app.options("/ask")
async def ask_options():
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        }
    )

@app.get("/")
async def root():
    return {"message": "Welcome to the Visual Question Answering API. Use /ask endpoint for questions."}
