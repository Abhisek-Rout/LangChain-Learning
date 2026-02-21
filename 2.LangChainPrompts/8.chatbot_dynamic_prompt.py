from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

llm =  OllamaLLM(
    model="gemma3:4b"
)

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

formatted_prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "long-off"
})

response = llm.invoke(formatted_prompt)

print(response)