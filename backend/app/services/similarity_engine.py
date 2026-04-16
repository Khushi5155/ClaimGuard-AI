from sentence_transformers import SentenceTransformer, util

# Load model safely
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception:
    print("Model loading failed. Running in fallback mode.")
    model = None

# Cache for KB embeddings
kb_cache = {
    "texts": [],
    "embeddings": None
}


# 🔥 Claim classification
def classify_claim(score):
    if score > 0.75:
        return "Likely Real"
    elif score > 0.5:
        return "Uncertain"
    else:
        return "Likely Fake"


def get_kb_embeddings(kb_texts):
    global kb_cache

    if kb_cache["texts"] == kb_texts and kb_cache["embeddings"] is not None:
        return kb_cache["embeddings"]

    embeddings = model.encode(kb_texts, convert_to_tensor=True)

    kb_cache["texts"] = kb_texts
    kb_cache["embeddings"] = embeddings

    return embeddings


def find_best_match(claim, kb_texts):
    if model is None:
        return {
            "claim": claim,
            "best_match": None,
            "similarity_score": 0,
            "status": "Unknown"
        }

    if not kb_texts or not claim:
        return None

    try:
        claim_embedding = model.encode(claim, convert_to_tensor=True)
        kb_embeddings = get_kb_embeddings(kb_texts)

        scores = util.cos_sim(claim_embedding, kb_embeddings)[0]

        best_idx = scores.argmax().item()
        best_score = float(scores[best_idx])

        return {
            "claim": claim,
            "best_match": kb_texts[best_idx],
            "similarity_score": round(best_score, 4),
            "status": classify_claim(best_score)
        }

    except Exception as e:
        print("Similarity error:", e)
        return None


def analyze_claims(claims, kb_texts):
    results = []

    for claim in claims:
        match = find_best_match(claim, kb_texts)
        if match:
            results.append(match)

    return results
    