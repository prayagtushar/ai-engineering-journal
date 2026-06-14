# Two ways to get responses:
#
# 1. client.models.generate_content_stream()   ← streaming (chunks arrive as they're generated)
#    - you get one chunk at a time as the model generates
#    - text lives in: chunk.text
#    - each chunk is a `GenerateContentResponse` with partial content
#    - example:
#        for chunk in stream:
#            print(chunk.text, end="", flush=True)
#
# 2. client.models.generate_content()           ← non-streaming (wait for full response)
#    - returns the complete response only when generation finishes
#    - response.text has the full content
#    - example:
#        response = client.models.generate_content(...)
#        print(response.text)
#
# In short: generate_content_stream() = see text as it's being written
#           generate_content()        = wait for the whole thing

# ----------------------------------------------------

# | Response Type       | Meaning                           |
# | ------------------- | --------------------------------- |
# | GenerateContentResp | Full response (candidates, meta)  |
# | (streamed chunks)   | Partial text, updated in each     |
# | finish_reason       | STOP | MAX_TOKENS | SAFETY | ... |

from google import genai

client = genai.Client()


# Pattern 1 - Streaming sync (text arrives chunk by chunk)
def stream_response(prompt: str):
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    for chunk in stream:
        # Each chunk is a GenerateContentResponse; text may be empty
        if chunk.text:
            print(chunk.text, end="", flush=True)
    print()  # newline after stream ends


# Pattern 2 - Streaming async (non-blocking)
import asyncio


async def stream_async(prompt: str):
    stream = await client.aio.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    async for chunk in stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
    print()


# Pattern 3 - Non-streaming (wait for complete response)
def complete_response(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=genai.types.GenerateContentConfig(max_output_tokens=500),
    )
    print(f"\n--- finish_reason: {response.candidates[0].finish_reason}")
    return response.text
