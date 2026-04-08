def analyze_context(text: str):
    flags = []

    text_lower = text.lower()

    # Rule 1: Sensational words
    if any(word in text_lower for word in ["shocking", "breaking", "unbelievable", "100%"]):
        flags.append("sensational_language")

    # Rule 2: ALL CAPS detection
    if text.isupper():
        flags.append("all_caps")

    # Rule 3: Suspicious numbers
    if "100%" in text or "guaranteed" in text_lower:
        flags.append("unrealistic_claim")

    return flags
    