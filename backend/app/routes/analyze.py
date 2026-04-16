from fastapi import APIRouter
from app.models.request_models import AnalyzeRequest
from app.services.claim_extractor import extract_claims
from app.services.knowledge_base import load_knowledge_base, get_all_texts
from app.services.similarity_engine import analyze_claims
from app.services.context_analyzer import analyze_context
from app.services.scoring_engine import calculate_truth_score
from app.services.source_checker import get_source_score

router = APIRouter()

@router.post("/analyze")
def analyze_news(request: AnalyzeRequest):
    text = request.text
    url = request.url

    # Step 1: Extract claims
    claims = extract_claims(text)

    # Step 2: Load KB
    kb = load_knowledge_base()
    kb_texts = get_all_texts(kb)

    # Step 3: Similarity
    similarity_results = analyze_claims(claims, kb_texts)

    # Step 4: Context
    context_flags = analyze_context(text)

    #  Step 5: Source credibility
    source_info = get_source_score(url)

    # Step 6: Final scoring
    final_result = calculate_truth_score(
        similarity_results,
        context_flags,
        source_info["source_score"]
    )

    if not claims:
        return {
        "message": "No valid claims found",
        "input_text": text
    }

    return {
        "input_text": text,
        "claims": claims,
        "analysis": similarity_results,
        "context_flags": context_flags,
        "source_info": source_info,
        "final_result": final_result
    }
    