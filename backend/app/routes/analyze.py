from fastapi import APIRouter
from app.models.request_models import AnalyzeRequest
from app.services.claim_extractor import extract_claims
from app.services.knowledge_base import load_knowledge_base

router = APIRouter()

@router.post("/analyze")
def analyze_news(request: AnalyzeRequest):
    text = request.text

    # Step 1: Extract claims
    claims = extract_claims(text)

    # Step 2: Load knowledge base
    knowledge_base = load_knowledge_base()

    return {
        "message": "Claims + Knowledge Base loaded",
        "input_text": text,
        "claims": claims,
        "knowledge_base_size": len(knowledge_base)
    }
    