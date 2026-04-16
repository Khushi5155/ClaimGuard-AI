def calculate_truth_score(similarity_results, context_flags, source_score=None):
    if not similarity_results:
        return {
            "truth_score": 0,
            "verdict": "No Data",
            "reasons": ["No claims found"]
        }

    avg_similarity = sum(
        item["similarity_score"] for item in similarity_results
    ) / len(similarity_results)

    # 🔥 Claim-level intelligence
    real_count = sum(1 for item in similarity_results if item["status"] == "Likely Real")
    fake_count = sum(1 for item in similarity_results if item["status"] == "Likely Fake")

    claim_confidence = real_count / len(similarity_results)

    # 🎯 Final score formula
    score = (avg_similarity * 70) + (claim_confidence * 30)
    score = score * 100

    reasons = []

    # Reasoning
    if avg_similarity > 0.75:
        reasons.append("Strong match with verified data")
    elif avg_similarity > 0.5:
        reasons.append("Partial match with known data")
    else:
        reasons.append("Weak similarity with trusted sources")

    if fake_count > real_count:
        reasons.append("More claims appear inconsistent")

    # Context penalties
    if "sensational_language" in context_flags:
        score -= 10
        reasons.append("Contains sensational language")

    if "unrealistic_claim" in context_flags:
        score -= 15
        reasons.append("Contains unrealistic claims")

    # Source credibility
    if source_score is not None:
        score = (score * 0.8) + (source_score * 0.2)

        if source_score > 80:
            reasons.append("Highly credible source")
        elif source_score < 40:
            reasons.append("Low credibility source")

    score = max(0, min(100, score))

    if score > 75:
        verdict = "Likely Real"
    elif score > 50:
        verdict = "Uncertain"
    else:
        verdict = "Likely Fake"

    return {
        "truth_score": round(score, 2),
        "verdict": verdict,
        "reasons": reasons
    }
    