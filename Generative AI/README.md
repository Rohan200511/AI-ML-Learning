# 🚀 Generative AI Learning Repository

A comprehensive guide to working with **Generative AI models** using LangChain, including chat models, embeddings, and various model providers.

## 📋 Overview

This repository contains practical examples and implementations for:

- **Chat Models**: Integration with multiple LLM providers (OpenAI, Google Gemini, Mistral AI, Groq, Hugging Face)
- **Embedding Models**: Text embedding generation using Google Generative AI and Hugging Face
- **Model Management**: Local models, API-based models, and inference endpoints
- **LangChain Integration**: Building with LangChain framework for AI applications

### 📁 Project Structure

```
Generative AI/
├── ChatModels/
│   ├── chat.py                 # Mistral AI & Google Gemini integration
│   ├── huggingface.py          # Hugging Face remote models (DeepSeek-R1)
│   └── localmodels.py          # Local model inference (TinyLlama)
├── EmbeddingModels/
│   ├── embeddings.py           # Google Generative AI embeddings
│   └── hugginfaceEmbedding.py  # Hugging Face embeddings
├── requirements.txt            # Python dependencies
├── pyproject.toml             # UV project configuration (when created)
├── uv.lock                    # UV lock file (auto-generated)
└── .env                       # Environment variables (local, not committed)
```

## 🔑 Required API Keys

Depending on which models you use, you'll need the following API keys:

### 1. **Google Generative AI (Gemini)**
- **Models Used**: `gemini-2.5-flash`, `gemini-embedding-2`
- **Get API Key**: https://aistudio.google.com/apikey
- **Environment Variable**: `GOOGLE_API_KEY`
- **Cost**: Free tier available, pay-as-you-go after

### 2. **Mistral AI**
- **Models Used**: `mistral-large-latest`
- **Get API Key**: https://console.mistral.ai/
- **Environment Variable**: `MISTRAL_API_KEY`
- **Cost**: Paid API, free credits for new users

### 3. **Hugging Face**
- **Models Used**: `DeepSeek-R1` (remote), `TinyLlama-1.1B-Chat-v1.0` (local)
- **Get API Key**: https://huggingface.co/settings/tokens
- **Environment Variable**: `HUGGINGFACEHUB_API_TOKEN`
- **Cost**: Free for many models, some require authentication

### 4. **OpenAI (Optional)**
- **Models Used**: Available through LangChain
- **Get API Key**: https://platform.openai.com/api-keys
- **Environment Variable**: `OPENAI_API_KEY`
- **Cost**: Paid API

### 5. **Groq (Optional)**
- **Models Used**: Groq LLM models
- **Get API Key**: https://console.groq.com/
- **Environment Variable**: `GROQ_API_KEY`
- **Cost**: Free tier available

---

## 📦 Installation Guide

### Prerequisites
- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`

### Step 1: Install UV (Recommended)

**macOS & Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Or using Homebrew (macOS):**
```bash
brew install uv
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/Rohan200511/AI-ML-Learning.git
cd AI-ML-Learning/Generative\ AI
```

### Step 3: Create Virtual Environment with UV

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### Step 4: Install Dependencies with UV

```bash
# Install all dependencies
uv pip install -r requirements.txt
```

**Or install individual packages:**
```bash
uv pip install langchain langchain-core langchain-community langgraph
uv pip install langchain-openai langchain-google-genai langchain-groq langchain-mistralai
uv pip install python-dotenv faiss-cpu tiktoken
uv pip install fastapi uvicorn requests
uv pip install langchain_huggingface
```

### Step 5: Set Up Environment Variables

Create a `.env` file in the `Generative AI` directory:

```bash
touch .env
```

Add your API keys:

```env
# Google Generative AI
GOOGLE_API_KEY=your_google_api_key_here

# Mistral AI
MISTRAL_API_KEY=your_mistral_api_key_here

# Hugging Face
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here

# OpenAI (Optional)
OPENAI_API_KEY=your_openai_api_key_here

# Groq (Optional)
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ **Important**: Never commit `.env` files to version control. They are already in `.gitignore`.

---

## 🎯 Quick Start Examples

### 1. Basic Chat with Mistral AI & Google Gemini

```bash
python ChatModels/chat.py
```

**What it does:**
- Queries Mistral AI's `mistral-large-latest` model
- Queries Google's `gemini-2.5-flash` model
- Demonstrates temperature parameter for controlling creativity

### 2. Hugging Face Remote Model (DeepSeek-R1)

```bash
python ChatModels/huggingface.py
```

**What it does:**
- Uses DeepSeek-R1 model from Hugging Face Hub
- Requires `HUGGINGFACEHUB_API_TOKEN` environment variable
- Best for complex reasoning tasks

### 3. Local Model Inference (TinyLlama)

```bash
python ChatModels/localmodels.py
```

**What it does:**
- Runs TinyLlama-1.1B model locally (no API key needed!)
- Requires ~2GB of memory
- Perfect for testing without API costs
- First run will download the model (~1.2GB)

### 4. Text Embeddings with Google Generative AI

```bash
python EmbeddingModels/embeddings.py
```

**What it does:**
- Generates embeddings using Google's `gemini-embedding-2` model
- Creates 64-dimensional vectors
- Shows single query embedding and batch document embeddings
- Useful for semantic search and similarity tasks

### 5. Hugging Face Embeddings

```bash
python EmbeddingModels/hugginfaceEmbedding.py
```

**What it does:**
- Uses `sentence-transformers/all-MiniLM-L6-v2` model
- Requires NO API key (runs locally or via Hugging Face Hub)
- Generates embeddings for batch text documents
- Lightweight and fast for production use

---

## 📚 Dependencies Breakdown

```
langchain                 # Core LangChain framework
langchain-core           # Core components
langchain-community      # Community integrations
langgraph               # Graph-based LLM workflows
langchain-openai        # OpenAI integration
langchain-google-genai  # Google Generative AI integration
langchain-groq          # Groq integration
langchain-mistralai     # Mistral AI integration
langchain_huggingface   # Hugging Face integration
python-dotenv           # Environment variable management
faiss-cpu               # Vector similarity search (CPU version)
tiktoken                # Token counting for OpenAI models
fastapi                 # Web framework for APIs
uvicorn                 # ASGI server
requests                # HTTP library
```

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'langchain'"
**Solution:**
```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Reinstall dependencies
uv pip install -r requirements.txt
```

### Issue: "GOOGLE_API_KEY not found"
**Solution:**
1. Create `.env` file in the project root
2. Add your API key: `GOOGLE_API_KEY=your_key_here`
3. Ensure `python-dotenv` is installed: `uv pip install python-dotenv`
4. Restart your Python script

### Issue: "Model download taking too long" (for local models)
**Solution:**
- First run downloads the model (~1-2GB depending on model)
- Subsequent runs load from cache
- Consider using a wired connection for faster downloads

### Issue: "CUDA out of memory" errors
**Solution:**
- Use smaller models (TinyLlama instead of larger models)
- Reduce `max_new_tokens` in `localmodels.py`
- Use GPU quantization options

---

## 📖 Learning Resources

### Documentation
- [LangChain Docs](https://python.langchain.com/)
- [Google Generative AI](https://ai.google.dev/docs)
- [Mistral AI Docs](https://docs.mistral.ai/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)

### Key Concepts
- **Temperature**: Controls randomness (0.0 = deterministic, 1.0+ = creative)
- **Tokens**: Units of text (roughly 4 characters = 1 token)
- **Embeddings**: Vector representations of text for semantic similarity
- **LLM**: Large Language Model

---

## 🚀 Next Steps

1. **Get API Keys**: Obtain keys from Google AI Studio, Mistral Console, and Hugging Face
2. **Create `.env` File**: Add your credentials securely
3. **Run Examples**: Start with `chat.py` to verify setup
4. **Explore**: Modify examples and build your own applications
5. **Build Projects**: Use these as building blocks for RAG, chatbots, and more

---

## 📝 Notes

- The `.gitignore` file prevents committing sensitive files (`.env`, `uv.lock`, `.python-version`)
- Always use virtual environments to avoid dependency conflicts
- Start with free/low-cost models (Gemini free tier, local models) before scaling
- Monitor API usage and costs, especially with paid providers

---

## 🤝 Contributing

Feel free to:
- Add more model examples
- Improve documentation
- Report issues
- Share optimization tips

---

## 📄 License

This project is part of the AI-ML-Learning repository.

---

**Last Updated**: 18/08/2026
**Status**: Active Development ✨
