# GenAI Roadmap — "Gen AI to come"

This document outlines a pragmatic, hands-on roadmap to add Generative AI (GenAI) topics to the AI-ML-Learning repository. The intention is notebook-first: short, runnable notebooks that introduce concepts, experiments, and small deployable demos.

## Vision

Bring GenAI experiments into the repo with reproducible notebooks that teach practical skills: prompting, fine-tuning, retrieval-augmented generation (RAG), multimodal pipelines, evaluation, and safety/ethics.

## High-level goals

- Provide beginner-friendly, runnable notebooks that explain core GenAI concepts.
- Show end-to-end examples (data → model → prompt → evaluation → demo).
- Keep resource usage reasonable (use small datasets or public APIs; provide options to run locally or on free cloud tiers).
- Emphasize reproducibility: requirements, small seed datasets, and artifact saving.

## Proposed Notebooks (starter list)

1. 00-GenAI-Intro.ipynb
    - What is GenAI: language models, tokens, decoding.
    - Small demos using an open model (e.g., llama.cpp, or a public API example placeholder).

2. 01-Text-Generation-Basics.ipynb
    - Prompt engineering basics: few-shot, chain-of-thought, temperature, top-p.
    - Local experiments with small open models or remote API examples.

3. 02-Fine-Tuning-Small.ipynb
    - How to fine-tune a small model (or adapter) on a tiny dataset.
    - Use Hugging Face transformers and datasets if available; include optional CPU-friendly path or use colab.

4. 03-RAG-Basics.ipynb
    - Retrieve + generate pipeline: embeddings, vector store, simple retriever, generation with context.
    - Example using small text corpus (e.g., course notes) and open-source embedding method.

5. 04-Multimodal-Intro.ipynb
    - Combine images and text: simple captioning or multimodal retrieval demo.

6. 05-Evaluation-and-Safety.ipynb
    - Automated and human-centered evaluation metrics.
    - Bias, hallucination, rate-limiting, and best-practice notes.

7. 06-GenAI-Deployment-Demo.ipynb
    - Lightweight demo showing a Streamlit app that queries a model or RAG pipeline.

## Tools & libraries

- Hugging Face transformers & datasets
- sentence-transformers (or small embedding alternatives)
- faiss / qdrant (local option: faiss-cpu) or simple in-memory vector store
- LangChain (optional, notebook-friendly usage)
- Streamlit for small demos
- Optional: llama.cpp bindings or other lightweight local inference tools

## Data sources (small & public)

- Small Wikipedia extracts, Project Gutenberg samples, or curated README/notes in repo
- Public CSVs (e.g., UCI datasets trimmed for text tasks)
- Use download scripts rather than committing large files

## Compute & cost guidance

- Provide two paths: (A) low-cost local CPU-compatible examples using very small models/datasets, and (B) cloud/paid API examples (clearly marked) for larger experiments.
- Add notes on estimated runtime, memory and GPU needs per notebook.

## Notebook conventions for GenAI

- Include a short "Goal" section and explicit hardware notes (CPU/GPU required?)
- Provide small example datasets and a script to download/prepare them
- Save artifacts (index, vector store, small model weights) using lightweight formats
- Mark any notebook cells that call paid APIs and provide placeholders for API keys via environment variables

## Starter folder structure suggestion

```
GenAI/
├── 00-GenAI-Intro.ipynb
├── 01-Text-Generation-Basics.ipynb
├── 02-Fine-Tuning-Small.ipynb
├── 03-RAG-Basics.ipynb
├── 04-Multimodal-Intro.ipynb
├── 05-Evaluation-and-Safety.ipynb
└── notes/                           # small datasets, download scripts, templates
```

## Example: Minimal RAG notebook snippet (pseudocode)

```python
# 1. Load small corpus
# 2. Compute embeddings
# 3. Build a simple in-memory vector index
# 4. Given a user query, retrieve top-k documents
# 5. Concatenate context and ask the model to generate
```

Provide concrete code in notebooks using sentence-transformers + a small generator (or API placeholder).

## Ethics & Responsible Use

- Add an explicit section in each notebook on risks, data provenance, and safe prompting
- Provide guidelines on evaluating hallucinations and avoiding sharing private data

## Milestones (example)

- Week 1: Add GenAI intro + text-gen basics notebooks
- Week 2: Add RAG basics and evaluation notebook
- Week 3: Add fine-tuning example and Streamlit demo

## How you can contribute

- Add a notebook and make sure it has a short goal and a small data prep cell
- Avoid adding large model weights or datasets; use download scripts
- Label paid API examples clearly and provide placeholders for API keys

---

If you want, I can create the GenAI folder and add the 00-GenAI-Intro.ipynb starter notebook (simple markdown + small runnable examples), plus update README to reference GenAI.
