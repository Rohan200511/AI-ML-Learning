import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders import TextLoader
data = TextLoader("Documents loaders/notes.txt" )

docs = data.load()

print(docs[0].page_content)
print(len(docs))