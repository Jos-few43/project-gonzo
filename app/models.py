from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class SourceMetadata(BaseModel):
    source_name: str
    source_url: HttpUrl
    published_at: Optional[str] = None

class GonzoArticle(BaseModel):
    disclaimer: str = "[This is a satirical reinterpretation of news in the style of Hunter S. Thompson]"
    headline: str
    subheading: str
    byline: str = "By The Vegas Correspondent"
    pull_quote: str
    body: str
    source: SourceMetadata

class RewriteRequest(BaseModel):
    article_text: str
    vegas_context: Optional[str] = None
    source_name: str
    source_url: HttpUrl
    published_at: Optional[str] = None

class RewriteResponse(GonzoArticle):
    pass
