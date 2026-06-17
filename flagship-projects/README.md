# Flagship Projects

Larger builds each live in **their own GitHub repo**. This folder holds a one-page showcase for each — what it is, the stack, the architecture, and a link to the full code. Small, self-contained learning builds instead live in [`../projects/`](../projects/).

| Project | What it is | Stack | Status | Repo |
|---------|-----------|-------|--------|------|
| [Indian Startup Ecosystem RAG](indian-startup-ecosystem-rag/) | Production RAG over Indian startup data; hand-rolled hybrid retrieval (vector + FTS → RRF → BGE rerank) + evals + tracing | Python · FastAPI · pgvector · Ragas · Langfuse · Next.js | 🚧 In progress | [↗](https://github.com/prayagtushar/Indian-Startup-Ecosystem-RAG) |
| [multi-llm-client](multi-llm-client/) | Unified async client over OpenAI / Anthropic / Gemini — library + CLI + REPL + API | Python · Pydantic v2 · asyncio · Tenacity · FastAPI | ✅ Working | [↗](https://github.com/prayagtushar/multi-llm-client) |
| [Readora](readora-ai/) | Citation-style RAG chat over your PDFs (live demo) | Next.js · Gemini · Pinecone · Drizzle · Neon | ✅ Live | [↗](https://github.com/Prayag-09/OpsverseAI) |
| [werewolf-agents](werewolf-agents/) | Multi-agent social-deduction game; LLM agents lie/deduce/vote, $0 on-device | Python · Pydantic · asyncio · Ollama · WebSocket | ✅ v1 | [↗](https://github.com/prayagtushar/werewolf-agents) |

## Convention

- **Big project** (multi-module, deployable, its own CI/issues) → its own repo + a pointer page here.
- **Small project** (single-purpose, learning a tool/pattern) → full code in [`../projects/`](../projects/).
