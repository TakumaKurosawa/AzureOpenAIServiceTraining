import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model=os.environ.get("AZURE_OPENAI_DEPLOYMENT_MODEL"),
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"},
    ],
)
generated_text = response.choices[0].message.content

print("Response: " + generated_text + "\n")
