# My AI/ML Journey 🚀

A personal, hands-on learning repository documenting my path into Machine Learning and AI — from Python and data-handling fundamentals through classical ML algorithms, model evaluation, and a first end-to-end deployed project.

## 📁 Repository Structure

```
My-AI-ML-Journey/
├── Basic Python/                  # Core Python: functions, lambdas, comprehensions,
│                                   # dictionaries, tuples, built-in functions
├── Numpy/                         # NumPy fundamentals for numerical computing
├── Pandas/                        # Data manipulation, feature extraction,
│                                   # and a countries-dataset project
├── MatPlotLib/                    # Data visualization: distribution, categorical,
│                                   # matrix & regression plots, IPL dataset project
├── Machine_Learning_Foundation/   # First ML notebooks (heart & insurance datasets)
├── Supervised Learning/
│   ├── Linear Regression/         # Insurance cost & car price prediction
│   ├── Classification/            # Logistic Regression, KNN, Decision Tree, Naive Bayes
│   │   └── Project/               # Heart disease risk prediction (Streamlit app)
│   ├── Cross_Validation.ipynb
│   ├── EnsembleLearning.ipynb
│   └── HyperParameterTuning.ipynb
└── Unsupervised Learning/
    ├── Clustering.ipynb
    └── PCA.ipynb
```

## ✅ Complete ML Pipeline

```
   Dataset
      │
      ▼
     EDA
      │
      ▼
   Cleaning
      │
      ▼
   Encoding
      │
      ▼
    Scaling
      │
      ▼
Feature Engineering
      │
      ▼
 Train/Test Split
      │
      ▼
Train Multiple Models
      │
      ▼
   Evaluate
      │
      ▼
Cross Validation
      │
      ▼
Hyperparameter Tuning
      │
      ▼
  Final Model
      │
      ▼
  Save Model
      │
      ▼
   Deploy 🚀
```

This is the workflow followed across the Machine Learning Foundation and Supervised Learning notebooks in this repo, and the same pipeline used to build the Heart Disease Risk Prediction project below.

## 🧠 What's Inside

**Foundations**
- Python essentials — functions, lambda expressions, list/dict comprehensions, built-ins
- NumPy for array/numerical operations
- Pandas for data cleaning, wrangling, and feature extraction
- Matplotlib/Seaborn-style visualizations, including an IPL dataset exploration

**Machine Learning**
- End-to-end ML pipeline practice: EDA → cleaning → encoding → scaling → feature engineering → train/test split → model training → evaluation → cross-validation → hyperparameter tuning
- **Regression:** insurance cost prediction, car price prediction
- **Classification:** Logistic Regression, KNN, Decision Tree, Naive Bayes
- **Model selection & tuning:** cross-validation, ensemble methods, hyperparameter tuning
- **Unsupervised learning:** clustering and PCA (dimensionality reduction)

**Featured Project — Heart Disease Risk Prediction** 🫶
An interactive Streamlit app (`Supervised Learning/Classification/Project/app.py`) that predicts heart disease risk from patient inputs (age, chest pain type, cholesterol, ECG results, etc.) using a trained and scaled KNN model.

To run it locally:
```bash
cd "Supervised Learning/Classification/Project"
pip install streamlit pandas scikit-learn joblib
streamlit run app.py
```

## 🍴 Fork & Use This Repo

Want to use this as a base for your own AI/ML learning journey? Here's how:

1. **Fork it** — click the **Fork** button at the top-right of this repo's GitHub page to create your own copy under your account.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/<your-username>/My-AI-ML-Journey.git
   cd My-AI-ML-Journey
   ```
3. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. **Install the core libraries**:
   ```bash
   pip install numpy pandas matplotlib scikit-learn jupyter streamlit joblib
   ```
5. **Open the notebooks**:
   ```bash
   jupyter notebook
   ```
6. **Keep your fork updated** with the original repo (optional):
   ```bash
   git remote add upstream https://github.com/Rohan200511/My-AI-ML-Journey.git
   git fetch upstream
   git merge upstream/main
   ```

Feel free to adapt the folder structure, swap in your own datasets, or use this as a template for tracking your own AI/ML progress.

## 🛠️ Tools & Libraries

- Python
- NumPy, Pandas
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook

## 🎯 Goals

- Build a strong foundation in AI/ML fundamentals
- Practice data preprocessing and feature engineering
- Train, evaluate, and compare multiple ML models
- Move from notebooks to a deployed, interactive project
- Progress toward deep learning, NLP, and GenAI

## 🌱 Learning Mindset

This repository favors **progress over perfection** — each notebook reflects hands-on practice and iterative improvement rather than polished, final work.

## 🤝 Connect

If you're also learning AI/ML, feel free to explore, fork, or share suggestions!

---

⭐ If you find this repository useful, consider giving it a star.
