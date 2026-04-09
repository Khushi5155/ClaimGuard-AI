from urllib.parse import urlparse

# Static credibility database (can expand later)
SOURCE_CREDIBILITY = {
    "bbc.com": 90,
    "ndtv.com": 85,
    "thehindu.com": 88,
    "indiatoday.in": 80,
    "randomblog.xyz": 20,
    "unknown": 50
}


def extract_domain(url: str):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "")
        return domain
    except:
        return None


def get_source_score(url: str):
    if not url:
        return {
            "source": None,
            "source_score": None
        }

    domain = extract_domain(url)

    score = SOURCE_CREDIBILITY.get(domain, SOURCE_CREDIBILITY["unknown"])

    return {
        "source": domain,
        "source_score": score
    }
    