from fastapi import APIRouter
from app.models.request_models import AnalyzeRequest

router = APIRouter()

@router.post("/analyze")
def analyze_news(request: AnalyzeRequest):
    text = request.text

    # For now: basic response
    return {
        "message": "API working",
        "input_text": text
    }
    