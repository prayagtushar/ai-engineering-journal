import json
from openai import OpenAI

# Use Pydantic for Schematic Response
from pydantic import BaseModel


client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
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

response = client.chat.completions.parse(
    model="gpt-4o",
    messages=[{"role": "user", "content": "List 3 fruits."}],
    response_format=FruitsList,
)
parsed: FruitsList = response.choices[0].message.parsed
