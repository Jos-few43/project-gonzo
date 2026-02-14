# Fear and Prompting in the Newsroom Machine 🖋️🌵

A weaponized gonzo news engine that drinks raw headlines and vomits them back out as satirical re-interpretations in the style of Hunter S. Thompson.

## High-Level Pipeline
1. **Ingest**: Pull raw news from APIs (NewsAPI, GNews).
2. **Extract**: Compact core facts (map-reduce compression).
3. **Enrich**: Add Vegas context and angle briefs.
4. **Generate**: HST style-transfer essays.

## Architecture
- **Backend**: FastAPI (Python)
- **Orchestration**: LangChain / Pydantic
- **News Intake**: NewsAPI.org / GNews.io
- **Bot Layer**: Scheduled worker for auto-gonzo generation

## Project Structure
```text
las-vegas-times/
app/
├── main.py        # FastAPI entrypoint
├── config.py      # Settings & API keys
├── models.py      # Pydantic schemas
├── chains.py      # Fact extraction & HST generation
├── news_client.py # News API wrappers
├── selector.py    # HST-friendly scoring logic
├── storage.py     # Feed management
└── worker.py      # Auto-bot logic
```
