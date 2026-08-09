# AI-ML-Learning

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python" />
  </a>
  <img src="https://img.shields.io/badge/Notebooks-Jupyter-orange?style=for-the-badge&logo=jupyter" alt="Jupyter" />
  <img src="https://img.shields.io/badge/Focus-Artificial%20Intelligence%20%26%20Machine%20Learning-success?style=for-the-badge" alt="AI/ML Focus" />
</p>

A project-driven, living collection of hands-on experiments, notes, and mini-projects that document a practical learning path through Artificial Intelligence and Machine Learning. This repository is organized around Jupyter notebooks that you can run, fork, extend, and learn from.

---

## ✨ Quick elevator pitch

Learn by doing: each notebook pairs a short conceptual note with complete, runnable code and a small exploration task. Progress from Python fundamentals to machine learning workflows and then to deep learning experiments and simple deployment demos.

---

## 🚀 What you'll find here

- Topic-by-topic Jupyter notebooks with clear goals and outputs.
- End-to-end examples that follow a production-style ML workflow: data → features → models → evaluation → improvement.
- Mini projects that end with a simple app (Streamlit) or saved model for quick demos.
- Notes, tips, and annotated results so you can learn the "why" and the "how".

---

## 🧭 Repository Structure (short)

```text
AI-ML-Learning/
├── .gitattributes
├── .vscode/                       # Editor settings
├── Basic Python/                  # Core Python concepts and practice problems
├── Deep Leaning/                  # Deep learning notebooks and experiments
├── Machine Learning/              # ML notebooks, tutorials, and small projects
└── README.md
```

> Note: Notebooks are intentionally compact and focused — each one tries to teach a single concept with code you can run and extend.

---

## 🧠 Learning coverage (practical focus)

Foundations
- Python fundamentals: functions, data structures, list/dict comprehensions, and idiomatic scripting
- Numerical computing with NumPy
- Tabular data handling with Pandas
- Visualization basics with Matplotlib (and tips for quick EDA)

Machine Learning
- Supervised learning: linear models, tree-based methods, common classifiers
- Model evaluation: precision, recall, ROC/AUC, confusion matrices, and cross-validation
- Hyperparameter tuning and pipelines (GridSearchCV, Pipelines)
- Feature engineering: encoding, scaling, selection
- Unsupervised learning: clustering and dimensionality reduction (PCA)

Deep Learning & Beyond
- Introductory deep learning experiments (notebook-first approach)
- Basic architectures, model saving/loading, and inference demos
- Notes and pointers toward NLP and generative models (future work)

---

## 🧩 End-to-end ML workflow (applied consistently)

```
Dataset → EDA → Cleaning → Encoding → Scaling → Feature Engineering
→ Train/Test Split → Model Training → Evaluation
→ Cross Validation → Hyperparameter Tuning → Final Model
→ (Optional) Save model → Simple deployment/demo
```

Each project follows the same roadmap so you can compare different approaches on the same footing.

---

## 🌟 Featured projects & examples

- Heart Disease Risk Prediction (Streamlit demo): a complete pipeline from notebook to a lightweight app for interactive exploration.
  - Path: Supervised Learning/Classification/Project
  - Run locally: see the Getting Started section below

- Starter templates: small notebooks that show how to structure experiments and save artifacts (models, scalers, results).

---

## ⚙️ Tech stack

- Language: Python
- Primary medium: Jupyter Notebooks
- Libraries: NumPy, Pandas, Matplotlib, scikit-learn, Streamlit, joblib

---

## 🛠️ Getting started (run notebooks & demos)

1. Clone the repository

```bash
git clone https://github.com/Rohan200511/AI-ML-Learning.git
cd AI-ML-Learning
```

2. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt || pip install numpy pandas matplotlib scikit-learn jupyter streamlit joblib
```

4. Launch Jupyter

```bash
jupyter notebook
```

5. Run a Streamlit demo (example: Heart Disease app)

```bash
cd "Supervised Learning/Classification/Project"
pip install streamlit pandas scikit-learn joblib
streamlit run app.py
```

---

## 🧭 Notebook conventions

- Each notebook begins with a short "Goal" section that describes the learning objective.
- Cells are split into: setup, data loading, EDA, preprocessing, modeling, evaluation, and conclusions.
- Where needed, notebooks save model artifacts with joblib so demos can load them quickly.

---

## 🎯 Roadmap & learning goals

Short-term
- Add more guided exercises for classification and regression
- Expand evaluation notebooks with more robust visualizations and error analysis

Mid-term
- Add basic deep learning tutorials (TensorFlow/PyTorch) and transfer learning demos
- Introduce simple NLP tasks (text classification)

Long-term
- More deployment examples (Docker + Streamlit or simple Flask APIs)
- A small curated curriculum (notebooks ordered for progressive learning)

---

## 🤝 Contributing & collaboration

This repo is primarily a personal learning notebook, but contributions and feedback are welcome. If you want to help:

1. Fork the repo and create a branch: git checkout -b your-feature
2. Add a notebook or improve an existing one with clear goals and runnable code
3. Add data or scripts to a sensible directory (keep data small or add links to external datasets)
4. Open a PR describing what you added and why

Guidelines
- Keep notebooks focused (one concept per notebook)
- Include a short intro and conclusion
- Avoid large datasets in the repo; include download scripts or links instead

---

## 🧠 Tips for learners (how to get the most out of this repo)

- Re-run notebooks and tweak hyperparameters to see effects on metrics
- Try replacing models (e.g., tree → logistic → SVM) and compare results
- Add a short write-up to each notebook: "what I tried, what worked, what didn’t"
- Use version control for notebooks carefully (clear commit messages, avoid committing large binary outputs)

---

## 📚 Resources & references

- scikit-learn documentation: https://scikit-learn.org
- Hands-On Machine Learning (book) — recommended for structured learning
- Official Python docs: https://python.org

---

## 🔒 License

This repository is open for learning purposes. Add your preferred license file if you want to clarify reuse terms.

---

## ✉️ Contact

If you’d like to collaborate or provide feedback, open an issue or a pull request.

---

<p align="center"><i>Learning in public — one notebook, one experiment, one improvement at a time.</i></p>
