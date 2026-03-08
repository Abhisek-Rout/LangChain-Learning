from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders.text import TextLoader

model =  ChatOllama(
    model="gemma3:4b"
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=['poem']
)

# Create an object for document
loader = TextLoader('cricket.txt', encoding='utf-8')

# Eager loading
# It returns a lit of langchain doc object
docs = loader.load()

print(type(docs))
print(len(docs))

print(type(docs[0]))

# How to view the doc content and metadata?
print(docs[0].page_content)
print(docs[0].metadata)

# Chain formation
chain = prompt | model | parser

# Use the content from document loader in your pipeline
print(chain.invoke({'poem': docs[0].page_content}))