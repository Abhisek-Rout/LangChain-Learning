from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

model =  ChatOllama(
    model="gemma3:4b"
)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

# Fomatting of prompt
prompt1 = template1.invoke({'topic': 'black hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result1.content})

result2 = model.invoke(prompt2)

print(result2.content)