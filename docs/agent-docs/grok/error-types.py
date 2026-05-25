# xAI (Grok) uses an OpenAI-compatible API — same SDK, so error handling is identical
# NOTE: OpenAI SDK reads OPENAI_API_KEY by default. Set it to your xAI key.
from openai import (
    OpenAI,
    OpenAIError,  # base class for everything
    APIError,  # base for all API-returned errors
    APIStatusError,  # catch-all for non-2xx status codes
    RateLimitError,  # 429 — RETRY THIS
    APITimeoutError,  # timeout — RETRY THIS
    APIConnectionError,  # network issue — RETRY THIS
    AuthenticationError,  # 401 — bad API key — don't retry
    BadRequestError,  # 400 — bad request params — don't retry
    PermissionDeniedError,  # 403 — insufficient permissions
    NotFoundError,  # 404 — model not found — don't retry
    ConflictError,  # 409 — resource conflict
    UnprocessableEntityError,  # 422 — validation error
    InternalServerError,  # 500+ — server error — RETRY THIS
)

client = OpenAI(base_url="https://api.x.ai/v1")  # set OPENAI_API_KEY to your xAI key in .env
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
except PermissionDeniedError:
    # → fail fast, no retry
    raise
except InternalServerError:
    # → retry with backoff
    pass
except APIStatusError as e:
    # catch-all for any other non-2xx response
    print(f"API error {e.status_code}: {e.message}")
