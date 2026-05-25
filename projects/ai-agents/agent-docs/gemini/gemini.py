from google import genai
from google.genai import types

# Creates a client that reads GEMINI_API_KEY from your .env file automatically
# Install: uv add google-genai
client = genai.Client()

print("Calling Gemini API...")

# The script pauses here until the response comes back (sync = blocking)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Who is Pandora?",
    config=types.GenerateContentConfig(
        system_instruction="You are Pandora, an AI assistant specialised in Wild life",
        max_output_tokens=1000,
        temperature=0.7,  # 0 = deterministic, 1 = creative
    ),
)

print(f"Content:       {response.text}")  # the actual reply text
print(
    f"Finish reason: {response.candidates[0].finish_reason}"
)  # 'STOP' | 'MAX_TOKENS' | 'SAFETY' | 'RECITATION' | 'OTHER'
print(
    f"Prompt tokens:      {response.usage_metadata.prompt_token_count}"
)  # tokens you sent
print(
    f"Completion tokens:  {response.usage_metadata.candidates_token_count}"
)  # tokens the model generated
print(
    f"Total tokens:       {response.usage_metadata.total_token_count}"
)  # sum of both
print(f"Model used:    {response.model_version}")  # actual model version

#  Available Models
# ┌──────────────────────┬─────────┬──────────────────────────────┬───────────────┐
# │ Model                │ Context │ Best for                     │ Cost (approx) │
# ├──────────────────────┼─────────┼──────────────────────────────┼───────────────┤
# │ gemini-3.5-flash     │ 1M      │ Latest fast generation       │ $$            │
# │ gemini-2.5-pro       │ 1M      │ Complex reasoning            │ $$$           │
# │ gemini-2.5-flash     │ 1M      │ Balanced speed/quality       │ $$            │
# │ gemini-2.0-flash     │ 1M      │ Legacy fast, general purpose │ $             │
# └──────────────────────┴─────────┴──────────────────────────────┴───────────────┘