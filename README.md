# AI Engineering Journal

Documenting everything I learn on the way to becoming an AI Product Engineer — the projects I ship, the tools I pick up, and the patterns behind them. Public on purpose: this is the build-in-public trail.

## How this repo is organized

| Folder | What's inside |
|--------|---------------|
| [flagship-projects/](flagship-projects/) | Showcase pages for the **big builds** — each lives in its own repo; here you get a one-page summary + link |
| [projects/](projects/) | **Small builds** with full code in-repo — single-purpose, learning a specific tool or pattern |
| [notes/](notes/) | Concept & tool notes: [python](notes/python/), [dsa](notes/dsa/), [llm-providers](notes/llm-providers/), [web-scraping snippets](notes/web-scraping-snippets/), [retry](notes/retry-mechanism/) |

**Big vs small:** a build lives in its own repo (and gets a pointer page in `flagship-projects/`) once it's multi-module, deployable, or interview-worthy. Otherwise the full code stays in `projects/`.

## Flagship projects

| Project | What it is | Status | Repo |
|---------|-----------|--------|------|
| [Indian Startup Ecosystem RAG](flagship-projects/indian-startup-ecosystem-rag/) | Production RAG with hand-rolled hybrid retrieval + evals + tracing | 🚧 In progress | [↗](https://github.com/prayagtushar/Indian-Startup-Ecosystem-RAG) |
| [multi-llm-client](flagship-projects/multi-llm-client/) | Unified async client over OpenAI / Anthropic / Gemini | ✅ Working | [↗](https://github.com/prayagtushar/multi-llm-client) |
| [Readora](flagship-projects/readora-ai/) | Citation-style RAG chat over PDFs (live demo) | ✅ Live | [↗](https://github.com/Prayag-09/OpsverseAI) |
| [werewolf-agents](flagship-projects/werewolf-agents/) | Multi-agent social-deduction game, $0 on-device | ✅ v1 | [↗](https://github.com/prayagtushar/werewolf-agents) |

## Small projects

| Project | Focus |
|---------|-------|
| [issue-tracker-fastapi](projects/issue-tracker-fastapi/) | FastAPI REST API — routing, Pydantic, layered storage |
| [web-scraping](projects/web-scraping/) | End-to-end scraping pipeline → dataset |
