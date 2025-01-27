from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
from typing import Optional

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def model_pipeline(text: str, image: Image.Image) -> str:
    try:
        # prepare inputs
        #ignore the warning
        encoding = processor(image, text, return_tensors="pt") # type: ignore

        # forward pass
        outputs = model(**encoding)
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        return model.config.id2label[idx]
    except Exception as e:
        raise Exception(f"Model processing error: {str(e)}")




