from openai import OpenAI

agent = OpenAI()

response = agent.chat.completions.create(
    model="gpt-4o",
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

print(f"Content:       {response.choices[0].message.content}")  # the actual reply text
print(
    f"Finish reason: {response.choices[0].finish_reason}"
)  # 'stop' | 'length' | 'tool_calls' | 'content_filter'
print(f"Prompt tokens: {response.usage.prompt_tokens}")  # tokens you sent
print(
    f"Completion tokens: {response.usage.completion_tokens}"
)  # tokens the model generated
print(f"Total tokens:  {response.usage.total_tokens}")  # sum of both
print(f"Model used:    {response.model}")  # actual model (may differ from requested)
print(f"Request ID:    {response.id}")  # useful for debugging in OpenAI dashboard

#  Available Models
# ┌──────────────┬─────────┬──────────────────────────┬───────────────┐
# │ Model        │ Context │ Best for                 │ Cost (approx) │
# ├──────────────┼─────────┼──────────────────────────┼───────────────┤
# │ gpt-5.4      │ 128k    │ Latest frontier model    │ $$$$          │
# │ gpt-5.2      │ 128k    │ General best quality     │ $$$           │
# │ gpt-4.1      │ 1M      │ Long context, reliable   │ $$$           │
# │ gpt-4o       │ 128k    │ Legacy best quality      │ $$$           │
# │ gpt-4o-mini  │ 128k    │ High-volume, cost-sens.  │ $             │
# │ o3           │ 200k    │ Complex reasoning        │ $$$           │
# │ o4-mini      │ 200k    │ Reasoning, cheaper       │ $$            │
# └──────────────┴─────────┴──────────────────────────┴───────────────┘
