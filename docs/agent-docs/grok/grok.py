# xAI (Grok) uses an OpenAI-compatible API, so we use the openai SDK
# with a custom base_url pointing to https://api.x.ai/v1
from openai import OpenAI

# NOTE: OpenAI SDK reads OPENAI_API_KEY by default. Set it to your xAI key.
# The only difference from OpenAI: a different base_url and model name.
# All parameters (messages, max_tokens, temperature, etc.) work identically.
agent = OpenAI(base_url="https://api.x.ai/v1")  # set OPENAI_API_KEY to your xAI key in .env

print("Calling Grok (xAI) API...")

# Sync call — script blocks until the response is returned
response = agent.chat.completions.create(
    model="grok-4.3",
    messages=[
        {
            "role": "system",
            "content": "You are Pandora, an AI assistant specialised in Wild life",
        },
        {"role": "user", "content": "Who is pandora?"},
    ],
    max_tokens=1000,
    temperature=0.7,  # 0 = deterministic, 1 = creative
)

# Response anatomy — same structure as OpenAI responses
print(f"Content:       {response.choices[0].message.content}")  # the actual reply text
print(
    f"Finish reason: {response.choices[0].finish_reason}"
)  # 'stop' | 'length' | 'tool_calls' | 'content_filter'

# Finish Reasons
# ┌─────────────────┬──────────────────────────────────────────────────────┐
# │ Reason          │ Meaning                                              │
# ├─────────────────┼──────────────────────────────────────────────────────┤
# │ stop            │ Model naturally stopped (found a stopping sequence)  │
# │ length          │ Hit max_tokens limit — response truncated            │
# │ tool_calls      │ Model wants to call a tool/function                  │
# │ content_filter  │ Response flagged by content moderation filter        │
# └─────────────────┴──────────────────────────────────────────────────────┘
print(f"Prompt tokens: {response.usage.prompt_tokens}")  # tokens you sent
print(
    f"Completion tokens: {response.usage.completion_tokens}"
)  # tokens the model generated
print(f"Total tokens:  {response.usage.total_tokens}")  # sum of both
print(f"Model used:    {response.model}")  # actual model (may differ from requested)
print(f"Request ID:    {response.id}")  # useful for debugging

#  Available Models
# ┌──────────────┬─────────┬──────────────────────────┬───────────────┐
# │ Model        │ Context │ Best for                 │ Cost (approx) │
# ├──────────────┼─────────┼──────────────────────────┼───────────────┤
# │ grok-4.7     │ 1M      │ Latest frontier model    │ $$$$          │
# │ grok-4.3     │ 131k    │ General purpose          │ $$$           │
# │ grok-4.3-mini│ 131k    │ Fast, cheap              │ $             │
# └──────────────┴─────────┴──────────────────────────┴───────────────┘
