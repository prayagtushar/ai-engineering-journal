# multi-llm-client

> **Flagship project — full code lives in its own repo:**
> **→ https://github.com/prayagtushar/multi-llm-client**

Unified **async Python client** for OpenAI, Anthropic, and Gemini — a single interface over three providers with consistent data models, streaming, retries, and a pluggable provider architecture.

## Highlights

- One async interface over **OpenAI, Anthropic, and Gemini** — normalizes messages, streaming, token usage, and errors across all three.
- **Four surfaces from one core**: Python library, CLI (`llm`), interactive REPL (`multi-llm`), and a FastAPI service.
- **Tenacity** exponential-backoff retries (5 attempts) with provider-specific error mapping and a custom exception hierarchy.
- Type-safe throughout: **Pydantic v2** models + `pydantic-settings` config + **mypy-strict**.
- `compare()` races a prompt across all configured providers **concurrently** (`asyncio.gather`) with per-call latency + request IDs.
- **40 tests** across client / provider adapters / API / REPL; Python 3.11+.

## Architecture

```
                    ┌──────────────────────┐
                    │   LLMProvider (ABC)   │
                    │  + complete()         │
                    │  + stream()           │
                    └──────────┬───────────┘
                               │ inherits
               ┌───────────────┼───────────────┐
               ▼               ▼               ▼
        OpenAIProvider  AnthropicProvider  GeminiProvider
               │               │               │
               └───────────────┴───────────────┘
                               │ all return
                               ▼
                       LLMResponse (Pydantic)
                    content, usage, latency_ms,
                    model, finish_reason, provider
```

A provider registry/factory resolves the active providers from whichever API keys are set, so adding a fourth provider is a single new adapter implementing the `LLMProvider` ABC.

**Read the full README, usage examples, and code in the repo →** https://github.com/prayagtushar/multi-llm-client
