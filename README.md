# Machine Learning Journey

### From Python fundamentals to classical Machine Learning — a structured, hands-on learning path

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Apps-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GitHub-ak1bhasan%2FML__Journey-181717?logo=github)](https://github.com/ak1bhasan/ML_Journey)

---

## Overview

This repository documents a **complete, week-by-week learning journey** in **AI Programming with Python** and **Machine Learning**.

It is designed for learners who want to build a strong foundation — starting from Python basics and data analysis, then progressing through feature engineering, supervised learning, unsupervised learning, and dimensionality reduction — with practice problems, assignments, and exams along the way.

**What you will gain**

- Fluency in Python for data and ML workflows
- Practical skills in NumPy, Pandas, and data visualization
- End-to-end experience with preprocessing and feature engineering
- Hands-on training of classical ML algorithms (from scratch and with scikit-learn)
- Experience building interactive Streamlit apps powered by the Google Gemini API

**Primary technologies:** Python · NumPy · Pandas · Matplotlib · Seaborn · Plotly · scikit-learn · Jupyter Notebook · Google Colab · Streamlit · Google Gemini API · Git / GitHub

---

## Table of Contents

- [Learning Roadmap](#-learning-roadmap)
- [Repository Structure](#-repository-structure)
- [Topics Covered](#-topics-covered)
- [Technologies Used](#-technologies-used)
- [Learning Modules](#-learning-modules)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Skills Developed](#-skills-developed)
- [How to Use](#-how-to-use)
- [Recommended Learning Order](#-recommended-learning-order)
- [Project Highlights](#-project-highlights)
- [Repository Statistics](#-repository-statistics)
- [Future Learning](#-future-learning)
- [Acknowledgements](#-acknowledgements)

---

## Learning Roadmap

Follow the repository folders in this order:

```text
AI Programming with Python
        ↓
Python Basics & Functions
        ↓
File Handling & Exception Handling
        ↓
Object-Oriented Programming (OOP)
        ↓
Streamlit & Gemini API Apps
        ↓
NumPy
        ↓
Pandas
        ↓
Data Visualization (Matplotlib → Seaborn & Plotly)
        ↓
Machine Learning
        ↓
Exploratory Data Analysis (EDA)
        ↓
Train / Test Split & Missing Value Handling
        ↓
Outlier Detection & Handling
        ↓
Encoding
        ↓
Scaling & ColumnTransformer
        ↓
Simple & Multiple Linear Regression
        ↓
Logistic Regression
        ↓
K-Nearest Neighbors (KNN) + GridSearchCV
        ↓
Decision Tree · Random Forest · SVM
        ↓
K-Means · DBSCAN
        ↓
PCA
        ↓
Assignments · Mid Term · Final Exam
```

---

## Repository Structure

```text
📦 ML Journey
 ┣ 📂 AI Programming With Python
 ┃ ┣ 📂 Week 01
 ┃ ┃ ┣ 📂 Module 01 Recap Through the Lens of ML
 ┃ ┃ ┣ 📂 Module 02 Function Through the Lens of ML
 ┃ ┃ ┣ 📂 Module 02.5 Practice Day 01
 ┃ ┃ ┣ 📂 Module 03                    ← File & Exception Handling
 ┃ ┃ ┣ 📂 Module 03.5 Practice Day 02
 ┃ ┃ ┗ 📂 Module 04 Exam
 ┃ ┣ 📂 Week 02
 ┃ ┃ ┣ 📂 Module 05 OOP
 ┃ ┃ ┣ 📂 Module 06 Streamlit & Gemini API
 ┃ ┃ ┣ 📂 Module 6.5 Practice Day
 ┃ ┃ ┣ 📂 Module 07                    ← Note / Quiz Generator app
 ┃ ┃ ┗ 📂 Module 7.5                   ← AI Code Debugger app
 ┃ ┣ 📂 Week 03
 ┃ ┃ ┣ 📂 Module 08 Data Analysis with NumPy 01
 ┃ ┃ ┣ 📂 Module 09 Data Analysis with NumPy 02
 ┃ ┃ ┣ 📂 Module 10 Data Analysis with Pandas 01
 ┃ ┃ ┗ 📂 Module 11 Mid Term Exam
 ┃ ┗ 📂 Week 04
 ┃   ┣ 📂 Module 12 Data Analysis with Pandas Part - 02
 ┃   ┣ 📂 Module 13 Data Visualization
 ┃   ┣ 📂 Module 14 Data Visualization with Seaborn and Plotly
 ┃   ┗ 📂 Module 15 Final Exam
 ┣ 📂 Machine Learning
 ┃ ┣ 📂 Week 01
 ┃ ┃ ┣ 📂 Module 01 Exploratory Data Analysis Part -01
 ┃ ┃ ┣ 📂 Module 02 Exploratory Data Analysis Part - 02
 ┃ ┃ ┣ 📂 Module 03 Starter, Train Test Split and Missing Value Handling
 ┃ ┃ ┗ 📂 ML Assignment 01
 ┃ ┣ 📂 Week 02
 ┃ ┃ ┣ 📂 Module 05 Prerequisites of Outlier Handling
 ┃ ┃ ┣ 📂 Module 06 Outlier Detection and Handling
 ┃ ┃ ┣ 📂 Module 07 Encoding
 ┃ ┃ ┗ 📂 Module 08 Scaling
 ┃ ┣ 📂 Week 03
 ┃ ┃ ┣ 📂 Module 09 AI ML Overview and Starting of Linear Regression
 ┃ ┃ ┣ 📂 Module 10 Simple Linear Regression Implementation and Gradient Descent
 ┃ ┃ ┣ 📂 Module 11 Multiple Linear Regression
 ┃ ┃ ┣ 📂 Module 12 Multiple Linear Regression with Scikit Learn
 ┃ ┃ ┗ 📂 Module 13 ML Assignment 02
 ┃ ┣ 📂 Week 04
 ┃ ┃ ┣ 📂 Module 14 Logistic Regression
 ┃ ┃ ┣ 📂 Module 15 Logistic Regression Using Scikit Learn
 ┃ ┃ ┣ 📂 Module 16 K Nearest Neighbour (KNN)
 ┃ ┃ ┗ 📂 Module 17 ML Mid Term
 ┃ ┣ 📂 Week 05
 ┃ ┃ ┣ 📂 Module 18 Decision Tree
 ┃ ┃ ┣ 📂 Module 19 Random forest classification
 ┃ ┃ ┗ 📂 Module 20 Support Vector Machine
 ┃ ┣ 📂 Week 06
 ┃ ┃ ┣ 📂 Module 21 K Means Clustering
 ┃ ┃ ┣ 📂 Module 22 DBSCAN
 ┃ ┃ ┣ 📂 Module 23 PCA
 ┃ ┃ ┗ 📂 Module 24 ML Final Exam
 ┃ ┗ 📂 Eid Vacation                   ← Optional practice sets
 ┣ 📄 Structure.md                     ← ML pipeline outline
 ┗ 📄 README.md
```

> **Note:** Some modules include duplicate notebooks (e.g. `Phitron_*.ipynb` alongside working copies), practice problem folders, datasets (`.csv`), and slides (`.pdf` / `.pptx`).

---

## Topics Covered

| Category | Topics |
|----------|--------|
| **Python Fundamentals** | Variables, conditionals, loops, lists, functions, arguments, return types |
| **Core Python** | File read/write, exception handling, OOP (classes, single & multiple inheritance) |
| **App Development** | Streamlit UI, media inputs, Gemini API integration, dotenv, gTTS |
| **Numerical Computing** | Ndarrays, dtypes, indexing, manipulation, concatenate, transpose |
| **Data Analysis** | Loading CSV/JSON/Excel/Parquet, DataFrames, null handling, unique values |
| **Visualization** | Line, scatter, histogram (Matplotlib/Pandas); Seaborn & Plotly plots |
| **EDA** | Univariate & multivariate analysis (Titanic and related datasets) |
| **Data Splitting** | Train/test split, stratification concepts (used in later modules) |
| **Missing Values** | Detection and handling strategies |
| **Outliers** | Z-score, IQR, Winsorization |
| **Encoding** | OrdinalEncoder, OneHotEncoder, LabelEncoder |
| **Scaling** | StandardScaler, MinMaxScaler, RobustScaler, ColumnTransformer pipelines |
| **Regression** | Simple & multiple linear regression (from scratch + scikit-learn), gradient descent, SGD |
| **Classification** | Logistic regression (from scratch + scikit-learn), KNN, Decision Tree, Random Forest, SVM |
| **Model Tuning** | GridSearchCV (KNN module) |
| **Evaluation** | Accuracy, confusion matrix, classification report, R², MSE, cross-validation patterns |
| **Unsupervised Learning** | K-Means clustering, DBSCAN |
| **Dimensionality Reduction** | PCA |
| **Assessments** | Practice days, assignments, mid terms, final exams, optional vacation practice |

---

## Technologies Used

| Technology | Where it appears |
|------------|------------------|
| **Python** | Notebooks and Streamlit apps throughout |
| **Jupyter Notebook** | Primary learning format (`.ipynb`) |
| **Google Colab** | Referenced / used in notebook workflow |
| **NumPy** | AI Programming Week 03; ML from-scratch models |
| **Pandas** | AI Programming Weeks 03–04; ML EDA & preprocessing |
| **Matplotlib** | Data visualization & ML plots |
| **Seaborn** | Module 14 (AI Programming) |
| **Plotly** | Module 14 (AI Programming) |
| **scikit-learn** | Preprocessing, models, pipelines, GridSearchCV, PCA, clustering |
| **Streamlit** | Weeks 02 apps (UI + AI tools) |
| **Google Gemini API** (`google-genai`) | Module 07 & 7.5 API integrations |
| **Pillow (PIL)** | Image handling in Streamlit apps |
| **gTTS** | Text-to-speech in Module 07 |
| **python-dotenv** | API key loading for Gemini apps |
| **Git / GitHub** | Version control & hosting ([ak1bhasan/ML_Journey](https://github.com/ak1bhasan/ML_Journey)) |

Root-level dependency file for the full ML track: **Not specified** (module-level `requirements.txt` files exist for Streamlit projects).

---

## Learning Modules

<details open>
<summary><strong>Part 1 — AI Programming With Python</strong></summary>

### Week 01 — Python Foundations

Builds Python fluency with an ML-oriented mindset: recap of basics, functions, file/exception handling, practice days, and a graded exam.

| Focus | Key notebooks / materials |
|-------|---------------------------|
| Concepts | Variables, conditionals, loops, lists, functions, file I/O, exceptions |
| Important notebooks | `Recap of Python basic.ipynb`, `Module_2_Function.ipynb`, `File_Handling_and_Exception_Handling.ipynb` |
| Practice | Module 02.5 & 03.5 practice days |
| Assessment | `AI_Programming_With_Python_Assignment_01_*.ipynb` |
| Skills | Core Python problem-solving for later data/ML work |

### Week 02 — OOP & Generative AI Apps

Introduces object-oriented programming and interactive AI applications with Streamlit and the Gemini API.

| Focus | Key materials |
|-------|---------------|
| Concepts | Classes, objects, inheritance; Streamlit widgets; multimodal Gemini calls |
| Important notebooks / apps | `oop.ipynb`; `STREAMLIT/` demos; Module 07 Note Summary & Quiz Generator; Module 7.5 AI Code Debugger |
| Practice | Module 6.5 Streamlit practice problems |
| Skills | OOP design, API integration, rapid UI prototyping |

> **Live demo (Module 7.5):** [AI Code Debugger](https://aidebug.streamlit.app/)

### Week 03 — NumPy & Pandas (Part 1)

Numerical computing with NumPy and the start of tabular data analysis with Pandas, closed by a mid-term exam.

| Focus | Key notebooks |
|-------|---------------|
| Concepts | Ndarrays, attributes, dtypes, array ops; loading files into DataFrames |
| Important notebooks | `numpy-1.ipynb`, `numpy2.ipynb`, `Pandas Part 01.ipynb` |
| Assessment | `AI_Programming_With_Python_Mid_Term.ipynb` |
| Skills | Array computing and first-pass data wrangling |

### Week 04 — Pandas (Part 2) & Visualization

Deepens Pandas (nulls, uniqueness, cleaning) and covers visualization with Matplotlib, Seaborn, and Plotly, ending in a final exam.

| Focus | Key notebooks |
|-------|---------------|
| Concepts | Null handling, uniqueness; line/scatter/histogram; Seaborn & Plotly |
| Important notebooks | `Pandas 02.ipynb`, `Data Visualization.ipynb`, `Visualization with Seaborn and plotly.ipynb` |
| Assessment | `AI_Programming_with_Python_Final_Exam.ipynb` |
| Skills | Cleaning tables and communicating insights visually |

</details>

<details open>
<summary><strong>Part 2 — Machine Learning</strong></summary>

### Week 01 — EDA & Feature Engineering Starter

Univariate/multivariate EDA on Titanic-style data, then train/test splitting and missing-value handling. Includes **ML Assignment 01**.

| Focus | Key notebooks |
|-------|---------------|
| Concepts | Categorical & numerical univariate analysis; multivariate plots; train/test split; missing values |
| Important notebooks | `EDA_P_01.ipynb`, `EDA_P_02.ipynb`, `FE_1(_Starter,_Train_Test_and_Handling_Missing_Values)_.ipynb` |
| Assessment | `ML_Assignment_01.ipynb` |
| Skills | Dataset profiling and safe train/test workflows |

### Week 02 — Outliers, Encoding & Scaling

Full feature-engineering toolkit: outlier methods, categorical encoding, feature scaling, and ColumnTransformer-based pipelines.

| Focus | Key notebooks |
|-------|---------------|
| Concepts | Z-score, IQR, Winsorization; Ordinal / One-Hot / Label encoding; Standard / MinMax / Robust scaling; ColumnTransformer |
| Important notebooks | `Feature_Engineering_Outlier_Handling_.ipynb`, `Winsorization_Technique.ipynb`, `Encoding(different_section).ipynb`, `Feature_Engineering.ipynb`, `Titanic_Feature_Engineering_via_columntransformer.ipynb`, `Robust_Scaler.ipynb` |
| Skills | Production-style preprocessing before modeling |

### Week 03 — Linear Regression

AI/ML overview, simple linear regression (intuition → from-scratch gradient descent), multiple linear regression, and scikit-learn pipelines / SGD. Includes **ML Assignment 02** (house price regression dataset).

| Focus | Key notebooks |
|-------|---------------|
| Concepts | \(y = wx + b\), cost, gradient descent; multi-feature regression; `LinearRegression`, `Pipeline`, SGD |
| Important notebooks | `Simple_Linear_Regression_first_part.ipynb`, `Simple_Linear_Regression.ipynb`, `Multiple_Linear_Regression.ipynb`, `ML_Pipeline.ipynb` |
| Assessment | `ML_Assignment_02.ipynb` |
| Skills | Regression theory + practical sklearn modeling |

### Week 04 — Classification Essentials

Logistic regression from scratch and with scikit-learn, KNN (including GridSearchCV), plus the **ML Mid Term**.

| Focus | Key notebooks |
|-------|---------------|
| Concepts | Sigmoid, binary classification; Titanic FE completion; KNN; hyperparameter search |
| Important notebooks | `Logistic_Regression_from_Scratch.ipynb`, `Logistic_Regression_with_Scikit_Learn.ipynb`, `KNN.ipynb`, `KNN_with_GridSearchCV.ipynb` |
| Assessment | `Machine_Learning_Mid_Term.ipynb` (`adult_income.csv`) |
| Skills | Classification modeling and tuning |

### Week 05 — Tree Models & SVM

Decision trees, random forests, and support vector classification with scikit-learn (often on Titanic-style pipelines).

| Focus | Key notebooks |
|-------|---------------|
| Concepts | Tree depth effects; ensemble classification; SVC workflow with FE + stratified split |
| Important notebooks | `Decision_Tree.ipynb`, `Random_Forest.ipynb`, `Support_vector_Classifier_with_Scikit_Learn.ipynb` |
| Skills | Non-linear classifiers and ensemble thinking |

### Week 06 — Clustering, PCA & Final Exam

Unsupervised learning (K-Means, DBSCAN), dimensionality reduction with PCA, and the **ML Final Exam** (Breast Cancer Wisconsin Diagnostic Dataset — classification).

| Focus | Key notebooks |
|-------|---------------|
| Concepts | Cluster discovery; density-based clustering; PCA; end-to-end exam project |
| Important notebooks | `K_Means_Clustering_using_Scikit_Learn_.ipynb`, `K_Means_Visualizer.ipynb`, `DBSCAN_using_Scikit_Learn.ipynb`, `PCA.ipynb`, `ML_FINAL.ipynb` |
| Skills | Unsupervised analysis and full-pipeline assessment |

### Eid Vacation — Optional Practice

Extra practice notebooks and datasets (e.g. insurance, telco churn, world happiness) for optional reinforcement.

| Materials | `Eid_ul_Adha_Vacation.ipynb`, `Beginner_Friendly_Practice_Set_(_Optional_)_.ipynb` |

</details>

---

## Machine Learning Workflow

This repository follows (and practices) the pipeline documented in `Structure.md`:

```text
Problem Definition
        ↓
Data Collection
        ↓
Exploratory Data Analysis (EDA)
        ↓
Train / Test Split
        ↓
Feature Engineering
        ↓
Missing Value Handling
        ↓
Outlier Handling (if needed)
        ↓
Encoding
        ↓
Scaling
        ↓
ColumnTransformer / Pipeline
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Hyperparameter Tuning
```

**Model Deployment & Monitoring:** outlined in `Structure.md` as a pipeline step; dedicated ML model deployment modules are **Not specified** in the current folders. Interactive **Streamlit + Gemini** apps are covered under AI Programming (Week 02).

---

## Skills Developed

- ✔ Python programming for AI / ML
- ✔ Object-oriented programming
- ✔ Building Streamlit apps with Gemini API
- ✔ Numerical computing with NumPy
- ✔ Data analysis with Pandas
- ✔ Data visualization (Matplotlib, Seaborn, Plotly)
- ✔ Exploratory data analysis
- ✔ Train/test splitting & missing-value handling
- ✔ Outlier detection & Winsorization
- ✔ Feature encoding & scaling
- ✔ ColumnTransformer / ML pipelines
- ✔ Linear & multiple regression (scratch + sklearn)
- ✔ Gradient descent intuition
- ✔ Logistic regression, KNN, Decision Tree, Random Forest, SVM
- ✔ Hyperparameter tuning with GridSearchCV
- ✔ Model evaluation metrics
- ✔ K-Means & DBSCAN clustering
- ✔ PCA for dimensionality reduction
- ✔ Completing assignments and exam-style projects

---

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/ak1bhasan/ML_Journey.git
cd ML_Journey
```

### 2. Set up a Python environment

Create a virtual environment (recommended), then install packages as needed for the section you are studying.

For Streamlit / Gemini modules, use the local requirements files:

```bash
# Example — Note Summary & Quiz Generator
cd "AI Programming With Python/Week 02/Module 07"
pip install -r requirements.txt

# Example — AI Code Debugger
cd "../Module 7.5"
pip install -r requirements.txt
```

For ML notebooks, install common libraries such as `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, and (where used) `plotly`. A single root `requirements.txt` for the full journey is **Not specified**.

### 3. Configure API keys (Streamlit apps only)

Modules that call Gemini expect a `.env` file with your key (variable name used in code: `GEMINI_API_KEY`). Do not commit secrets.

### 4. Open and run notebooks

- Prefer **Jupyter Notebook / JupyterLab** or **Google Colab**
- Run cells **top to bottom**
- Follow folder order in [Recommended Learning Order](#-recommended-learning-order)
- Practice folders (`Practice Problem`, practice days) reinforce each module before exams

### 5. Run Streamlit apps

```bash
streamlit run app.py
```

---

## Recommended Learning Order

1. **AI Programming With Python → Week 01** (Python basics → functions → files/exceptions → exam)
2. **Week 02** (OOP → Streamlit demos → practice → Gemini apps)
3. **Week 03** (NumPy → Pandas intro → mid term)
4. **Week 04** (Pandas advanced → Matplotlib → Seaborn/Plotly → final exam)
5. **Machine Learning → Week 01** (EDA → split/missing values → Assignment 01)
6. **Week 02** (outliers → encoding → scaling / ColumnTransformer)
7. **Week 03** (linear regression path → Assignment 02)
8. **Week 04** (logistic regression → KNN / GridSearchCV → mid term)
9. **Week 05** (Decision Tree → Random Forest → SVM)
10. **Week 06** (K-Means → DBSCAN → PCA → final exam)
11. **Eid Vacation** (optional extra practice)

---

## Project Highlights

| Project / Notebook | Track | Description |
|--------------------|-------|-------------|
| **Note Summary & Quiz Generator** (`Module 07`) | AI Programming | Streamlit app: upload note images → Gemini summary, quiz, and audio |
| **AI Code Debugger** (`Module 7.5`) | AI Programming | Streamlit app that explains code errors from screenshots ([live demo](https://aidebug.streamlit.app/)) |
| **Streamlit media demos** (`Module 06/STREAMLIT`) | AI Programming | Text, image, audio, and video Streamlit elements |
| **Titanic EDA + Feature Engineering** | Machine Learning | Multi-week pipeline: EDA → missing values → outliers → encoding → scaling → ColumnTransformer |
| **Linear Regression from Scratch** | Machine Learning | Manual parameter tuning and gradient descent |
| **Logistic Regression from Scratch** | Machine Learning | Sigmoid + NumPy gradient descent for binary outcomes |
| **KNN + GridSearchCV** | Machine Learning | Neighbor-based classification with hyperparameter search |
| **ML Pipeline notebook** | Machine Learning | Preprocessing + `LinearRegression` / SGD with scikit-learn |
| **ML Assignment 02** | Machine Learning | House price regression assignment |
| **ML Mid Term** | Machine Learning | Adult income classification-style assessment |
| **ML Final Exam** | Machine Learning | End-to-end classification on Breast Cancer Wisconsin Diagnostic data |
| **Eid Vacation practice** | Machine Learning | Optional advanced / beginner practice sets |

---

## Repository Statistics

| Metric | Count |
|--------|------:|
| Learning tracks | 2 |
| AI Programming weeks | 4 |
| Machine Learning weeks (+ Eid Vacation) | 7 |
| Module-level folders (approx.) | ~44 |
| Total folders (excl. `.git` / venv) | 88 |
| Jupyter notebooks | 110 |
| Python (`.py`) files | 16 |
| CSV datasets | 59 |
| PDF resources | 26 |
| Markdown docs | 3 (`README.md`, `Structure.md`, Module 7.5 `README.md`) |

**Main libraries:** NumPy, Pandas, Matplotlib, Seaborn, Plotly, scikit-learn, Streamlit, Google Gemini API  

**Learning modules:** AI Programming (Weeks 01–04) + Machine Learning (Weeks 01–06) + optional Eid practice  

---

## Future Learning

Topics **not yet covered** as dedicated modules in this repository — natural next steps:

- Deep Learning (neural networks)
- PyTorch / TensorFlow
- Computer Vision
- Natural Language Processing (beyond Gemini API usage)
- Advanced ensemble methods (e.g. boosting libraries — **Not specified** here)
- MLOps & experiment tracking
- Production ML model deployment & monitoring
- Recommendation systems

---

## Acknowledgements

This repository documents a structured learning journey in **AI Programming with Python** and **Machine Learning** — combining weekly modules, practice problems, assignments, exams, and applied projects.

It is intended for students, self-learners, collaborators, and recruiters who want a clear view of progressive skill-building from Python foundations to classical ML.

---

<div align="center">

**Learn → Practice → Build → Evaluate**

Made for continuous growth in Machine Learning

[Repository on GitHub](https://github.com/ak1bhasan/ML_Journey)

</div>
