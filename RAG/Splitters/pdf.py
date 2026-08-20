import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("Documents loaders/GRU.pdf" )

spillter = RecursiveCharacterTextSplitter(
    chunk_size = 1000 , 
    chunk_overlap = 10
)

docs = data.load()

chunks = spillter.split_documents(docs)

print((chunks[0].page_content))