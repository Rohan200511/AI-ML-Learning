import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

data = PyPDFLoader("Documents loaders/deeplearning.pdf" )
docs = data.load()

splitter = RecursiveCharacterTextSplitter(chunk_size = 1000 , chunk_overlap = 200)
chunks = splitter.split_documents(docs)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","""You are an Ai that summarizes the text."""),
        ("human" , "{data}")
    ]
)

model = ChatMistralAI(model_name='mistral-small-2506')

final_prompt = prompt.format_messages(data = docs)

response = model.invoke(final_prompt)

print(response.content)
