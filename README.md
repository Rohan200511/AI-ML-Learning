# AI-ML-Learning

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python" />
  </a>
  <img src="https://img.shields.io/badge/Notebooks-Jupyter-orange?style=for-the-badge&logo=jupyter" alt="Jupyter" />
  <img src="https://img.shields.io/badge/Focus-Artificial%20Intelligence%20%26%20Machine%20Learning-success?style=for-the-badge" alt="AI/ML Focus" />
</p>

A structured, project-driven repository documenting my hands-on learning journey in **Artificial Intelligence** and **Machine Learning** — from Python fundamentals to model building, evaluation, and deployment-oriented thinking.

---

## 📌 Overview

This repository is a centralized collection of:

- Topic-wise Jupyter notebooks
- Practical ML experiments on real datasets
- End-to-end pipeline practice (data prep → modeling → evaluation)
- Notes and implementations that track progress over time

It is designed to demonstrate both **conceptual understanding** and **practical execution**.

---

## 🧭 Repository Structure

```text
AI-ML-Learning/
├── Basic Python/                  # Core Python concepts and problem-solving
├── Numpy/                         # Numerical computing with arrays and vectorized ops
├── Pandas/                        # Data cleaning, transformation, analysis
├── MatPlotLib/                    # Data visualization and exploratory plots
├── Machine_Learning_Foundation/   # Intro ML workflows and baseline models
├── Supervised Learning/
│   ├── Linear Regression/         # Regression problems and evaluation
│   ├── Classification/            # Classification algorithms and project work
│   │   └── Project/               # Heart disease risk prediction (Streamlit app)
│   ├── Cross_Validation.ipynb
│   ├── EnsembleLearning.ipynb
│   └── HyperParameterTuning.ipynb
└── Unsupervised Learning/
    ├── Clustering.ipynb
    └── PCA.ipynb
```

---

## 🧠 Learning Coverage

### Foundations
- Python essentials (functions, comprehensions, built-ins)
- NumPy for numerical operations
- Pandas for preprocessing and feature handling
- Data visualization with Matplotlib

### Machine Learning
- Supervised learning: regression and classification
- Model evaluation and comparison
- Cross-validation and hyperparameter tuning
- Ensemble learning basics
- Unsupervised learning: clustering and dimensionality reduction (PCA)

---

## 🔁 End-to-End ML Workflow Practiced

```text
Dataset → EDA → Cleaning → Encoding → Scaling → Feature Engineering
→ Train/Test Split → Model Training → Evaluation
→ Cross Validation → Hyperparameter Tuning → Final Model
```

This workflow is consistently applied across multiple notebooks to reinforce production-style ML habits.

---

## 🌟 Featured Project

### Heart Disease Risk Prediction (Streamlit)
A notebook-to-app implementation that predicts heart disease risk using patient-related input features and trained classification models.

Run locally:

```bash
cd "Supervised Learning/Classification/Project"
pip install streamlit pandas scikit-learn joblib
streamlit run app.py
```

---

## ⚙️ Tech Stack

- **Language:** Python
- **Environment:** Jupyter Notebook
- **Libraries:** NumPy, Pandas, Matplotlib, Scikit-learn, Streamlit, Joblib

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Rohan200511/AI-ML-Learning.git
cd AI-ML-Learning
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install numpy pandas matplotlib scikit-learn jupyter streamlit joblib
```

### 4. Launch Jupyter

```bash
jupyter notebook
```

---

## 🎯 Current Goals

- Strengthen ML fundamentals through repeated implementation
- Improve model selection and evaluation depth
- Expand into deployment-ready mini projects
- Progress toward deep learning, NLP, and GenAI topics

---

## 🤝 Contributions

This is a personal learning repository, but constructive feedback and suggestions are welcome.

If you’d like to contribute:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📌 Note

This repository emphasizes **continuous learning and iterative improvement**. Notebooks may evolve as concepts are refined and better approaches are discovered.

---

<p align="center"><i>Learning in public — one notebook, one experiment, one improvement at a time.</i></p>
