import streamlit as st
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

# Custom CSS for CourseMateAi branding
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            font-size: 42px;
            font-weight: 900;
            text-align: center;
            color: #00FF7F;
            margin-bottom: 5px;
        }
        .sub-title {
            font-size: 18px;
            text-align: center;
            color: #FFD700;
            margin-bottom: 30px;
        }
        .search-bar input {
            width: 100%;
            padding: 15px;
            border-radius: 30px;
            border: 2px solid #00FF7F;
            font-size: 18px;
            background-color: #1c1c1c;
            color: #ffffff;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff416c, #ff4b2b);
            color: white;
            font-size: 18px;
            border-radius: 25px;
            padding: 10px 25px;
            font-weight: bold;
        }
        .response-box {
            background-color: #111111;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            border: 1px solid #00FF7F;
            font-size: 16px;
            color: #00FFFF;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>📘 CourseMateAi</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Your Smart Study Companion</div>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📂 Navigation")
st.sidebar.markdown("- Upload PDF")
st.sidebar.markdown("- Ask Questions")
st.sidebar.markdown("- About CourseMateAi")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    temp_path = os.path.join("Documents loaders", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    data = PyPDFLoader(temp_path)
    docs = data.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorStore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    retriever = vectorStore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5}
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    prompt = ChatPromptTemplate.from_messages([
        ('system', """You are a helpful AI assistant.
        Use ONLY the provided context to answer the question.
        If the answer is not present in the context,
        say: "I could not find the answer in the document."
        """),
        ('human', """Context:{context}
        Question:{question}""")
    ])

    # Search-bar style input
    st.markdown("<div class='search-bar'>", unsafe_allow_html=True)
    query = st.text_input("🔍 Ask CourseMateAi:", placeholder="Type your question here...")
    st.markdown("</div>", unsafe_allow_html=True)

    if query:
        docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        final_prompt = prompt.invoke({"context": context, "question": query})
        response = llm.invoke(final_prompt)

        st.markdown("<div class='response-box'>", unsafe_allow_html=True)
        st.markdown(f"**🤖 Answer:** {response.content}")
        st.markdown("</div>", unsafe_allow_html=True)
