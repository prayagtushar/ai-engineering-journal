# Readora — RAG chat over your PDFs

> **Flagship project — full code lives in its own repo:**
> **→ https://github.com/Prayag-09/OpsverseAI**
>
> **Live:** https://readora.prayagtushar.xyz/

A retrieval-augmented chat interface for PDF documents. Upload a file and ask grounded, citation-style questions — parse → chunk → embed → retrieve → stream grounded answers, with a hallucination-resistant system prompt.

## Highlights

- **Citation-style RAG over PDFs** with a hallucination-resistant system prompt.
- Recursive chunking at 1,000 chars / 200 overlap.
- Google `gemini-embedding-001` embeddings (768-d) using **asymmetric task types** (`RETRIEVAL_DOCUMENT` vs `RETRIEVAL_QUERY`) for better query–chunk alignment.
- **Pinecone** vector store with **per-file namespacing** + MD5 chunk dedup; top-K=5, score threshold ≥ 0.5, 3,000-char context cap.
- Answers streamed from `gemini-2.5-flash`; Clerk auth; Drizzle ORM + Neon Postgres; client-side uploads via Vercel Blob (10 MB limit).
- Two modes: zero-signup demo (one PDF/browser, history in localStorage) + authenticated flow.

## Pipeline

```
PDF ─▶ parse (pdf-parse) ─▶ chunk (1000c / 200 overlap, recursive)
                              │
                              ▼
                       embed (Gemini gemini-embedding-001, 768-d)
                              │
                              ▼
                  upsert ─▶ Pinecone (one namespace per file)
                              │
  user query ─▶ embed ─▶ query (top-K=5, score ≥ 0.5) ─▶ context
                                                              │
                                                              ▼
                              streamText (Gemini 2.5 Flash) ─▶ UI
```

Every stage is its own module under `lib/rag/` — chunking, embeddings, vectorstore, ingest, retrieval. Swapping the embedding model or vector store is a one-file change.

**Try it live** at https://readora.prayagtushar.xyz/ · **full code →** https://github.com/Prayag-09/OpsverseAI
