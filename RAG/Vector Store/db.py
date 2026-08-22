import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

embedding_model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

vectorStore = Chroma.from_documents(documents=docs , embedding=embedding_model , persist_directory="chroma_db")

result = vectorStore.similarity_search("What is used for data analysis" , k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)

retriever = vectorStore.as_retriever()

docs = retriever.invoke("Explain Deep Learning")

for d in docs:
    print(d.page_content)