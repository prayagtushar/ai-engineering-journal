# Indian Startup Ecosystem RAG

> **Flagship project — full code lives in its own repo:**
> **→ https://github.com/prayagtushar/Indian-Startup-Ecosystem-RAG**

Production RAG over Indian startup data (YC · Inc42 · Wikipedia · DPIIT). A **hand-rolled hybrid retrieval pipeline** — vector + keyword search fused with RRF, then BGE reranking — with a measured eval suite, Langfuse tracing, and a streaming Next.js chat UI with inline citations.

**Status (Jun 2026):** in active development. Architecture, TS/Python contracts, and local Postgres + pgvector infra are in place; the ingest → retrieval → eval pipeline is being built out. Not yet deployed.

> The interview line this is built to earn: *"I built the retrieval pipeline myself — embed → hybrid search → RRF fusion → rerank — and the eval numbers show each stage helps."*

## Tech stack

Python · FastAPI (SSE streaming) · pgvector + Postgres FTS · BGE embeddings + reranker (sentence-transformers) · Ragas · Langfuse Cloud · Next.js · uv + Turborepo monorepo · Docker · Cloud Run + Vercel + Supabase

**No LangChain** — the retrieval pipeline is hand-rolled, because that pipeline is the point.

## Architecture at a glance

```
scrapers → startups.jsonl → chunk → embed → Postgres (chunks · vectors · tsvector)
user query → /chat → retrieve(hybrid + rerank) → prompt → LLM (stream) → SSE → UI
                 └───────────────── Langfuse trace ─────────────────┘
golden set → evals runner → Ragas metrics → EVALUATION.md
```

A single Postgres holds both halves of hybrid search: pgvector for semantic similarity and `tsvector` full-text for keyword/BM25. Results are fused with Reciprocal Rank Fusion, then reranked by a BGE cross-encoder.

## Why it's here

This is the centerpiece of my AI-engineering portfolio — the project that demonstrates retrieval-pipeline depth, evals, and observability rather than glue code. Deployed demo, `ARCHITECTURE.md`, and `EVALUATION.md` (with retrieval/answer metrics) will be published as milestones land.

**Read the full README, architecture spec, and code in the repo →** https://github.com/prayagtushar/Indian-Startup-Ecosystem-RAG
