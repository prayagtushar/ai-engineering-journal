# xAI (Grok) uses an OpenAI-compatible API — same SDK, different base_url
# NOTE: OpenAI SDK reads OPENAI_API_KEY by default. Set it to your xAI key.
#
# Two ways to stream:
#
# 1. .create(stream=True)          ← older, manual way
#    - you get one tiny piece at a time
#    - you must check each piece yourself
#    - text lives in: chunk.choices[0].delta.content
#    - example:
#        for chunk in response:
#            print(chunk.choices[0].delta.content)
#
# 2. .stream()                     ← newer, easier way
#    - SDK handles the boring parts
#    - gives you helper like .text_stream() to get text directly
#    - example:
#        with agent.chat.completions.stream(...) as stream:
#            for text in stream.text_stream():
#                print(text)
#
# In short: .create(stream=True) = raw chunks, you do the work
#           .stream()           = built-in helpers, less code

# ----------------------------------------------------

# | Event Type      | Meaning                |
# | --------------- | ---------------------- |
# | `content.delta` | Partial generated text |
# | `content.done`  | Generation finished    |
# | `chunk`         | Raw streamed packet    |
# | `message`       | Full completed message |
# | `refusal.delta` | Partial refusal text   |

from openai import AsyncOpenAI

async_client = AsyncOpenAI(base_url="https://api.x.ai/v1")


# Pattern 1 - Old and Manual method
async def stream_manual(prompt: str):
    stream = await async_client.chat.completions.create(
        model="grok-4.3",
        messages=[{"role": "user", "content": prompt}],
        stream=True,  # Highlight
    )

    async for chunks in stream:
        delta = chunks.choices[0].delta
        if delta.content:  # delta.content is None on the last chunk
            print(delta.content, end="", flush=True)
    print()  # newline after stream ends


# Pattern 2 - Preferred and Latest method
async def streaming_response(prompt: str) -> str:
    texts = ""
    async with async_client.chat.completions.stream(
        model="grok-4.3",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    ) as stream:
        async for event in stream:
            # event types can be 'content.delta','content.done', 'chunk', 'message', refusal.delta'
            if event.type == "content.delta":
                texts += event.delta  # So each stream text will get added to the texts

        # After stream exhausted, get the full accumulated completion:
        final = await stream.get_final_completion()
        print("\n--- finish_reason:", final.choices[0].finish_reason)
    return texts
