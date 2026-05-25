# uv add anthropic

import asyncio
from anthropic import AsyncAnthropic

async_client = AsyncAnthropic()


async def completion(prompt: str):
    async_response = await async_client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )
    return async_response.content[0].text


# Gather runs multiple async tasks CONCURRENTLY (not one after another)
async def batch_completion(prompts: list[str]) -> list:
    tasks = [completion(p) for p in prompts]
    print("  -> gathering all tasks concurrently...")

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
