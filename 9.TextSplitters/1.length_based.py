from langchain_text_splitters.character import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader    

# Create the object for loader
loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=5,
    separator=''
)

result = splitter.split_documents(docs)

print(len(result[1].page_content))
print(result[1].page_content)

print(len(result[2].page_content))
print(result[2].page_content)