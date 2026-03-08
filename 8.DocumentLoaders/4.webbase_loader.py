from langchain_ollama import ChatOllama
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model =  ChatOllama(
    model="gemma3:4b"
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the follwing question \n {question} in short from the following text - \n {text}',
    input_variables=['question', 'text']
)

url = "https://www.samsung.com/in/smartphones/galaxy-s25-ultra/"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    'question': 'What are the camera specs of this phone ?',
    'text': docs[0].page_content
})

print(result)