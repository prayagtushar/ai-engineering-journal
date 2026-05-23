from openai import (
    OpenAI,
    OpenAIError,  # base class for everything
    APIError,  # base for all API-returned errors
    RateLimitError,  # 429 — RETRY THIS
    APITimeoutError,  # timeout — RETRY THIS
    APIConnectionError,  # network issue — RETRY THIS
    AuthenticationError,  # 401 — bad API key — don't retry
    BadRequestError,  # 400 — bad request params — don't retry
    NotFoundError,  # 404 — model not found — don't retry
)

client = OpenAI()
# Status codes on the error:
try:
    response = client.chat.completions.create(...)
except RateLimitError as e:
    print(e.status_code)  # 429
    print(e.message)  # human-readable message
    print(e.response)  # raw httpx.Response
    print(e.body)  # parsed JSON body
    # → retry with backoff
except APITimeoutError:
    # → retry
    pass
except AuthenticationError:
    # → fail fast, no retry
    raise
