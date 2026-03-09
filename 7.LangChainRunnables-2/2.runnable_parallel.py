from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.base import RunnableSequence, RunnableParallel

model =  ChatOllama(
    model="gemma3:4b"
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic': 'AI'})

print(result['tweet'])
print(result['linkedin'])