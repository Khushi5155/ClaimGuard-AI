import re

def extract_claims(text: str):
    # Step 1: Clean text
    text = text.strip()

    # Step 2: Split into sentences
    sentences = re.split(r'[.!?]+', text)

    claims = []

    for sentence in sentences:
        sentence = sentence.strip()

        # Step 3: Filter rules
        if len(sentence) < 10:
            continue

        # Remove emotional / useless lines
        if any(word in sentence.lower() for word in ["shocking", "breaking", "wow"]):
            continue

        # Split on "and" for multiple claims
        sub_claims = sentence.split(" and ")
        
        for claim in sub_claims:
            claim = claim.strip()
            if len(claim) > 10:
                claims.append(claim)
                
    return claims
