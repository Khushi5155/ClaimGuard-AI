from fastapi import APIRouter
from app.models.request_models import AnalyzeRequest
from app.services.claim_extractor import extract_claims

router = APIRouter()

@router.post("/analyze")
def analyze_news(request: AnalyzeRequest):
    text = request.text

    # Step 1: Extract claims
    claims = extract_claims(text)

    return {
        "message": "Claims extracted successfully",
        "input_text": text,
        "claims": claims
    }
    