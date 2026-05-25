from google import genai
from google.genai import errors

client = genai.Client()

# The google-genai SDK raises typed exceptions for different failure modes:
#
#   errors.APIError        → base class for all API errors (4xx/5xx)
#   errors.ClientError     → 4xx — bad request, auth, not found, etc.
#   errors.ServerError     → 5xx — temporary server-side issue
#   errors.APIKeyError     → API key is missing or invalid
#   errors.HttpError       → Low-level HTTP error wrapper

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Tell me a story",
    )
    print(response.text)

except errors.ClientError as e:
    # 4xx errors — bad request, auth failure, model not found, etc.
    print(f"Client error {e.code}: {e.message}")
    # e.code → HTTP status (400, 401, 404, 429, etc.)
    # → Don't retry (except 429 rate-limit, which you CAN retry with backoff)

except errors.ServerError as e:
    # 5xx errors — temporary server problem
    print(f"Server error {e.code}: {e.message}")
    # → Retry with backoff

except errors.APIKeyError as e:
    # Missing or invalid API key
    print(f"API key error: {e}")
    # → Fail fast, fix your env variable

except errors.APIError as e:
    # Catch-all for any other API error
    print(f"API error {e.code}: {e.message}")
