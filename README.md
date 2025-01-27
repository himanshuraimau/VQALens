# Visual Question Answering API

This project implements a FastAPI-based service for Visual Question Answering (VQA) using the ViLT model.

## Features

- REST API endpoint for VQA
- Docker support for easy deployment
- Based on the ViLT model fine-tuned for VQA

## Requirements

- Python 3.12+
- FastAPI
- Transformers
- PyTorch
- Pillow
- Uvicorn

## Quick Start

### Running Locally

1. Install dependencies:
```bash
pip install -r req.txt
```

2. Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

### Using Docker

1. Build and run using Docker Compose:
```bash
docker compose up --build
```

The API will be available at http://localhost:8000

## API Usage

Send a POST request to `/ask` endpoint with:
- `text`: Your question about the image
- `image`: Image file upload

Example response:
```json
{
    "answer": "yes"
}
```

## Docker Deployment

### Cloud Deployment

1. Build the image:
```bash
docker build -t myapp .
```

For different CPU architecture (e.g., Mac M1 to amd64):
```bash
docker build --platform=linux/amd64 -t myapp .
```

2. Push to registry:
```bash
docker push myregistry.com/myapp
```

## References

- [Docker's Python guide](https://docs.docker.com/language/python/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ViLT Model](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa)
