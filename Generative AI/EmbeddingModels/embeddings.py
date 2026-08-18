from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    dimensions = 64
)

vector = embeddings.embed_query("Hi, My name is Rohan")

print(vector)

print("\n ------------------------------------------------------------ \n")

texts = [
    "Hello this is Rohan Gupta",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]

print(embeddings.embed_documents(texts))