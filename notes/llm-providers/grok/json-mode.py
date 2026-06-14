# xAI (Grok) uses an OpenAI-compatible API — same SDK, different base_url
# NOTE: OpenAI SDK reads OPENAI_API_KEY by default. Set it to your xAI key.
import json
from openai import OpenAI

# Use Pydantic for Schematic Response
from pydantic import BaseModel


client = OpenAI(base_url="https://api.x.ai/v1")

response = client.chat.completions.create(
    model="grok-4.3",
    max_tokens=200,
    messages=[
        {"role": "system", "content": "Always respond with JSON."},
        {"role": "user", "content": "List 3 fruits with colors."},
    ],
    response_format={"type": "json_object"},
)
# Now this will return in valid JSON [ Not schematic]
data = json.loads(response.choices[0].message.content)


class Fruits(BaseModel):
    name: str
    color: str

class FruitsList(BaseModel):
    fruits: list[Fruits]

# NOTE: .chat.completions.parse() may not work on xAI (uses OpenAI's structured output format).
# Use the json_object approach above for reliable results with xAI.
response = client.chat.completions.parse(
    model="grok-4.3",
    messages=[{"role": "user", "content": "List 3 fruits."}],
    response_format=FruitsList,
)
parsed: FruitsList = response.choices[0].message.parsed
