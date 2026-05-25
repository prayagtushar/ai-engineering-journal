import asyncio
from google import genai

# Two ways to create an async Gemini client:
#
# 1. client.aio.models.generate_content()    ← preferred, uses same client
#    client = genai.Client()
#    response = await client.aio.models.generate_content(...)
#
# 2. from google.genai import aio             ← explicit async client
#    async_client = aio.Client()
#    response = await async_client.models.generate_content(...)
#
# Both work identically. Option 1 is recommended.

client = genai.Client()


async def completion(prompt: str):
    async_response = await client.aio.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={"max_output_tokens": 1000},
    )
    return async_response.text


# Gather runs multiple async tasks CONCURRENTLY (not one after another)
async def batch_completion(prompts: list[str]) -> list:
    tasks = [completion(p) for p in prompts]
    print("  → gathering all tasks concurrently...")

    # asyncio.gather runs all tasks at the same time and waits for all to finish
    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    prompts = ["Tell me a joke", "What is Python?", "What is Asyncio?"]

    # asyncio.run() is the entry point for any async program
    results = asyncio.run(batch_completion(prompts))

    print("\n--- Final results ---")
    for i, r in enumerate(results):
        print(f"  Result {i + 1}: {r[:80]}")
