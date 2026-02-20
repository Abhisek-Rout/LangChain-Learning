from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(
    model="gemma3:4b"
)

st.header('Greeting user playground')

user_name = st.text_input("Enter your name?")

template = PromptTemplate(
    template="Greet the user with 5 different languages in new lines. Specify which language you are using. The name of user is {user_name}",
    input_variables=["user_name"]
)

if st.button("Greet"):
    if user_name:
        # Approach-1
        # template.invoke() returns a PromptValue after variable replacement
        formatted_prompt = template.invoke(
            {
                "user_name": user_name
            }
        )

        # Approach-2
        # formatted_prompt = template.format(user_name=user_name)

        result = llm.invoke(formatted_prompt)
        st.write(result)

        #########################################################
        
        # Approach-3
        # Using chaining technique
        chain = template | llm
        result = chain.invoke(
            {
                "user_name": user_name
            }
        )
        st.write(result)

    else:
        st.warning("Please enter you name first")