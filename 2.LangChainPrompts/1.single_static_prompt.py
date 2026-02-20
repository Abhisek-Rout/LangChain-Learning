from langchain_ollama import OllamaLLM
import streamlit as st

llm = OllamaLLM(
    model="gemma3:4b"
)

st.header("Research Tool")

user_input = st.text_input("Enter your Prompt")

if st.button("Summarize"):
    if user_input:
        result = llm.invoke(user_input)
        st.write(result)
    else:
        st.warning("Please enter a prompt first")