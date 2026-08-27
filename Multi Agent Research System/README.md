# 🔬 DeepTrace --- Multi-Agent AI Research System

> **Search deeper. Understand better.**
>
> DeepTrace is a multi-agent AI research system where specialized AI
> agents collaborate to discover sources, investigate content,
> synthesize a structured report, and critically review the final
> answer.

------------------------------------------------------------------------

## ✨ What is DeepTrace?

DeepTrace turns a research question into a structured research workflow.

Instead of asking one LLM to do everything, the system separates the
work into four stages:

``` text
Research Question
       │
       ▼
┌─────────────────┐
│  🔎 Search Agent │
│  Find sources    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  📖 Reader Agent │
│  Scrape / read   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ✍️ Writer Chain │
│  Synthesize      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 🧐 Critic Chain  │
│ Review + score   │
└────────┬────────┘
         │
         ▼
   Final Research Report
```

------------------------------------------------------------------------

## 🚀 Features

-   🔎 **Web Search Agent** --- searches for recent and relevant
    information using Tavily.
-   📖 **Reader Agent** --- selects a relevant source and extracts
    deeper page content.
-   ✍️ **Research Writer** --- converts gathered research into a
    structured report.
-   🧐 **Research Critic** --- evaluates the generated report and
    provides a score, strengths, weaknesses, and verdict.
-   🖥️ **Streamlit UI** --- interactive research interface with pipeline
    progress.
-   📑 **Markdown report download**.
-   🔬 **Research Trail** --- inspect intermediate search and reader
    outputs.
-   ⚡ **Modular multi-agent architecture** --- each stage has a focused
    responsibility.

------------------------------------------------------------------------

## 🧠 Architecture

### 1. Search Agent

The Search Agent is created with LangChain's agent API and receives the
custom `web_search` tool.

``` python
def build_seacrh_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )
```

Its job is to find recent, reliable information and return useful source
URLs and snippets.

------------------------------------------------------------------------

### 2. Reader Agent

The Reader Agent receives the `scrape_url` tool.

``` python
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )
```

The agent is asked to choose a relevant URL from the search results and
investigate it in more depth.

------------------------------------------------------------------------

### 3. Writer Chain

The Writer is implemented as a LangChain prompt → model → output parser
chain.

``` python
writer_chain = (
    writer_prompt
    | llm
    | StrOutputParser()
)
```

The generated report is structured around:

-   Introduction
-   Key Findings
-   Conclusion
-   Sources

------------------------------------------------------------------------

### 4. Critic Chain

The Critic receives the generated report and evaluates it.

``` python
critic_chain = (
    critic_prompt
    | llm
    | StrOutputParser()
)
```

The expected format is:

``` text
Score: X/10

Strengths:
- ...

Areas to Improve:
- ...

One line verdict:
...
```

This gives the workflow a dedicated quality-control stage.

------------------------------------------------------------------------

# 🏗️ Project Structure

``` text
Multi Agent Research System/
│
├── app.py
├── Agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .env
│
└── .streamlit/
    └── config.toml
```

### `app.py`

Streamlit frontend and user interaction.

### `Agents.py`

Defines:

-   Mistral LLM
-   Search Agent
-   Reader Agent
-   Writer Chain
-   Critic Chain

### `tools.py`

Contains:

-   Tavily web search
-   URL scraping with Requests + BeautifulSoup

### `pipeline.py`

Connects all four stages into the research workflow.

------------------------------------------------------------------------

# ⚙️ Tech Stack

  Technology      Purpose
  --------------- ------------------------------------
  Python          Core application
  Streamlit       Web UI
  LangChain       Agents, prompts, chains, and tools
  Mistral AI      LLM
  Tavily          Web search
  Requests        HTTP requests
  BeautifulSoup   Web-page text extraction
  python-dotenv   Environment variables
  Rich            Terminal output

------------------------------------------------------------------------

# 🔑 Environment Variables

Create a `.env` file in the project root:

``` env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Never commit `.env` to GitHub.

Add:

``` gitignore
.env
__pycache__/
.streamlit/secrets.toml
```

------------------------------------------------------------------------

# 📦 Installation

## 1. Clone the repository

``` bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the URL with your GitHub repository.

------------------------------------------------------------------------

## 2. Create a virtual environment

### Windows

``` bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

------------------------------------------------------------------------

## 3. Install dependencies

``` bash
pip install -r requirements.txt
```

The project uses packages including:

``` text
streamlit
langchain
langchain-core
langchain-mistralai
tavily-python
requests
beautifulsoup4
python-dotenv
rich
```

------------------------------------------------------------------------

## 4. Configure API keys

Create `.env`:

``` env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

------------------------------------------------------------------------

# ▶️ Run Locally

Start the Streamlit application:

``` bash
streamlit run app.py
```

Then open the local Streamlit URL, typically:

``` text
http://localhost:8501
```

------------------------------------------------------------------------

# 🔬 How the Pipeline Works

The complete workflow is implemented in `pipeline.py`.

Conceptually:

``` python
def run_research_pipeline(topic: str) -> dict:

    state = {}

    # 1. Search
    # 2. Read
    # 3. Write
    # 4. Critique

    return state
```

The stages pass information forward:

``` text
topic
  │
  ▼
Search Agent
  │
  │ search_results
  ▼
Reader Agent
  │
  │ scraped_content
  ▼
Writer Chain
  │
  │ report
  ▼
Critic Chain
  │
  │ feedback
  ▼
Final state
```

The returned state contains the intermediate research artifacts and
final outputs.

------------------------------------------------------------------------

# 🛠️ Custom Tools

## Web Search

The `web_search` tool uses Tavily:

``` python
@tool
def web_search(query: str) -> str:
    results = tavily.search(
        query=query,
        max_results=5,
    )

    return ...
```

The tool is exposed to the Search Agent.

------------------------------------------------------------------------

## URL Scraping

The Reader Agent can use:

``` python
@tool
def scrape_url(url: str) -> str:
    ...
```

The scraper:

1.  Sends an HTTP request.
2.  Parses the page with BeautifulSoup.
3.  Removes unnecessary elements such as scripts, styles, navigation,
    and footers.
4.  Returns cleaned page text.

Example:

``` python
response = requests.get(
    url,
    timeout=8,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)
```

------------------------------------------------------------------------

# 🖥️ Using the UI

1.  Enter a research topic.
2.  Click **Start Deep Research**.
3.  The Search Agent finds sources.
4.  The Reader Agent investigates a relevant source.
5.  The Writer Chain creates the report.
6.  The Critic Chain reviews the report.
7.  Inspect the Research Trail if needed.
8.  Download the final Markdown report.

Example questions:

``` text
What are the latest developments in quantum computing?

How are AI agents changing software engineering?

What is the current state of fusion energy?

How is CRISPR being used in medicine?
```

For best results, ask a topic that benefits from current web research.

------------------------------------------------------------------------

# 🧩 Extending the System

The architecture is modular, so individual agents and tools can be
extended independently.

## Add another tool

Create a tool in `tools.py`:

``` python
from langchain.tools import tool

@tool
def my_custom_tool(query: str) -> str:
    """Describe what this tool does."""
    # Your implementation
    return "result"
```

Then expose it to an agent:

``` python
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[
            web_search,
            my_custom_tool,
        ],
    )
```

------------------------------------------------------------------------

## Add another agent

You can create specialized agents for:

-   Fact checking
-   Citation verification
-   Data analysis
-   Academic-paper research
-   Market research
-   Competitive analysis

Example:

``` python
def build_fact_checker():
    return create_agent(
        model=llm,
        tools=[web_search],
    )
```

Then add that stage to the pipeline.

------------------------------------------------------------------------

## Add a new pipeline stage

For example:

``` python
state["fact_check"] = fact_checker.invoke(
    {
        "messages": [
            (
                "user",
                f"Fact-check this report:\n{state['report']}"
            )
        ]
    }
)
```

The result can then be passed to the Critic or Writer.

------------------------------------------------------------------------

# 📊 Why Multiple Agents?

A single LLM call can answer a question, but research often requires
different responsibilities.

DeepTrace separates:

``` text
Discovery
   ↓
Investigation
   ↓
Synthesis
   ↓
Evaluation
```

This makes it easier to:

-   Replace individual components.
-   Add specialized tools.
-   Inspect intermediate outputs.
-   Add quality-control stages.
-   Experiment with different prompts and models.
-   Extend the workflow without rewriting the entire system.

------------------------------------------------------------------------

# ⚠️ Important Notes

### Web content

The system relies on external websites. Some pages may:

-   Block automated requests.
-   Require JavaScript.
-   Return incomplete content.
-   Change their HTML structure.

The scraper is therefore not a universal browser.

### Research quality

The Critic provides an additional review layer, but its score is still
generated by an LLM. Treat it as an evaluation signal, not an objective
truth score.

### API usage

Mistral and Tavily usage may incur API costs depending on the account
and plan being used.

### Security

Never commit API keys.

Keep:

``` text
.env
```

private.

------------------------------------------------------------------------

# 🐛 Troubleshooting

## `ModuleNotFoundError`

Make sure your environment is active:

``` bash
python -m venv .venv
```

Then install:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Wrong `agents` package is imported

Python can accidentally import an unrelated package named `agents`.

Check what Python is loading:

``` python
import agents

print(agents.__file__)
```

It should point to your project module.

If necessary, rename the local module to something more unique, such as:

``` text
research_agents.py
```

and update imports.

------------------------------------------------------------------------

## API key errors

Make sure `.env` exists in the project root:

``` text
Multi Agent Research System/
├── app.py
├── Agents.py
├── tools.py
├── pipeline.py
└── .env
```

Then restart Streamlit.

------------------------------------------------------------------------

# 🚀 Deployment

DeepTrace is built as a Streamlit application.

For deployment, make sure the hosting environment has:

1.  The project files.
2.  All Python dependencies.
3.  `MISTRAL_API_KEY`.
4.  `TAVILY_API_KEY`.

For hosted environments, use the platform's secret-management system
instead of committing `.env`.

The application can later be split into:

``` text
Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
Multi-Agent Research Pipeline
```

This is a natural next step if you want to separate the UI from the
research backend.

------------------------------------------------------------------------

# 🔮 Future Improvements

-   [ ] True live agent-status callbacks
-   [ ] Parallel source investigation
-   [ ] Multi-source synthesis
-   [ ] Citation verification
-   [ ] Source credibility scoring
-   [ ] Persistent research history
-   [ ] PDF report generation
-   [ ] Research memory
-   [ ] FastAPI backend
-   [ ] React / Next.js frontend
-   [ ] Authentication
-   [ ] Streaming agent responses
-   [ ] Long-term research projects

------------------------------------------------------------------------

# 👨‍💻 Project Goal

DeepTrace was built to explore how **multi-agent LLM systems** can turn
open-ended web research into a structured and inspectable workflow.

The core idea:

> **Don't make one AI do everything. Give specialized agents clear
> responsibilities and let them collaborate.**

------------------------------------------------------------------------

## ⭐ Contributing

Pull requests, improvements, new tools, and agent ideas are welcome.

A simple contribution flow:

``` bash
git checkout -b feature/my-improvement
git add .
git commit -m "Add my improvement"
git push origin feature/my-improvement
```

Then open a pull request on GitHub.

------------------------------------------------------------------------

