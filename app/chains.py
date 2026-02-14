from typing import Dict, Any, List, Optional
import os
import requests
import openai
from .config import settings

# System Prompts
FACT_SYSTEM_PROMPT = """
You are an analyst extracting core factual bullet points from a news article. 
Return only a compact bullet list of objective facts: who, what, when, where, money amounts, outcomes, and key quotes in your own words. 
Do not copy sentences from the article.
"""

HST_SYSTEM_PROMPT = """
You are "The Vegas Correspondent", a satirical commentator clearly inspired by Hunter S. Thompson. 
You write first-person, gonzo-style reinterpretations of news stories as darkly humorous, metaphor-rich essays. 
You MUST:
- Keep the factual content consistent with the provided fact list.
- Use a visceral, first-person narrative voice (Gonzo).
- Add analysis about power, money, corruption, and American absurdity, often via a Las Vegas metaphor.
- Produce 900-1200 words.
- Include exactly these sections and format: [Disclaimer] [HST-STYLE HEADLINE] [Subheading] [Opening] [Article body] [Editorial conclusion]

---
**Source Attribution:** Based on reporting from [SOURCE_NAME]
**Original Story:** [LINK]
**Published:** [DATE]

You MUST:
- Avoid copying any wording from the original article.
- Not follow the original article's paragraph order.
- Make it obvious this is satirical commentary, not straight news.
"""

def get_rag_context(query: str) -> str:
    """
    Placeholder for RAG logic to fetch Hunter S. Thompson style snippets.
    To be implemented after style research.
    """
    return "Style Context: Heavy use of drug metaphors, visceral descriptions of 'The Fear', and cynical political analysis."

def _call_openai(system: str, user: str, model: str = "gpt-4o") -> str:
    client = openai.OpenAI(api_key=settings.openai_api_key)
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.9,
    )
    return resp.choices[0].message.content

def _call_gemini(system: str, user: str) -> str:
    # Placeholder for Gemini API call
    # Requires google-generativeai package
    return "Gemini Response Placeholder"

def _call_ollama(system: str, user: str) -> str:
    url = f"{settings.ollama_base_url}/api/generate"
    payload = {
        "model": settings.ollama_model,
        "prompt": f"System: {system}\n\nUser: {user}",
        "stream": False,
        "options": {"temperature": 0.9}
    }
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    return resp.json()["response"]

def dispatch_llm(system: str, user: str, provider: Optional[str] = None) -> str:
    provider = provider or settings.primary_provider
    try:
        if provider == "openai":
            return _call_openai(system, user)
        elif provider == "gemini":
            return _call_gemini(system, user)
        elif provider == "ollama":
            return _call_ollama(system, user)
    except Exception as e:
        print(f"Provider {provider} failed: {e}")
        # Simple fallback logic
        if provider != "ollama":
            return dispatch_llm(system, user, provider="ollama")
    return "All LLM providers failed."

def extract_facts(article_text: str) -> str:
    user_prompt = f"Article text: {article_text}\n\nReturn the bullet list of facts."
    return dispatch_llm(FACT_SYSTEM_PROMPT, user_prompt)

def generate_hst_article(
    facts: str, 
    vegas_context: Optional[str], 
    source_name: str, 
    source_url: str, 
    published_at: Optional[str]
) -> str:
    style_examples = get_rag_context(facts)
    context_snippet = vegas_context or "Use Las Vegas as a metaphor for American excess."
    
    user_prompt = f"""
    STYLE REFERENCE: {style_examples}
    
    FACT LIST: {facts}
    
    VEGAS CONTEXT: {context_snippet}
    
    SOURCE METADATA:
    Name: {source_name}
    URL: {source_url}
    Published: {published_at or "Unknown"}
    
    Write the full article now using the required structure and voice.
    """
    return dispatch_llm(HST_SYSTEM_PROMPT, user_prompt)
