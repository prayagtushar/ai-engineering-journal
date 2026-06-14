# uv add anthropic

# Two ways to stream:
#
# 1. .create(stream=True)          <- older, manual way
#    - you get one tiny piece at a time
#    - you must check each piece yourself
#    - text lives in: chunk.delta.text
#    - example:
#        for chunk in response:
#            print(chunk.delta.text)
#
# 2. .stream()                     <- newer, easier way
#    - SDK handles the boring parts
#    - gives you helpers like .text_stream to get text directly
#    - example:
#        with client.messages.stream(...) as stream:
#            for text in stream.text_stream:
#                print(text)
#
# In short: .create(stream=True) = raw chunks, you do the work
#           .stream()           = built-in helpers, less code

# ----------------------------------------------------

# | Event Type            | Meaning                             |
# | --------------------- | ----------------------------------- |
# | `content_block_start` | A new content block (text/tool)     |
# | `content_block_delta` | A partial chunk of text             |
# | `content_block_stop`  | Block finished                      |
# | `message_delta`       | Message-level update (stop_reason)  |
# | `message_start`       | Response begins, has message header |
# | `message_stop`        | Streaming complete                  |

from anthropic import AsyncAnthropic

async_client = AsyncAnthropic()


# Pattern 1 - Old and Manual method
async def stream_manual(prompt: str):
    async with await async_client.messages.create(
        model="claude-opus-4-7",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        stream=True,  # Highlight
    ) as stream:
        async for chunk in stream:
            if chunk.type == "content_block_delta":
                # chunk.delta is a TextDelta object with a .text attribute
                print(chunk.delta.text, end="", flush=True)
    print()  # newline after stream ends


# Pattern 2 - Preferred method (SDK-level streaming helper)
async def streaming_response(prompt: str) -> str:
    texts = ""
    async with async_client.messages.stream(
        model="claude-opus-4-7",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)
            texts += text

        # After stream exhausted, get the full accumulated response
        final = await stream.get_final_message()
        print("\n--- stop_reason:", final.stop_reason)
    return texts
