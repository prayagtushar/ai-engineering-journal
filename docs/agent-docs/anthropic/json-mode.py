# uv add anthropic
# uv add pydantic

import json
from anthropic import Anthropic

# Use Pydantic for schematic response
from pydantic import BaseModel

client = Anthropic()

# --- Approach 1: JSON via output_config (native — SDK v0.103+) ---
# Anthropic now has native structured output support via output_config.
# No need for system prompt hacks anymore.

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "List 3 fruits with their colors as a JSON array of {name, color}."},
    ],
    output_config={"format": "json_object"},  # tells the API to return valid JSON
)
data = json.loads(response.content[0].text)


class Fruit(BaseModel):
    name: str
    color: str


class FruitList(BaseModel):
    fruits: list[Fruit]


# --- Approach 2: Structured output with Pydantic schema ---
# You can also pass a JSON schema to enforce the exact structure.

schema = FruitList.model_json_schema()

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=500,
    messages=[{"role": "user", "content": "List 3 fruits with their colors."}],
    output_config={
        "format": "json_object",
        "schema": schema,
    },
)

parsed = FruitList.model_validate_json(response.content[0].text)
