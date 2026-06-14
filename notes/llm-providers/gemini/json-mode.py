import json
from google import genai
from pydantic import BaseModel

client = genai.Client()

# =============================================
# Approach 1 — Plain JSON mode (no schema)
# =============================================
# Tells Gemini to respond with JSON, but doesn't enforce a structure.
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="List 3 fruits with colors.",
    config=genai.types.GenerateContentConfig(
        response_mime_type="application/json",
        max_output_tokens=200,
    ),
)

# Parse the JSON string into a Python dict/list
data = json.loads(response.text)
print("Plain JSON:", data)

# =============================================
# Approach 2 — Pydantic schema (structured output)
# =============================================
# Gemini will return JSON that matches the Pydantic model exactly.


class Fruits(BaseModel):
    name: str
    color: str


class FruitsList(BaseModel):
    fruits: list[Fruits]


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="List 5 fruits with their colors.",
    config=genai.types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=FruitsList,
    ),
)

# response.text is still raw JSON, but you can parse it into your model:
parsed: FruitsList = FruitsList.model_validate_json(response.text)
print(f"Parsed ({len(parsed.fruits)} fruits):", parsed)
