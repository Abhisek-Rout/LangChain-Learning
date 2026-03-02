from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser

model =  ChatOllama(
    model="gemma3:4b"
)

parser = JsonOutputParser()

# 1st prompt -> detailed report
template = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({})

print(final_result)
print(type(final_result))

# Problem with JSON ouput parser
# Although we get the output from LLM in json format but we cannot enforce a specific schema
# If you want to enforce a specific schema on LLM then u have to use the StructuredOutputParser class