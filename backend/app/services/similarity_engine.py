from sentence_transformers import SentenceTransformer, util

# Load model once (important ⚠️)
model = SentenceTransformer('all-MiniLM-L6-v2')


def find_best_match(claim: str, kb_texts: list):
    if not kb_texts:
        return None

    # Convert to embeddings
    claim_embedding = model.encode(claim, convert_to_tensor=True)
    kb_embeddings = model.encode(kb_texts, convert_to_tensor=True)

    # Compute similarity
    scores = util.cos_sim(claim_embedding, kb_embeddings)[0]

    # Get best match index
    best_idx = scores.argmax().item()

    return {
        "claim": claim,
        "best_match": kb_texts[best_idx],
        "similarity_score": float(scores[best_idx])
    }

def analyze_claims(claims: list, kb_texts: list):
    results = []

    for claim in claims:
        match = find_best_match(claim, kb_texts)

        if match:
            results.append(match)

    return results
    