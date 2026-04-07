from fastapi import APIRouter
from app.models.request_models import AnalyzeRequest
from app.services.claim_extractor import extract_claims
from app.services.knowledge_base import load_knowledge_base, get_all_texts
from app.services.similarity_engine import analyze_claims

router = APIRouter()

@router.post("/analyze")
def analyze_news(request: AnalyzeRequest):
    text = request.text

    # Step 1: Extract claims
    claims = extract_claims(text)

    # Step 2: Load knowledge base
    kb = load_knowledge_base()
    kb_texts = get_all_texts(kb)

    # Step 3: Compare claims
    similarity_results = analyze_claims(claims, kb_texts)

    return {
        "message": "Phase 4 working: Similarity Engine",
        "input_text": text,
        "claims": claims,
        "analysis": similarity_results
    }
    