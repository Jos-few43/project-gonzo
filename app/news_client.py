import requests
from typing import List, Dict, Any
from .config import settings

BASE_URL = "https://newsapi.org/v2"

def fetch_top_headlines(categories: List[str] = None, page_size: int = 20) -> List[Dict[str, Any]]:
    if categories is None:
        categories = settings.news_categories
    
    headers = {"X-Api-Key": settings.newsapi_key}
    articles: List[Dict[str, Any]] = []
    
    for cat in categories:
        params = {
            "country": settings.news_country,
            "category": cat,
            "pageSize": page_size,
        }
        try:
            resp = requests.get(f"{BASE_URL}/top-headlines", params=params, headers=headers, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            articles.extend(data.get("articles", []))
        except Exception as e:
            print(f"Error fetching {cat}: {e}")
            
    return articles
