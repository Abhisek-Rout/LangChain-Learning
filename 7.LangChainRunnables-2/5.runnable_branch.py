from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.base import RunnableSequence
from langchain_core.runnables.passthrough import RunnablePassthrough
from langchain_core.runnables.branch import RunnableBranch

model =  ChatOllama(
    model="gemma3:4b"
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a detailed report on the {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarise the following text \n {text}",
    input_variables=['topic']
)

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic': 'Is attack on Iran justified?'}))