from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-turbo")

result = model.invoke("What is the capital of India?")

print(result)
print(result.content)