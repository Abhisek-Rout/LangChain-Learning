from langchain_ollama import OllamaLLM

llm =  OllamaLLM(
    model="gemma3:4b"
)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)

    if user_input == "exit":
        break
    
    result = llm.invoke(chat_history)
    chat_history.append(result)
    print("AI: ", result)
