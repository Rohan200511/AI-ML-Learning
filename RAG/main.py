import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader

from langchain_core.prompts import ChatPromptTemplate

data = PyPDFLoader("Documents loaders/GRU.pdf" )
docs = data.load()

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
