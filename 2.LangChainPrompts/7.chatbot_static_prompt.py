from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm =  OllamaLLM(
    model="gemma3:4b"
)

chat_history = [
    SystemMessage("You are a helpful assistant. Assist the user as per request")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))

    if user_input == "exit":
        break
    
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(result))
    print("AI: ", result)

print(chat_history)
