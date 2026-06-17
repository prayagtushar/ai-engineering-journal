# 🐺 werewolf-agents

> **Flagship project — full code lives in its own repo:**
> **→ https://github.com/prayagtushar/werewolf-agents**

**A multi-agent social-deduction game where LLM agents lie, deduce, and vote each other out — running 100% on-device for $0.**

**Status:** ✅ v1 runs end-to-end. Built task-by-task (TDD); a full game (7–9 players) plays locally on Ollama, streamed live to a dashboard or the terminal. 65 tests green · ruff + mypy strict clean.

## Highlights

- Multi-agent social-deduction game: 7 or 9 LLM agents across 4 roles (werewolf, seer, doctor, villager).
- **Dual-channel output** per turn — `private_reasoning` vs `public_action` (JSON-schema-constrained Pydantic) — so model intent vs behavior is fully observable.
- **The werewolf pack coordinates**: every wolf acts at night, sees its packmates' picks in private memory, and the kill is the pack's majority vote.
- **Deterministic game engine fully separated from the LLM**: malformed output *or a model timeout/transport error* is re-prompted, then falls back to a random legal move — a bad or slow model never crashes a game.
- AsyncIO orchestrator streaming `GameEvent`s over **WebSocket** to a live dashboard; per-agent memory across turns.
- **Eval harness**: win-rate, voting accuracy, deception proxy, doctor-save rate, first-blood, and fallback / valid-output rate over batch runs.
- Runs at **$0 on local Ollama** (`qwen2.5:3b`); 3 balanced presets selectable via env var.

## Why it exists

A portfolio piece demonstrating what actually matters for agentic systems: **multi-agent orchestration** (a deterministic engine drives N LLM agents through a night/day loop), **structured LLM output** (Pydantic-validated JSON every turn), **prompt engineering for role-play & deception**, **local inference / cost engineering** ($0/game), **evals & observability**, and a **real-time streaming UI** (FastAPI + WebSocket).

**Core principle:** the Game Engine is the single source of truth and contains **zero LLM code**. Agents only *propose* actions; the engine validates and applies them — so a dumb model can never crash or cheat the game.

**Read the full README, eval results, and code in the repo →** https://github.com/prayagtushar/werewolf-agents
