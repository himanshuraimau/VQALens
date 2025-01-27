# VQALens

A powerful Visual Question Answering API service powered by ViLT model.

## Features

- REST API endpoint for VQA
- Docker support for easy deployment
- Based on the ViLT model fine-tuned for VQA
- Web interface for easy testing

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
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at http://localhost:8000

### Using Docker

1. Build and run using Docker Compose:
```bash
docker compose up --build
```

The API will be available at http://localhost:8000

## API Usage

### Web Interface
Visit http://localhost:8 to use the web interface.

### API Endpoints
Send a POST request to `/ask` endpoint with:
- `text`: Your question about the image
- `image`: Image file upload

Example using curl:
```bash
curl -X POST http://localhost:8000/ask \
  -F "image=@path/to/image.jpg" \
  -F "text=What color is the sky?"
```

Example response:
```json
{
    "answer": "blue"
}
```

## Docker Deployment

1. Build the image:
```bash
docker build -t vqalens .
```

For different CPU architecture (e.g., Mac M1 to amd64):
```bash
docker build --platform=linux/amd64 -t vqalens .
```

2. Run the container:
```bash
docker run -p 8000:8000 vqalens
```

## Environment Variables

- `PORT`: Server port (default: 8000)

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ViLT Model](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa)
- [Docker Documentation](https://docs.docker.com/)
