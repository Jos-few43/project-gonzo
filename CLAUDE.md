# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A gonzo news engine that ingests raw headlines and transforms them into satirical re-interpretations in Hunter S. Thompson's style. Uses local LLMs for style-transfer with a RAG corpus of Thompson's work.

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| LLM | LangChain, local models (Mistral NeMo 12B via KoboldCPP/Ollama) |
| Schemas | Pydantic |
| News | NewsAPI.org, GNews.io |

## Project Structure

```
project-gonzo/
├── app/
│   ├── main.py           # FastAPI entrypoint
│   ├── chains.py          # Fact extraction & HST style-transfer LLM chains
│   ├── config.py          # Settings
│   ├── models.py          # Pydantic schemas
│   ├── news_client.py     # News API wrappers
│   └── selector.py        # Scoring logic
├── corpus/                # HST excerpts for style RAG
├── requirements.txt
└── RESEARCH_GONZO.md      # RTX 3060 GPU optimization research
```

## Key Commands

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload    # Start dev server
```

## Cross-Repo Relationships

- **shared-memory** / **shared-skills** — Ecosystem integration
- **litellm-stack** — Local model routing

## Things to Avoid

- Don't hardcode `/home/yish` — use `$HOME` or `/var/home/yish`
- Don't use cloud APIs when local LLMs are available — designed for local inference
