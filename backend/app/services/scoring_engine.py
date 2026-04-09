def calculate_truth_score(similarity_results, context_flags, source_score=None):
    if not similarity_results:
        return {
            "truth_score": 0,
            "verdict": "No Data",
            "reasons": ["No claims found"]
        }

    # Average similarity
    avg_similarity = sum([item["similarity_score"] for item in similarity_results]) / len(similarity_results)

    score = avg_similarity * 100
    reasons = []

    # Similarity reasoning
    if avg_similarity > 0.75:
        reasons.append("High similarity with trusted data")
    elif avg_similarity > 0.5:
        reasons.append("Moderate similarity with known data")
    else:
        reasons.append("Low similarity with verified sources")

    # Context penalties
    if "sensational_language" in context_flags:
        score -= 10
        reasons.append("Contains sensational language")

    if "unrealistic_claim" in context_flags:
        score -= 15
        reasons.append("Contains unrealistic claims")

    # 🆕 Source credibility impact
    if source_score is not None:
        score = (score * 0.8) + (source_score * 0.2)

        if source_score > 80:
            reasons.append("Source is highly credible")
        elif source_score < 40:
            reasons.append("Source is low credibility")

    # Clamp
    score = max(0, min(100, score))

    # Verdict
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
    