from sentence_transformers import SentenceTransformer, util

try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    print("Model loading failed. Check internet or download model manually.")
    model = None

# 🔥 Cache for knowledge base embeddings
kb_cache = {
    "texts": [],
    "embeddings": None
}


def get_kb_embeddings(kb_texts: list):
    """
    Returns cached embeddings if KB hasn't changed,
    otherwise computes and caches them.
    """
    global kb_cache

    # If same KB, reuse embeddings
    if kb_cache["texts"] == kb_texts and kb_cache["embeddings"] is not None:
        return kb_cache["embeddings"]

    # Compute embeddings
    embeddings = model.encode(kb_texts, convert_to_tensor=True)

    # Update cache
    kb_cache["texts"] = kb_texts
    kb_cache["embeddings"] = embeddings

    return embeddings


def find_best_match(claim: str, kb_texts: list):
    """
    Finds the most similar text from knowledge base
    for a given claim.
    """

    if model is None:
        return {
            "claim": claim,
            "best_match": None,
            "similarity_score": 0
    }

    if not kb_texts or not claim:
        return None

    try:
        # Encode claim
        claim_embedding = model.encode(claim, convert_to_tensor=True)

        # Get KB embeddings (cached)
        kb_embeddings = get_kb_embeddings(kb_texts)

        # Compute cosine similarity
        scores = util.cos_sim(claim_embedding, kb_embeddings)[0]

        # Get best match
        best_idx = scores.argmax().item()
        best_score = float(scores[best_idx])

        return {
            "claim": claim,
            "best_match": kb_texts[best_idx],
            "similarity_score": round(best_score, 4)
        }

    except Exception as e:
        print("Error in similarity calculation:", e)
        return None


def analyze_claims(claims: list, kb_texts: list):
    """
    Processes multiple claims and returns similarity results.
    """
    results = []

    if not claims or not kb_texts:
        return results

    for claim in claims:
        match = find_best_match(claim, kb_texts)

        if match:
            results.append(match)

    return results
    