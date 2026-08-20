# 🚀 Generative AI Learning Repository

A practical, project-driven collection of hands-on experiments, notes, and mini-projects for learning **Generative AI** with LangChain, chat models, and embeddings.

This folder is organized around runnable Python scripts and Jupyter-based learning experiments that you can fork, extend, and learn from.

---

## 📋 Overview

This directory contains examples for working with:

- **Chat Models** — Using multiple LLM providers through LangChain
- **Embedding Models** — Generating text embeddings for semantic search and similarity tasks
- **Model Providers** — Google Gemini, Mistral AI, and Hugging Face integrations
- **Environment Management** — Secure API key handling with `.env`
- **LangChain Workflows** — Simple, reusable building blocks for AI applications

---

## 📁 Project Structure

```text
Generative AI/
├── ChatModels/
│   ├── chat.py
│   ├── huggingface.py
│   └── localmodels.py
├── EmbeddingModels/
│   ├── embeddings.py
│   └── hugginfaceEmbedding.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ✨ What’s Inside

### Chat Models
The chat examples demonstrate how to query different LLM providers using LangChain.

- `chat.py`  
  Uses:
  - **Mistral AI** via `ChatMistralAI`
  - **Google Gemini** via `ChatGoogleGenerativeAI`

### Embedding Models
The embedding examples demonstrate how to convert text into vector representations.

- `embeddings.py`  
  Uses:
  - **Google Generative AI embeddings** with `gemini-embedding-2`

- `hugginfaceEmbedding.py`  
  Uses:
  - **Hugging Face sentence-transformers embeddings**

---

## 🔑 Required API Keys

Depending on the model you use, you may need the following environment variables:

### Google Generative AI
- **Environment Variable:** `GOOGLE_API_KEY`
- **Used For:** Gemini chat models and embeddings
- **API Key:** https://aistudio.google.com/apikey

### Mistral AI
- **Environment Variable:** `MISTRAL_API_KEY`
- **Used For:** Mistral chat models
- **API Key:** https://console.mistral.ai/

### Hugging Face
- **Environment Variable:** `HUGGINGFACEHUB_API_TOKEN`
- **Used For:** Hugging Face-hosted models and embeddings
- **API Token:** https://huggingface.co/settings/tokens

### Optional
- `OPENAI_API_KEY`
- `GROQ_API_KEY`

---

## 📦 Installation

### Prerequisites
- Python 3.10+
- `uv` recommended, or `pip`

### Install dependencies
```bash
pip install -r requirements.txt
```

If you prefer `uv`:
```bash
uv pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in this directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

> Do not commit `.env` to version control.

---

## 🚀 Quick Start

### Run chat model example
```bash
python ChatModels/chat.py
```

### Run Google embeddings example
```bash
python EmbeddingModels/embeddings.py
```

---

## 🧠 Example Learnings

### `ChatModels/chat.py`
Demonstrates:
- Loading environment variables with `python-dotenv`
- Calling **Mistral AI** with `mistral-large-latest`
- Calling **Gemini** with `gemini-2.5-flash`
- Using temperature to control response creativity

### `EmbeddingModels/embeddings.py`
Demonstrates:
- Creating embeddings with `gemini-embedding-2`
- Generating a single query vector
- Generating vectors for a batch of documents
- Using a fixed embedding dimension of 64

---

## 📚 Dependencies

Common packages used in this folder include:

- `langchain`
- `langchain-core`
- `langchain-community`
- `langchain-google-genai`
- `langchain-mistralai`
- `langchain-huggingface`
- `python-dotenv`
- `requests`
- `faiss-cpu`
- `uvicorn`
- `fastapi`

---

## 🛠 Troubleshooting

### `ModuleNotFoundError`
Make sure dependencies are installed in the active environment:

```bash
pip install -r requirements.txt
```

### Missing API key
If a model fails due to an environment variable error:
1. Check your `.env`
2. Confirm the variable name
3. Restart the script after loading env vars

### Slow local model downloads
Some Hugging Face models may download on first run and take time.

---

## 🎯 Next Steps

- Add more chat providers
- Add RAG examples
- Build a simple chatbot UI
- Add retrieval and vector search demos
- Expand the notebook-based learning path

---

## 🤝 Contributing

Contributions are welcome:
- Improve documentation
- Add more model examples
- Fix typos and naming inconsistencies
- Extend the learning experiments

---

## 📝 Notes

- This folder is part of the larger **AI-ML-Learning** repository
- The code is intended for learning and experimentation
- API usage may incur provider-specific costs depending on model and plan

---

**Status:** Active development
