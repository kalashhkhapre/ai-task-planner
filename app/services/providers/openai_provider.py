from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the AzureOpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2025-01-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT") # type: ignore
)

def generate_response(prompt: str):
    response = client.chat.completions.create(
        model=os.getenv("AZURE_DEPLOYMENT_NAME"),  # type: ignore
        messages=[
            {
                "role": "system",
                "content": "You are an AI task planning assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
