from typing import Dict, Any

HST_KEYWORDS = [
    "election", "campaign", "trump", "biden", "congress", "senate", 
    "stock", "market", "bond", "inflation", "casino", "vegas", 
    "bailout", "corruption", "lobbyist", "war", "strike", "riot", 
    "crypto", "bitcoin", "scandal", "surveillance", "vulnerability",
    "collapse", "meltdown"
]

def score_article(article: Dict[str, Any]) -> float:
    title = (article.get("title") or "").lower()
    desc = (article.get("description") or "").lower()
    content = (article.get("content") or "").lower()
    text = " ".join([title, desc, content])
    
    score = 0.0
    for kw in HST_KEYWORDS:
        if kw in text:
            score += 1.0
            
    return score

def is_hst_friendly(article: Dict[str, Any], threshold: float = 2.0) -> bool:
    return score_article(article) >= threshold
