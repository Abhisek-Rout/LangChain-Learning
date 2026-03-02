from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

# Build the chain pipleline
# How the parser helps here?
# Ans: If parser wouldn't have been there then you would have written custom logic to extract content out of the result and give that as an input to the next template
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)