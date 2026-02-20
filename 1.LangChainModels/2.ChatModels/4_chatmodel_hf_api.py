from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

# Get the token from environment
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

if not hf_token or hf_token.startswith("hf_"):
    print("Warning: Make sure you have a valid HuggingFace token in .env")
    print("Get your token at: https://huggingface.co/settings/tokens")

# Create the HuggingFace LLM endpoint
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

# Wrap it with ChatHuggingFace for chat interface
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")

print(result)
print(result.content)