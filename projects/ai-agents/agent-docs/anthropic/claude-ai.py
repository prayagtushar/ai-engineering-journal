# uv add anthropic

import anthropic

# Creates a client that reads ANTHROPIC_API_KEY from your .env file automatically
client = anthropic.Anthropic()

print("Calling Anthropic API...")

# The script pauses here until the response comes back (sync = blocking)
response = client.messages.create(
    model="claude-opus-4-7",
    system="You are Pandora, an AI assistant specialised in Wild life",
    messages=[
        {"role": "user", "content": "Who is Pandora?"},
    ],
    max_tokens=1000,
    temperature=0.7,  # 0 = deterministic, 1 = creative
)

# Anatomy of the response
print(
    f"Content:       {response.content[0].text}"
)  # the actual reply text (first text block)
print(
    f"Stop reason:   {response.stop_reason}"
)  # 'end_turn' | 'max_tokens' | 'stop_sequence' | 'tool_use'
print(f"Input tokens:  {response.usage.input_tokens}")  # tokens you sent
print(f"Output tokens: {response.usage.output_tokens}")  # tokens the model generated
print(f"Model used:    {response.model}")  # actual model (may differ from requested)
print(f"Request ID:    {response.id}")  # useful for debugging in Anthropic console
print(f"Role:          {response.role}")  # always 'assistant'

# The content field is a list because Anthropic supports multiple blocks
# e.g. text block + tool_use block in the same response
for block in response.content:
    if block.type == "text":
        print("TEXT:", block.text)
    elif block.type == "tool_use":
        print("TOOL:", block.name, block.input)

# Available Models
# ┌──────────────────────────────┬─────────┬──────────────────────────────┬───────────────┐
# │ Model                        │ Context │ Best for                     │ Cost (approx) │
# ├──────────────────────────────┼─────────┼──────────────────────────────┼───────────────┤
# │ claude-opus-4-7              │ 200k    │ Complex reasoning            │ $$$$          │
# │ claude-sonnet-4-6            │ 200k    │ General best quality         │ $$$           │
# │ claude-haiku-4-5-20251001    │ 200k    │ High-volume, fast, cheap     │ $             │
# └──────────────────────────────┴─────────┴──────────────────────────────┴───────────────┘
