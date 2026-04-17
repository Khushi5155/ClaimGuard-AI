import wikipedia


def fetch_wikipedia_evidence(claim: str):
    try:
        # Search related topics
        search_results = wikipedia.search(claim)

        if not search_results:
            return None

        # Take top result
        page_title = search_results[0]

        summary = wikipedia.summary(page_title, sentences=2)

        return {
            "title": page_title,
            "evidence": summary
        }

    except Exception as e:
        print("Wikipedia error:", e)
        return None


def get_evidence_for_claims(claims: list):
    results = []

    for claim in claims:
        evidence = fetch_wikipedia_evidence(claim)

        results.append({
            "claim": claim,
            "evidence": evidence
        })

    return results
    