from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema

model =  ChatOllama(
    model="gemma3:4b"
)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

# 1st prompt -> detailed report
template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({'topic': 'black hole'})

print(final_result)

# Problem with StructuredOutputParser
# Although we get the output from LLM in json format as we have defined but we cannot validate the output structure
# If you want to validate a specific schema on LLM then u have to use the PydanticOutputParser class