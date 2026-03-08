from langchain_community.document_loaders import CSVLoader

# Create the respective loader object
loader = CSVLoader(file_path='Social_Network_Ads.csv')

# Invoke the load() method to get the document list
docs = loader.load()

print(len(docs))
print(docs[1])