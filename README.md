# 🧠 Machine Learning Journey

This repository is my record of two [Phitron](https://phitron.io) courses, taken in order: **AI Programming with Python**, then **Machine Learning**. The first course is four weeks of Python, a short stop on object-oriented programming, a few Streamlit apps that call the Gemini API, and the NumPy, Pandas, and plotting I needed before any model. The second course is six weeks of exploratory analysis, preprocessing, regression, classification, clustering, and PCA, with practice sets, two assignments, a midterm, and a final. An optional Eid vacation folder sits beside the ML weeks.

What you will find is the course material as I kept it: instructor notebooks, my re-runs, practice solutions, exam write-ups, small datasets, and the Streamlit projects. A folder being present does not mean every exercise inside it was finished. Where a notebook has saved output, the numbers below are those saved values. I did not retrain anything while writing this README.

The later deep learning work lives in two other repositories, [Deep Learning](https://github.com/ak1bhasan/Deep-Learning) and [Advanced Deep Learning](https://github.com/ak1bhasan/Advanced_Deep_Learning). This one stops at classical machine learning.

---

## Overview

Each course is arranged by week, and each week is split into numbered modules. Inside a module you will usually find some mix of:

| File type | What it is |
|---|---|
| `Phitron_*.ipynb` | The instructor notebook, kept under its original name |
| Unprefixed `*.ipynb` | My working copy. Most of these have execution counts and saved output |
| `Practice Problem/` | A question sheet, a solution notebook, or both |
| `*.pdf`, `*.pptx`, `*.docx` | Course notes, slide decks, and practice sheets. Several of the large PDFs are image exports, so little text can be read out of them |
| `*.csv` and a few other tables | Datasets used by the notebooks. The same Titanic file is copied into many module folders |

The `Phitron_` prefix is the usual signal, and it is not a perfect one. Some lessons exist as only one notebook. A few instructor files still contain output even though their execution counts were cleared. And a notebook that asks a question is not the same thing as a notebook that answers it. I point out those cases in the module notes below.

`Structure.md` is a one-page outline of a machine learning pipeline, including deployment and monitoring. The notebooks practice the earlier steps. They do not deploy or monitor a model.

---

## Table of Contents

- [Learning Roadmap](#learning-roadmap)
- [Repository Structure](#repository-structure)
- [Topics Covered](#topics-covered)
- [Technologies and Tools](#technologies-and-tools)
- [Learning Modules](#learning-modules)
  - [Part 1. AI Programming With Python](#part-1-ai-programming-with-python)
  - [Part 2. Machine Learning](#part-2-machine-learning)
- [Practical Work and Projects](#practical-work-and-projects)
- [Assignments and Exams](#assignments-and-exams)
- [Machine Learning Workflow](#machine-learning-workflow)
- [Skills and Learning Outcomes](#skills-and-learning-outcomes)
- [How to Use](#how-to-use)
- [Where this repository stops](#where-this-repository-stops)
- [Acknowledgements](#acknowledgements)

---

## Learning Roadmap

```text
AI Programming with Python
   Week 01  Python recap, functions, files, exceptions, a practice day on each
   Week 02  Classes and inheritance, Streamlit demos, Gemini apps
   Week 03  NumPy, then the first Pandas week, then the midterm
   Week 04  Cleaning tables, Matplotlib, Seaborn, Plotly, then the final
        │
Machine Learning
   Week 01  Titanic EDA, train/test split, missing values, Assignment 01
   Week 02  Z-score, IQR, winsorization, encoding, scaling, ColumnTransformer
   Week 03  Linear regression from scratch and with scikit-learn, Assignment 02
   Week 04  Logistic regression, KNN, GridSearchCV, the midterm
   Week 05  Decision trees, random forests, SVM
   Week 06  K-Means, DBSCAN, PCA, the final exam
   Eid      Optional practice on Adult, churn, insurance, and happiness
```

---

## Repository Structure

```text
ML Journey/
├── README.md
├── Structure.md
├── AI Programming With Python/
│   ├── Week 01/
│   │   ├── Module 01 Recap Through the Lens of ML/
│   │   ├── Module 02 Function Through the Lens of ML/
│   │   ├── Module 02.5 Practice Day 01/
│   │   ├── Module 03/                          file and exception handling
│   │   ├── Module 03.5 Practice Day 02/
│   │   └── Module 04 Exam/
│   ├── Week 02/
│   │   ├── Module 05 OOP/
│   │   ├── Module 06 Streamlit & Gemini API/STREAMLIT/
│   │   ├── Module 6.5 Practice Day/
│   │   ├── Module 07/                          Note Summary and Quiz Generator
│   │   └── Module 7.5/                         AI Code Debugger
│   ├── Week 03/
│   │   ├── Module 08 Data Analysis with NumPy 01/
│   │   ├── Module 09 Data Analysis with NumPy 02/
│   │   ├── Module 10 Data Analysis with Pandas 01/
│   │   └── Module 11 Mid Term Exam/
│   └── Week 04/
│       ├── Module 12  Data Analysis with Pandas Part  - 02/
│       ├── Module 13  Data Visualization/
│       ├── Module 14 Data Visualization with Seaborn and Plotly/
│       └── Module 15 Final Exam/
└── Machine Learning/
    ├── Week 01/   EDA, split and missing values, ML Assignment 01
    ├── Week 02/   outliers, encoding, scaling
    ├── Week 03/   linear regression, ML Assignment 02
    ├── Week 04/   logistic regression, KNN, ML Mid Term
    ├── Week 05/   decision tree, random forest, SVM
    ├── Week 06/   K-Means, DBSCAN, PCA, ML Final Exam
    └── Eid Vacation/
```

Folder names are kept as they are, including `Module 12  Data Analysis with Pandas Part  - 02` (two spaces, then a spaced hyphen), `Module 13  Data Visualization`, `Module 09  AI ML Overview and Starting of Linear Regression`, `Module 05  Prerequisites of Outlier Handling`, `Module 16 K Nearest Neighbour(KNN)`, and `Module 19 Random forest classification`.

The tree leaves out duplicate notebooks, most CSV copies, and the virtual environment under `Module 07/Project1venv`. That environment is local install noise, not course material. Outside that environment and the Git metadata, the repository currently holds 110 notebooks, 16 Python files, 59 CSV files, 26 PDFs, 5 slide decks, and 2 Word documents.

---

## Topics Covered

| Area | Theory / written work | Implemented in code |
|---|---|---|
| **Python fundamentals** | Variables, conditionals, loops, lists, dictionaries, functions, `*args` / `**kwargs`, generators, `lambda` with `map`, `filter`, and `apply` | Recap and function notebooks, plus two practice days. One recap cell also runs an untrained PyTorch `Sequential` and a KNN loop on Breast Cancer; the comparison table under it is typed in by hand |
| **Files and exceptions** | Reading, writing, `seek`, `try` / `except` / `else` / `finally` | File notebook and Practice Day 02. The later cleaning exercises are written in my copy; only the early cells have saved execution counts |
| **OOP** | Classes, single and multiple inheritance, polymorphism, encapsulation, abstraction | `oop.ipynb`, including a private `__battery` example whose saved run raises `AttributeError` on a direct read, which is the name-mangling point of the exercise |
| **Streamlit and Gemini** | App structure in the Module 7.5 README | Widget demos, a note-summary app, and a code-debugger app. These call a hosted Gemini model. They do not train one |
| **NumPy** | Array attributes, dtypes, creation, slicing, stacking, reductions, linear-algebra helpers | `numpy-1.ipynb` and `numpy2.ipynb`. The bonus notebook also splits a 10-row toy matrix by hand and with `train_test_split` |
| **Pandas** | Loading tables, indexing, sorting, filtering, nulls, duplicates, `groupby`, dates | Pandas notebooks on the included student tables, plus a practice day |
| **Visualization** | Line, scatter, histogram, bar, pie; then Seaborn and Plotly chart types | Matplotlib module and the Seaborn/Plotly module, both with saved figures |
| **EDA** | Univariate and multivariate questions, written observations on Titanic | Count, bar, KDE, and pie plots; a ydata-profiling report saved as HTML |
| **Splitting and missing values** | Why an imputer must be fit on the training fold only (practice write-up) | `train_test_split` with `random_state=42`, usually `test_size=0.2`. Mean, median, mode, and constant imputation, with the statistic taken from `X_train` in the feature-engineering notebook |
| **Outliers** | Z-score versus IQR, and when to cap instead of delete. Week 02 opens with a normal-distribution slide deck | Z-score and IQR on Titanic `Age` and `Fare`, clipping, and 12th/88th-percentile winsorization on `marks_dataset.csv` |
| **Encoding** | Ordinal versus one-hot, including a written reason for ordinal age groups | `OrdinalEncoder`, `OneHotEncoder`, and `LabelEncoder` on Titanic and on the encoding practice sets |
| **Scaling and ColumnTransformer** | Why distance-based models care about scale, and why trees do not (practice answer) | `StandardScaler`, `MinMaxScaler`, `RobustScaler`. Week 02 uses `ColumnTransformer` for preprocessing. From Week 03 the same idea is often wrapped in a `Pipeline` with the model |
| **Linear regression** | Prediction function, squared-error cost, gradient updates, SGD | A five-point from-scratch fit, multiple regression from scratch, then `LinearRegression` and `SGDRegressor` inside pipelines |
| **Logistic regression** | Sigmoid, log loss, class weight, threshold | A from-scratch gradient loop whose saved cost rises, then scikit-learn on Titanic and on a downloaded telco churn table |
| **KNN, trees, SVM** | Distance, tree depth, ensembles, kernels. The long Week 05 and Week 06 slide PDFs are image notes | `KNeighborsClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, `SVC`, several of them inside `GridSearchCV` |
| **Clustering and PCA** | Elbow method, density clustering, variance explained. Slide PDFs for these three topics have almost no extractable text | `KMeans` and `DBSCAN` on generated sets, PCA compared with logistic regression on Breast Cancer |
| **Evaluation** | What accuracy, precision, and recall answer, including a note that accuracy can mislead. Question point values are printed on the exams. Awarded marks are not stored | Accuracy, precision, recall, classification report, confusion matrix, R², MSE, RMSE, MAE, ROC AUC on the churn notebook, and 5-fold search scores where `GridSearchCV` or `cross_val_score` is actually called |
| **Deployment and monitoring** | Named as the last step in `Structure.md` | No model-serving or monitoring code in this repository. The Streamlit apps are interfaces to Gemini, not deployed classical models |

---

## Technologies and Tools

| Category | What the files actually use |
|---|---|
| Language | Python. Notebooks were run in a mix of Google Colab and a local Windows Jupyter kernel. The ydata-profiling cell in EDA Part 2 records a Colab path under Python 3.12. A Matplotlib warning in the visualization notebook records a local Windows path. There is no root `requirements.txt` and no pinned notebook environment |
| Tables and arrays | NumPy, pandas. Pandas is used to read CSV, JSON, Excel (`.xlsx`), and Parquet in Week 03 of the Python course |
| Classical ML | scikit-learn: splitters, imputers, encoders, scalers, `ColumnTransformer`, `Pipeline`, `LinearRegression`, `SGDRegressor`, `LogisticRegression`, `KNeighborsClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, `SVC`, `KMeans`, `DBSCAN`, `PCA`, `GridSearchCV`, `RandomizedSearchCV`, `cross_val_score`, and the usual metrics |
| Visualization | Matplotlib, Seaborn, Plotly. Seaborn sample datasets (`tips`, `penguins`) are loaded in a few notebooks. Saved figures include notebook image outputs, `newplot.png`, and `digital_marketing_data.html` |
| Profiling | `ydata-profiling` is installed from a notebook cell and writes `my_report.html`. It is not part of either `requirements.txt` |
| Apps | Streamlit. `google-genai` (`from google import genai`, pinned at 1.73.1) is the Gemini SDK in every API script I checked. Pillow reads uploads. `gTTS` is used only by the note-summary app. `python-dotenv` loads `GEMINI_API_KEY` |
| Other | `ucimlrepo` in the Eid notebook (`fetch_ucirepo`). One early recap notebook imports PyTorch for a single untrained forward pass. PyTorch is not used again in this repository |
| App pins | [`Module 07/requirements.txt`](AI%20Programming%20With%20Python/Week%2002/Module%2007/requirements.txt) and [`Module 7.5/requirements.txt`](AI%20Programming%20With%20Python/Week%2002/Module%207.5/requirements.txt) pin Streamlit 1.56.0, `google-genai` 1.73.1, and their dependencies. Only the Module 07 file includes `gTTS==2.5.4` |

---

## Learning Modules

### Part 1. AI Programming With Python

#### Week 01, Python foundations

The week rebuilds ordinary Python with a few machine-learning shapes mixed in, then asks for the same ideas on paper.

[Recap of Python basic.ipynb](AI%20Programming%20With%20Python/Week%2001/Module%2001%20Recap%20Through%20the%20Lens%20of%20ML/Recap%20of%20Python%20basic.ipynb) walks variables, conditions, loops, lists, and dictionaries. One cell feeds four made-up numbers through an untrained `nn.Sequential` (`Linear → ReLU → Linear → Sigmoid`) and prints a probability. The weights are never fit, so that print is a random forward pass. The same notebook then loads scikit-learn's Breast Cancer data, splits 70/30 with `random_state=42`, and scores `KNeighborsClassifier` for `k` from 1 to 50 **on the test set**. The saved run peaks at `k = 10` with test accuracy 0.9825. Choosing `k` on the test fold means that number is not an honest estimate of a new test set. The small model-comparison frame under it (`KNN` 0.942, `RandomForest` 0.965, `LogisticReg` 0.910) is a dictionary written into the cell, not a training loop. [Recap_of_python_basic_.ipynb](AI%20Programming%20With%20Python/Week%2001/Module%2001%20Recap%20Through%20the%20Lens%20of%20ML/Recap_of_python_basic_.ipynb) is a close second copy with outputs and cleared execution counts.

[Module_2_Function.ipynb](AI%20Programming%20With%20Python/Week%2001/Module%2002%20Function%20Through%20the%20Lens%20of%20ML/Module_2_Function.ipynb) is the function week: defaults, `*args`, `**kwargs`, return values, iterators, a chunk generator named like a data loader, and `lambda` with `Series.apply` and `Series.map`. The saved run includes the errors you get from a missing argument and from indexing a set, which the notebook is demonstrating. [Phitron_Module_2_Function.ipynb](AI%20Programming%20With%20Python/Week%2001/Module%2002%20Function%20Through%20the%20Lens%20of%20ML/Phitron_Module_2_Function.ipynb) is the instructor copy.

[Module 2.5 Practice Day.ipynb](AI%20Programming%20With%20Python/Week%2001/Module%2002.5%20Practice%20Day%2001/Module%202.5%20Practice%20Day.ipynb) answers five short problems (f-strings, a batch generator, `map`, an optional exponent, `filter`). The question PDF is beside it. [Module_03_5_Practice_Day_02.ipynb](AI%20Programming%20With%20Python/Week%2001/Module%2003.5%20Practice%20Day%2002/Module_03_5_Practice_Day_02.ipynb) implements create, numbered read, append, `seek`, and a `safe_read` that catches `FileNotFoundError`. The saved output shows the missing-file branch and the success branch.

[File_Handling_and_Exception_Handling.ipynb](AI%20Programming%20With%20Python/Week%2001/Module%2003/File_Handling_and_Exception_Handling.ipynb) reads and writes text, counts lines, words, and characters with `map` and `reduce`, and uses `w+` with `seek` and `truncate`. The exception section covers `ZeroDivisionError`, a bare `Exception`, and `else` / `finally`. My copy also contains three extra cleaning exercises (emails, names, and an index check). Only 3 of 24 code cells have execution counts, so the later exercises are written rather than saved as a full run. The instructor notebook stops earlier and does not include those three exercises.

Module 04 is the week exam. The notebook there is an image sheet: five code cells, none executed. I did not recover question text from the images. Treat that folder as the question packet, not as a scored solution.

#### Week 02, OOP and Gemini apps

[oop.ipynb](AI%20Programming%20With%20Python/Week%2002/Module%2005%20OOP/oop.ipynb) builds a phone class, then smartphone and cooling classes, multiple inheritance, method overriding, private attributes, and an abstract telephone. The practice cells add `GamingPhone.start_game` and a `MobilePhone` whose battery is stored as `__battery`. [Phitron_oop.ipynb](AI%20Programming%20With%20Python/Week%2002/Module%2005%20OOP/Phitron_oop.ipynb) is the instructor version of the lesson, without those two practice classes.

Module 06 is a set of small Streamlit scripts, not one app. From `STREAMLIT/`:

- [`txt_input.py`](AI%20Programming%20With%20Python/Week%2002/Module%2006%20Streamlit%20%26%20Gemini%20API/STREAMLIT/txt_input.py) writes titles, markdown, and two numbers.
- [`input_element.py`](AI%20Programming%20With%20Python/Week%2002/Module%2006%20Streamlit%20%26%20Gemini%20API/STREAMLIT/input_element.py) uses text, a number, a button, and a select box.
- [`image_element.py`](AI%20Programming%20With%20Python/Week%2002/Module%2006%20Streamlit%20%26%20Gemini%20API/STREAMLIT/image_element.py) shows a local image, a URL, and an uploader capped in a warning at two files.
- [`audio.py`](AI%20Programming%20With%20Python/Week%2002/Module%2006%20Streamlit%20%26%20Gemini%20API/STREAMLIT/audio.py) plays `audio/welcome.mp3` and an upload.
- [`video.py`](AI%20Programming%20With%20Python/Week%2002/Module%2006%20Streamlit%20%26%20Gemini%20API/STREAMLIT/video.py) plays an uploaded mp4 or mkv after a button press. `video/nature.mp4` is included.
- [`app.py`](AI%20Programming%20With%20Python/Week%2002/Module%2006%20Streamlit%20%26%20Gemini%20API/STREAMLIT/app.py) is the only script in this folder that calls Gemini. On startup it asks `gemini-3-flash-preview` for a 100-word description and renders `response.text`. There is no button and no training loop.

Module 6.5 is three separate scripts. [`Problem 01.py`](AI%20Programming%20With%20Python/Week%2002/Module%206.5%20Practice%20Day/Problem%2001.py) is a four-operation calculator with a divide-by-zero message. [`Problem 02.py`](AI%20Programming%20With%20Python/Week%2002/Module%206.5%20Practice%20Day/Problem%2002.py) sends a text prompt to `gemini-3-flash-preview`. [`Problem 03.py`](AI%20Programming%20With%20Python/Week%2002/Module%206.5%20Practice%20Day/Problem%2003.py) asks the same model to rewrite a sentence. All three use `google-genai` except the calculator, which is plain Streamlit.

**Note Summary and Quiz Generator** ([`Module 07/app.py`](AI%20Programming%20With%20Python/Week%2002/Module%2007/app.py)) is the first app with a real flow. The sidebar accepts up to three note images (jpeg, jpg, png) and a quiz difficulty of Easy, Medium, or Hard. [`api_calling.py`](AI%20Programming%20With%20Python/Week%2002/Module%2007/api_calling.py) sends the images plus a prompt to `gemini-3-flash-preview` through `client.models.generate_content`. One call writes a short summary and key points. A second call writes three multiple-choice questions, two short questions, and an answer key, and the prompt tells the model to stay inside the image. `gTTS` then speaks the summary after the markdown characters are stripped. [`working_images.py`](AI%20Programming%20With%20Python/Week%2002/Module%2007/working_images.py) and [`working_with_audio.py`](AI%20Programming%20With%20Python/Week%2002/Module%2007/working_with_audio.py) are the earlier one-file experiments this app was built from. The model is a hosted API. Nothing in the folder fine-tunes it, and the UI does not show retries, auth beyond the API key, or tests.

**AI Code Debugger** ([`Module 7.5/app.py`](AI%20Programming%20With%20Python/Week%2002/Module%207.5/app.py), [project README](AI%20Programming%20With%20Python/Week%2002/Module%207.5/README.md)) takes up to three screenshots of a code error. The select box offers "Hints" or "Solution with code". For either choice the app first calls [`debug_generator`](AI%20Programming%20With%20Python/Week%2002/Module%207.5/api_calling.py) in an internal `"issue"` mode that is told not to reveal a fix, then calls it again in the selected mode. Hints are constrained to two to four bullets and no corrected code. Solution mode asks for steps, corrected code, and a short explanation. The same `gemini-3-flash-preview` client is used. The project README links a demo at <https://aidebug.streamlit.app/>. A request to that URL returned HTTP 303, so the host answered with a redirect. I did not open the app and click through a screenshot.

#### Week 03, NumPy, Pandas, and the midterm

[numpy-1.ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2008%20Data%20Analysis%20with%20NumPy%2001/numpy-1.ipynb) is my long NumPy pass: `ndarray` attributes, dtypes, `zeros` / `ones` / `full`, random arrays, `arange`, reshape, slicing, boolean masks, and `nditer`. Two short exercises convert Celsius to Fahrenheit and lap times to minutes. The instructor notebook is [Phitron_numpy_1.ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2008%20Data%20Analysis%20with%20NumPy%2001/Phitron_numpy_1.ipynb). [Data Analysis with NumPy(Bonus).ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2008%20Data%20Analysis%20with%20NumPy%2001/Data%20Analysis%20with%20NumPy%28Bonus%29.ipynb) builds a 10-row study-hours matrix, shuffles it, and splits 80/20. The hand-written slice refers to `Y` after the target was named `y`, so that cell does not stand on its own. The `train_test_split` cell underneath is the one that matches the library call.

[numpy2.ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2009%20Data%20Analysis%20with%20NumPy%2002/numpy2.ipynb) continues with concatenate, transpose, arithmetic, logic, sort, search, statistics, and `np.linalg` (dot, trace, determinant, rank), using the tiny [`student_score.csv`](AI%20Programming%20With%20Python/Week%2003/Module%2009%20Data%20Analysis%20with%20NumPy%2002/student_score.csv). A saved `ValueError` shows a bad concatenate. Of 57 code cells, 23 have execution counts, so the closing practice block is only partly run. [Phitron_numpy2.ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2009%20Data%20Analysis%20with%20NumPy%2002/Phitron_numpy2.ipynb) is the instructor copy and includes a correlation example on study hours and exam scores.

[Pandas Part 01.ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2010%20Data%20Analysis%20with%20Pandas%2001/Pandas%20Part%2001.ipynb) loads the included `student_data.csv`, `phitron_student_marks.xlsx`, `students.parquet`, and `data.json`, then does `loc` / `iloc`, drops, in-place edits, sorting, and filters such as "completed and data-structures marks at least 90". [Practice Day.ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2010%20Data%20Analysis%20with%20Pandas%2001/Practice%20Day.ipynb) answers seven small frame exercises (shape, `describe`, `loc` / `iloc`, drop, sort, filter) on frames built in the notebook. [Phitron_pandas.ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2010%20Data%20Analysis%20with%20Pandas%2001/Phitron_pandas.ipynb) is the instructor notebook.

The midterm, [AI_Programming_With_Python_Mid_Term.ipynb](AI%20Programming%20With%20Python/Week%2003/Module%2011%20Mid%20Term%20Exam/AI_Programming_With_Python_Mid_Term.ipynb), is a NumPy and Pandas exam on an employee table. The questions ask for array metadata, salary and age summaries, a 25-to-40 age filter with salary above 50,000, an age adjustment that must not overwrite the original array, an 8% raise for tech roles, then Pandas `head` / `info` / `describe`, an HR filter, a sort, and a raise split between developer roles and everyone else. Eleven of nineteen code cells have execution counts. The notebook reads `staff_data.csv`, and that file is not in the repository, so a fresh run stops until the table is recreated. I am not treating the partial output as a finished paper, and no awarded mark is stored.

#### Week 04, cleaning, plots, and the final

[Pandas 02.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2012%20%20Data%20Analysis%20with%20Pandas%20Part%20%20-%2002/Pandas%2002.ipynb) goes further on the student tables: `nunique`, null checks, `dropna` and `fillna` (including a mean fill and a fill mapped from the instructor's mean), summary statistics, `apply`, datetime deltas, and `groupby`. One saved cell raises `AttributeError` because `DataFrame.unique` is not a method. `unique` belongs on a Series. [Phitron_Pandas_2.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2012%20%20Data%20Analysis%20with%20Pandas%20Part%20%20-%2002/Phitron_Pandas_2.ipynb) is the instructor notebook and also shows duplicate handling. `student_completed_data.csv` and `new_data.xls` live in this folder.

[Data Visualization.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2013%20%20Data%20Visualization/Data%20Visualization.ipynb) draws line, scatter, histogram, bar, and pie charts from `enrollment_data.csv`, `student_IQdata.csv`, and `student_data.csv`. Eighteen figures are saved in the notebook. [Practice Problem.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2013%20%20Data%20Visualization/Practice%20Problem.ipynb) adds a 10% discount column, drops duplicate employees, fills `Age` with the mean, drops rows with missing `Salary`, summarizes three mark columns, and plots `Practice.csv` plus the IQ table. A Google Drive link in the prompt is how one of those tables was originally shared. The files used by the saved run are already in the folder.

[Visualization with Seaborn and plotly.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2014%20Data%20Visualization%20with%20Seaborn%20and%20Plotly/Visualization%20with%20Seaborn%20and%20plotly.ipynb) is the long chart notebook: Seaborn line, scatter, facet, histogram, KDE, count, bar, `regplot`, `lmplot`, pair, and joint plots, then Plotly scatter, line, and histogram. It reads `sns_data.csv`, `student_dataset_complete.csv`, `enrollment_data.csv`, and Seaborn's `tips`. Forty-two figures are saved. One cell fails because `regplot` was called with `hue`, which that function does not take. The instructor notebook is [Phitron_Visualization_with_Seaborn_and_plotly.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2014%20Data%20Visualization%20with%20Seaborn%20and%20Plotly/Phitron_Visualization_with_Seaborn_and_plotly.ipynb). The practice notebook in `Practice Problem/` plots `sales.csv` and `students.csv` (line, scatter colored by gender, facet by subject, histogram with KDE, count, regression, pairplot) and was executed. `Practice Question.pdf` is the sheet. `digital_marketing_data.html` and `newplot.png` are exported Plotly figures.

The final exam is a NumPy, Pandas, and plotting paper on `school_data.csv` (score, attendance, age, department, grade). [AI_Programming_With_Python_Final_Exam_Question.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2015%20Final%20Exam/AI_Programming_With_Python_Final_Exam_Question.ipynb) is the blank question file. [AI_Programming_with_Python_Final_Exam.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2015%20Final%20Exam/AI_Programming_with_Python_Final_Exam.ipynb) and [All Solution.ipynb](AI%20Programming%20With%20Python/Week%2004/Module%2015%20Final%20Exam/All%20Solution.ipynb) are filled runs. Both print a maximum score of 99, a minimum of 41 (the minimum print is labeled "Maximum Score", which is a label bug), and an average score of 67.3, then filter, sort, and draw a score-by-grade box plot and an attendance-versus-score scatter. Eleven of twelve code cells ran. `school_data.csv` is not in the repository, so those outputs are from a run where the file was on the Colab path. The question sheet says each of the early questions is worth 10 marks. No awarded grade is stored. The two solution notebooks are almost the same paper; the saved score dtype differs (`int64` in one, `int32` in the other), so they are two runs rather than one duplicated file.

### Part 2. Machine Learning

#### Week 01, EDA and missing values

The ML course starts on the Titanic table and stays there for most of the feature-engineering weeks. The file used almost everywhere is `titanic_data_updated.csv` (891 passengers, the usual columns, target `Survived`). `Titanic-Dataset.csv` in Module 01 is a second copy of the same columns.

[EDA_P_01.ipynb](Machine%20Learning/Week%2001/Module%2001%20Exploratory%20Data%20Analysis%20Part%20-01/EDA_P_01.ipynb) does feature screening, a statistical profile, and univariate plots: a count plot and percentage split of `Survived`, a pie chart, and numeric views of `Age` and `Fare`. [Phitron_EDA_P_01.ipynb](Machine%20Learning/Week%2001/Module%2001%20Exploratory%20Data%20Analysis%20Part%20-01/Phitron_EDA_P_01.ipynb) is the instructor notebook. The practice notebook loads Seaborn's `penguins`, drops rows with missing `sex`, and answers the screening questions in text as well as code. The question PDF is next to it. The practice file name contains a double space: `Practice_ Exploratory Data  Analysis Part - 01.ipynb`.

[EDA_P_02.ipynb](Machine%20Learning/Week%2001/Module%2002%20Exploratory%20Data%20Analysis%20Part%20-%2002/EDA_P_02.ipynb) is the multivariate week. Survival is split by sex and by passenger class (`value_counts(normalize=True)`), age is compared with bar and KDE plots, and fare gets a KDE by survival. The notebook then installs `ydata-profiling` and writes [my_report.html](Machine%20Learning/Week%2001/Module%2002%20Exploratory%20Data%20Analysis%20Part%20-%2002/my_report.html). That install cell was run on Colab. [Practice_Problem_on_Multivariate.ipynb](Machine%20Learning/Week%2001/Module%2002%20Exploratory%20Data%20Analysis%20Part%20-%2002/Practice%20Problem/Practice_Problem_on_Multivariate.ipynb) answers the written questions (count plot versus bar plot, how to read a scatter, what a profiling report collects) and fills the code blanks on Seaborn's Titanic sample and the small student CSV. [multivariate_practice_sheet.ipynb](Machine%20Learning/Week%2001/Module%2002%20Exploratory%20Data%20Analysis%20Part%20-%2002/Practice%20Problem/multivariate_practice_sheet.ipynb) is the same sheet with the blanks still empty. `Report.html` in the practice folder is another profiling export.

[FE_1 notebook](Machine%20Learning/Week%2001/Module%2003%20Starter%2C%20Train%20Test%20Split%20and%20Missing%20Value%20Handling/FE_1%28_Starter%2C_Train_Test_and_Handling_Missing_Values%29_.ipynb) separates `Survived` as `y`, splits 80/20 with `random_state=42`, and imputes age. The mean and the median are computed on `X_train['Age']` and then used to fill both the training and test columns. `SimpleImputer` is fit for a mean age, a most-frequent `Embarked`, and a constant `'Missing'` cabin with `add_indicator=True`. The instructor twin is the `Phitron_FE_1...` notebook. The practice notebook on `data.csv` (1,000 rows, a mix of numeric and categorical columns plus `Target`) writes out why `fit_transform` on the full frame before the split leaks test information into the medians, then fits the diagnosis imputer on `X_train` only. The question text is also in `Practice Problem.docx`.

[ML Assignment 01](Machine%20Learning/Week%2001/ML%20Assignment%2001/ML_Assignment_01.ipynb) is the same Titanic workflow as a graded paper: shape and samples, missing values and duplicates, a statistical profile, univariate plots of `Survived` and `Age`, multivariate plots by sex, the 80/20 split, and the three imputers. All 41 code cells ran. The saved shapes are 712 training rows and 179 test rows. The written notes say `Age`, `Cabin`, and `Embarked` are incomplete, and that `Fare` is right-skewed. Questions are marked out of 10 each. No awarded score is stored. This assignment stops at preprocessing. It does not fit a classifier.

#### Week 02, outliers, encoding, and scaling

Module 05 is preparation rather than a model. [Module Slides.pptx](Machine%20Learning/Week%2002/Module%2005%20%20Prerequisites%20of%20Outlier%20Handling/Module%20Slides.pptx) works a z-score by hand (a 1200 on a test with mean 1000 and standard deviation 100 is `z = 2`) and defines the IQR as Q3 minus Q1. The `Practice Problem` folder under this module is empty.

[Feature_Engineering_Outlier_Handling_.ipynb](Machine%20Learning/Week%2002/Module%2006%20Outlier%20Detection%20and%20Handling/Feature_Engineering_Outlier_Handling_.ipynb) continues the Titanic split and then flags `Age` and `Fare` on the training frame. A point is a z-score outlier when the absolute z-score exceeds 3. The IQR fences are Q1 − 1.5 IQR and Q3 + 1.5 IQR, with the fare floor held at 0. Fare is then clipped to those fences. Rows with an age z-score above 3 are filtered out of `X_train` in pandas. That filter is not inside a transformer, so anyone reusing the cell has to drop the matching `y_train` rows by the same mask. [Winsorization_Technique.ipynb](Machine%20Learning/Week%2002/Module%2006%20Outlier%20Detection%20and%20Handling/Winsorization_Technique.ipynb) clips `maths_marks` in `marks_dataset.csv` (100 students) to the 12th and 88th percentiles (`x = 12`, then `x / 100`). The practice notebook solves the same ideas on small hand-typed lists and plots a KDE. One cell raises `TypeError` on a float. The slide deck `Outlier Detection & Handling.pptx` is in the module folder.

[Encoding notebook](Machine%20Learning/Week%2002/Module%2007%20Encoding/Encoding%28different_section%29.ipynb) keeps the outlier steps and adds encoders. `Pclass` is an `OrdinalEncoder` with the order third, second, first. Sex, embarked, and deck use `OneHotEncoder(sparse_output=False)` with pandas output. `LabelEncoder` appears as well. The practice notebook is large (150 executed code cells) and moves past Titanic: Pima `diabetes.csv` (zeros in glucose, blood pressure, and BMI set to missing, then a median imputer, then an ordinal `Age_Group`), `heart.csv` one-hot on `cp` and `thal` (the saved shapes go from 13 columns to 21), `tips.csv` with one-hot and an ordinal tip band, `CarPrice_Assignment.csv`, a second heart file, and the IBM HR attrition table. `hotel_bookings.csv` is in the folder (about 119,000 rows) and is not what those modeling cells load.

[Feature_Engineering.ipynb](Machine%20Learning/Week%2002/Module%2008%20Scaling/Feature_Engineering.ipynb) adds `StandardScaler` and `MinMaxScaler` on top of the same Titanic pipeline. [Robust_Scaler.ipynb](Machine%20Learning/Week%2002/Module%2008%20Scaling/Robust_Scaler.ipynb) fits `RobustScaler` on the marks file. [Titanic_Feature_Engineering_via_columntransformer.ipynb](Machine%20Learning/Week%2002/Module%2008%20Scaling/Titanic_Feature_Engineering_via_columntransformer.ipynb) is the cleaner version of the same ideas: one `ColumnTransformer` imputes age, embarked, and cabin, and a second one ordinal-encodes class, one-hot encodes embarked, sex, and deck, standard-scales age, and min-max scales fare and family size. The z-score row filter and the fare clip stay outside those transformers. There is no estimator in the pipeline yet. The practice notebook loads California housing, diabetes, Breast Cancer, and wine from scikit-learn, fits `StandardScaler` on the training fold, and compares how min-max, standard, and robust scaling treat a column with outliers. The written answer says KNN moves when scales differ and a tree does not, because a tree splits on a threshold.

#### Week 03, linear regression

Module 09 is the orientation week. The folder holds slide decks on the start of AI, types of machine learning, and the ML pipeline, a PDF of the Dartmouth summer-project paper, and a short docx of suggested podcasts and documentaries. [Simple_Linear_Regression_first_part.ipynb](Machine%20Learning/Week%2003/Module%2009%20%20AI%20ML%20Overview%20and%20Starting%20of%20Linear%20Regression/Simple_Linear_Regression_first_part.ipynb) sets up a tiny line, plots it, and tries a few slopes by hand. The practice notebook is five executed cells of the same idea. No test metric is stored, because nothing is trained yet.

[Simple_Linear_Regression.ipynb](Machine%20Learning/Week%2003/Module%2010%20Simple%20Linear%20Regression%20Implementation%20and%20Gradient%20Descent/Simple_Linear_Regression.ipynb) is the from-scratch line. The target in the notebook is a five-value salary list `[15, 35, 45, 65, 75]`. The update is the usual batch step, `w := w - alpha * dj/dw`, with `alpha = 0.01`. The saved log starts at cost 790 and is about 0 by iteration 2500, with the slope near 10 and the intercept near 5. That is a fit to this toy line, on the same points that defined the loss. The conceptual session, [ML_Week_03_CS_01.ipynb](Machine%20Learning/Week%2003/Module%2010%20Simple%20Linear%20Regression%20Implementation%20and%20Gradient%20Descent/Conceptual%20Session/ML_Week_03_CS_01.ipynb), switches to [`iq_cgpa_org.csv`](Machine%20Learning/Week%2003/Module%2010%20Simple%20Linear%20Regression%20Implementation%20and%20Gradient%20Descent/Conceptual%20Session/iq_cgpa_org.csv) (1,000 rows, columns `IQ` and `CGPA`), splits 80/20 with `random_state=42`, and fits `LinearRegression`. The saved **test** scores are MAE 0.218, MSE 0.075, RMSE 0.273, and R² 0.950. The instructor copy of that session hard-codes a `/content/` path. The practice notebook repeats gradient descent on `Salary_Data.csv`, `Housing.csv`, `StudentsPerformance.csv`, and `insurance.csv`. `Important Links.pdf` did not yield readable text.

[Multiple_Linear_Regression.ipynb](Machine%20Learning/Week%2003/Module%2011%20Multiple%20Linear%20Regression/Multiple_Linear_Regression.ipynb) extends the same gradient to a vector of weights. The saved cost starts at 188 and reaches about 0 by iteration 450,000, with `alpha = 0.01` on a small constructed set. The notebook then places `LinearRegression` next to `SGDRegressor(penalty=None, max_iter=450001, learning_rate='constant')`. The practice notebook uses `Salary Data.csv` (age, gender, education, job title, years of experience, salary).

[ML_Pipeline.ipynb](Machine%20Learning/Week%2003/Module%2012%20Multiple%20Linear%20Regression%20with%20Scikit%20Learn/ML_Pipeline.ipynb) is where preprocessing and the model finally share one object. The table is `bangladesh_student_performance_updated.csv` (2,018 students). `hsc_result` is the target and `date` is dropped. Numeric and nominal columns each get an imputer inside a `Pipeline`, those pipelines sit in a `ColumnTransformer`, and the transformer is the first step of a second `Pipeline` whose last step is `LinearRegression` or `SGDRegressor`. Because the scaler lives inside the pipeline, `fit` on `X_train` is what learns the preprocessing. The saved **test** scores are:

| Model | Test MSE | Test R² | Test RMSE | Test MAE |
|---|---:|---:|---:|---:|
| `LinearRegression` | 0.0203 | 0.9459 | 0.1425 | 0.1114 |
| `SGDRegressor` | 0.0207 | 0.9448 | 0.1438 | 0.1136 |

R² here is the fraction of test-set variance of `hsc_result` captured by the predictions. RMSE and MAE are in the same units as that column. The conceptual session repeats the exercise on `bangladesh_student_performance.csv` and also calls `cross_val_score`. The saved 5-fold R² values are 0.948, 0.953, 0.939, 0.943, and 0.942, mean 0.945. In that same session the linear model records train R² 0.947 and test R² 0.946. The practice notebook does the same pipeline on the included housing file (`price` as the target, 545 rows). Saved test R² is 0.546 for linear regression and 0.545 for SGD, with test RMSE about 1.51 million in the price units of the file. The notebook's own comparison picks linear regression as the lower test RMSE. A test R² near 0.55 is a moderate fit, and it is a different problem from the student-result R² above.

[ML Assignment 02](Machine%20Learning/Week%2003/Module%2013%20ML%20Assignment%2002/ML_Assignment_02.ipynb) uses [`house_price_regression_dataset.csv`](Machine%20Learning/Week%2003/Module%2013%20ML%20Assignment%2002/house_price_regression_dataset.csv): 1,000 rows, features for size, bedrooms, bathrooms, year, lot, garage, and neighborhood quality, target `House_Price`. The paper asks for EDA, a from-scratch gradient update in NumPy, a leakage-safe split, pipelines, and a comparison of `SGDRegressor` and `LinearRegression`. All 26 code cells ran. The from-scratch log on a scaled line falls from cost 0.490 to about 0.0088. The pipeline **test** R² is 0.9981 for SGD (RMSE 10,957) and 0.9984 for linear regression (RMSE 10,250). Train R² is 0.9985 and 0.9986. `cross_val_score` is imported and I did not find a call, so there is no cross-validated number in the saved output. A test R² this close to 1, and this close to the training R², means `House_Price` in this file is nearly a linear function of the columns. It is a result on this assignment file, not a general claim about predicting house prices.

#### Week 04, logistic regression, KNN, and the midterm

[Logistic_Regression_from_Scratch.ipynb](Machine%20Learning/Week%2004/Module%2014%20Logistic%20Regression/Logistic_Regression_from_Scratch.ipynb) implements sigmoid, log loss, and gradient descent for two weights. The saved run does not converge. Cost starts at 0.73 and is still climbing past 2 after tens of thousands of steps, so those weights are not a finished classifier. The practice notebook is a question sheet (sigmoid, cost, and a short discussion of why accuracy can mislead). It has no execution counts. A printed line in that file says accuracy 100% and log loss 1.204. I am treating that as material shipped with the questions, not as a model I trained.

[Logistic_Regression_with_Scikit_Learn.ipynb](Machine%20Learning/Week%2004/Module%2015%20Logistic%20Regression%20Using%20Scikit%20Learn/Logistic_Regression_with_Scikit_Learn.ipynb) returns to Titanic. The split is 80/20, `random_state=42`, and `stratify=y`. Imputers, encoders, and scalers sit in pipelines inside a `ColumnTransformer`, and the estimator is `LogisticRegression(class_weight='balanced', max_iter=1000)`. The saved **test** scores are accuracy 0.76, precision 0.67, and recall 0.75. With the default binary settings those precision and recall values are for the positive class, `Survived = 1`. Accuracy is the share of test passengers whose predicted class matches the label. The practice notebook repeats the pipeline and records test accuracy 0.77, precision 0.68, and recall 0.75. This module folder also contains instructor copies of the Week 01 EDA notebooks and a finished Titanic feature-engineering notebook. They repeat earlier work.

The conceptual session, [logistic_regression_example.ipynb](Machine%20Learning/Week%2004/Module%2015%20Logistic%20Regression%20Using%20Scikit%20Learn/Conceptual%20Session/logistic_regression_example.ipynb), downloads the IBM telco churn table (7,043 rows, target `Churn`) from a GitHub raw URL, drops `customerID`, and builds a preprocessing pipeline plus logistic regression. The saved **test** baseline accuracy is 0.8038 on 1,407 test rows. ROC AUC is 0.8359, which is the probability that a random churner ranks above a random non-churner. `RandomizedSearchCV` tries 20 draws of `C` and an L1/L2 penalty with `liblinear`, scored by 5-fold accuracy. The best CV accuracy is 0.8052 (`C` about 0.028, L1). The tuned model's **test** accuracy is 0.7989, a bit under the baseline. The last cell prints "Accuracy at Threshold 0.30" but sets `custom_threshold = 0.5`, and the printed accuracy matches the baseline. I would not read that cell as a 0.30-threshold result. [`logistic_regression_visulaization.py`](Machine%20Learning/Week%2004/Module%2015%20Logistic%20Regression%20Using%20Scikit%20Learn/Conceptual%20Session/logistic_regression_visulaization.py) is a separate Streamlit toy: `make_blobs` draws a 2-D set, a sidebar sets penalty, `C`, solver, and iterations, and the page draws the decision regions. It does not use Gemini. The filename spells visualization with one `i`.

[KNN.ipynb](Machine%20Learning/Week%2004/Module%2016%20K%20Nearest%20Neighbour%28KNN%29/KNN.ipynb) loads the wine dataset (178 rows, 13 measurements, 3 classes), scales inside a pipeline, and uses a stratified 80/20 split. A saved classification report shows accuracy 1.00 on 36 test rows for Minkowski `p = 2` with 15 neighbors. Wine is a small, well-separated set, so a perfect test score here is a property of that split, not a reason to prefer KNN in general. [KNN_with_GridSearchCV.ipynb](Machine%20Learning/Week%2004/Module%2016%20K%20Nearest%20Neighbour%28KNN%29/KNN_with_GridSearchCV.ipynb) searches `n_neighbors` from 1 to 29, `p` of 1 or 2, and uniform versus distance weights, with `cv=5`. The saved best parameters are 8 neighbors, `p = 1` (Manhattan), uniform weights. Test accuracy of that estimator is also 1.0. The conceptual session fits `k = 3` on Iris after scaling and records test accuracy 1.0 on 30 rows. The practice notebook (71 of 80 code cells executed) works through Iris, letter recognition, the UCI credit-card default table, and a marketing-campaign file, again with pipelines and grid search. I am not quoting a single score from that notebook because the tasks are different. `ML W4 CS02.pdf` is a large slide export.

[Machine_Learning_Mid_Term.ipynb](Machine%20Learning/Week%2004/Module%2017%20ML%20Mid%20Term/Machine_Learning_Mid_Term.ipynb) is an Adult Income paper. The included [`adult_income.csv`](Machine%20Learning/Week%2004/Module%2017%20ML%20Mid%20Term/adult_income.csv) has 48,842 rows and the census columns, with `income` as the class label. All 78 code cells ran. The exam has an EDA section, a regression section, a classification section, and a tuning section. Question headings show point values (20, 20, 20, 20, and the tuning section). Those are the paper's marks, not a grade.

Two details in the regression half are easy to misread. The code sets `y` to `hours-per-week` and drops `fnlwgt`, `education-num`, and `hours-per-week` from `X`. A later markdown cell says income was removed because it was the target. The code does the opposite: it label-encodes `income` on the full frame and uses it as a feature. That encoder is fit before the split. The saved regression scores on the 20% test fold are train R² 0.188 and test R² 0.177 for linear regression, and train R² 0.182 and test R² 0.173 for SGD, with test MAE about 7.8 hours. An R² near 0.18 means the columns, as used here, explain little of the variation in hours worked.

The classification half is the income task. `income` is the target, the split is stratified 80/20 with `random_state=42`, and the pipeline balances logistic regression. Saved **test** scores are accuracy 0.8056, precision 0.5628, and recall 0.8421. Precision and recall are for the higher-income class. The KNN search over Manhattan versus Euclidean distance, odd `k` from 1 to 29, and uniform versus distance weights selects Manhattan, 29 neighbors, and uniform weights. `accuracy_score` on that model's test predictions prints accuracy 0.8574, precision 0.724, and recall 0.6534. The comparison table later in the notebook is typed in by hand as Tuned KNN accuracy 0.841, precision 0.6798, and recall 0.635. Those typed numbers do not match the printed test scores, so I would trust the `accuracy_score` prints and treat the table as inconsistent with them.

#### Week 05, trees and SVM

The week stays small on purpose. Iris has 150 rows, and every test report below is on 30 rows from a stratified 80/20 split with `random_state=42`.

[Decision_Tree.ipynb](Machine%20Learning/Week%2005/Module%2018%20Decision%20Tree/Decision_Tree.ipynb) fits a default `DecisionTreeClassifier` and then `GridSearchCV` over `criterion` (`gini`, `entropy`) and `max_depth` from 1 to 8 plus `None`. The saved classification report for the default tree shows accuracy 0.97 on the 30 test rows. The search's saved best estimator is `DecisionTreeClassifier(criterion='entropy', max_depth=8)`, and the report after that search shows accuracy 0.93. On this split, the searched tree did not beat the default tree. `Decision Tree.pdf` is a large image-style export. The practice folder has only `Practice Problem.pdf`, and the simple text extract from that PDF was not readable, so I am not describing its questions. There is no solution notebook.

[Random_Forest.ipynb](Machine%20Learning/Week%2005/Module%2019%20Random%20forest%20classification/Random_Forest.ipynb) first refits trees of depth 2, 3, and 4. Saved test accuracy on the 30 rows sits between 0.933 and 0.967, while training accuracy climbs from 0.967 toward 0.992. The forest search covers `criterion` and `n_estimators` in `{100, 150, 200, 250, 300, 400}`. The saved best estimator is `RandomForestClassifier(criterion='entropy', n_estimators=200)`. Its training accuracy is 1.0 and its test accuracy is 0.933. Training accuracy of 1.0 on 120 Iris rows, next to a lower test score, is the overfitting picture the depth loop is there to show. The practice folder again has a PDF and no solution notebook. `Random Forest.pdf` did not yield useful text.

[Support_vector_Classifier_with_Scikit_Learn.ipynb](Machine%20Learning/Week%2005/Module%2020%20Support%20Vector%20Machine/Support_vector_Classifier_with_Scikit_Learn.ipynb) comes back to Titanic with the same stratified 80/20 split and a preprocessing pipeline, then `SVC` inside `GridSearchCV` (`cv=5`). The grid includes ranges of `C`, `gamma`, and kernel settings, with polynomial degree among them. The notebook does not print `best_params_`. What it does print, after `predict`, is training accuracy 0.843, **test** accuracy 0.804, test precision 0.815, and test recall 0.638. The gap between train and test accuracy is the number I would remember from this run. `Support Vector Regressor.pdf` is a short note file whose text did not extract cleanly. The practice folder contains a question PDF and the Breast Cancer CSV (`data.csv`, diagnosis plus 30 numeric features). There is no practice solution notebook, so that CSV is not a completed SVM experiment in this repo. The final exam later uses the same dataset through `load_breast_cancer`.

#### Week 06, clustering, PCA, and the final

[K_Means_Clustering_using_Scikit_Learn_.ipynb](Machine%20Learning/Week%2006/Module%2021%20K%20Means%20Clustering/K_Means_Clustering_using_Scikit_Learn_.ipynb) scales Iris and fits `KMeans(n_clusters=3, max_iter=400, random_state=42)`. The saved inertia is 102.63. Inertia is the within-cluster sum of squares, not an accuracy. The labels are compared with the real species only as a teaching plot. [K_Means_Visualizer.ipynb](Machine%20Learning/Week%2006/Module%2021%20K%20Means%20Clustering/K_Means_Visualizer.ipynb) steps through K-Means on a generated cloud and prints inertia from K=1 (2812) down to K=10 (112). The notebook's own comment reads the elbow near K=4. Only one of three code cells has an execution count, so that commentary is saved output rather than a fresh run I can vouch for cell by cell. The practice notebook is mostly executed and uses `CC GENERAL.csv` (credit-card customers), Iris, and `Mall_Customers.csv`. `K Means Clustering.pdf` contains only a Noteastic title line.

[DBSCAN_using_Scikit_Learn.ipynb](Machine%20Learning/Week%2006/Module%2022%20DBSCAN/DBSCAN_using_Scikit_Learn.ipynb) builds `make_moons(n_samples=300, noise=0.06, random_state=42)`, scales it, and fits `DBSCAN(eps=0.3, min_samples=3)` beside `KMeans(n_clusters=2)`. The point of the pair is visual: DBSCAN follows the crescents, and K-Means with two centers cuts across them. There is no held-out accuracy, because nothing here is a supervised prediction. [Practice.ipynb](Machine%20Learning/Week%2006/Module%2022%20DBSCAN/Practice%20Problem/Practice.ipynb) has 9 of 20 code cells executed. `DBSCAN.pdf` has no extractable lesson text.

[PCA.ipynb](Machine%20Learning/Week%2006/Module%2023%20PCA/PCA.ipynb) loads Breast Cancer, looks at the full explained-variance curve, then makes a stratified 80/20 split (`random_state=42`). Two pipelines each contain `StandardScaler` and `LogisticRegression(max_iter=500)`. One adds `PCA(n_components=10)`. Saved **test** accuracy is 0.982 without PCA and 0.974 with 10 components. The drop is small on this split. PCA here is a compression step in front of a classifier, not a clustering result. The instructor notebook is [Phitron_PCA.ipynb](Machine%20Learning/Week%2006/Module%2023%20PCA/Phitron_PCA.ipynb). `PCA.pdf` is another image export.

[ML_FINAL.ipynb](Machine%20Learning/Week%2006/Module%2024%20ML%20Final%20Exam/ML_FINAL.ipynb) is the end-to-end exam on Breast Cancer Wisconsin Diagnostic, loaded with `load_breast_cancer` (569 rows, 30 numeric features, target benign versus malignant). The written description treats the features as measurements from fine-needle aspirate images. Forty-two of forty-three code cells ran. The supervised path drops six redundant size columns (`mean perimeter`, `mean area`, `worst perimeter`, `worst area`, `perimeter error`, and `area error`) after a correlation check on the **full** frame, then does a stratified 80/20 split. That column drop sees the test rows, so the feature list is not chosen from training data alone. Scaling is inside the model pipelines, which does keep the scaler's `fit` on the training fold. `LogisticRegression(max_iter=500)` records test accuracy 0.98 on 114 rows. `RandomForestClassifier(n_estimators=300)` records test accuracy 0.96 on the same fold. The write-up prefers logistic regression and mentions the forest's false negatives and false positives. I would read 0.98 as one stratified split of a clean, linearly separable medical table, not as a clinical result.

The unsupervised section scales the full feature matrix, fits PCA, and runs K-Means for K from 1 to 19. Inertia falls from 16,243 to 4,637, which it will always do as K grows. A 2-cluster K-Means and `DBSCAN(eps=3, min_samples=8)` are fit on the PCA projection of all rows. Those fits are exploration. They are not test-set scores. The exam's last section is a reflection prompt. I am leaving that personal answer out of this README. Section headings show the paper's mark breakdown (15, 15, 10, 10, 5, 15, 20, 10). No awarded grade is stored.

#### Eid vacation

[Eid_ul_Adha_Vacation.ipynb](Machine%20Learning/Eid%20Vacation/Eid_ul_Adha_Vacation.ipynb) is an optional advanced set, and 84 of 85 code cells ran. The questions I can see from the headings are an income problem, a churn problem, a z-score problem, a large-city outlier problem, and a world-happiness EDA. The income section calls `fetch_ucirepo(id=2)`, which is the UCI Adult data (the same task as the midterm, downloaded rather than read from `adult_income.csv`). Churn and insurance use the CSVs in this folder. Happiness uses `world-happiness-report-2021.csv`. One cell reads `NYC.csv` and samples 20,000 rows. That file is not in the repository, so this notebook does not rerun from a fresh clone without it. [Eid Vacation Problemset (Advanced).pdf](Machine%20Learning/Eid%20Vacation/Eid%20Vacation%20Problemset%20%28Advanced%29.pdf) is the question packet. Its text encoding did not come out cleanly.

[Beginner_Friendly_Practice_Set_(_Optional_)_.ipynb](Machine%20Learning/Eid%20Vacation/Beginner_Friendly_Practice_Set_%28_Optional_%29_.ipynb) is a separate optional set of 27 questions, from easy EDA through a bonus full pipeline, and all 29 code cells ran. The bonus builds a `ColumnTransformer` for a `Purchased` target. It is practice, not a new dataset study.

---

## Practical Work and Projects

| Project / experiment | Task / dataset | Method | Main learning | Source |
|---|---|---|---|---|
| Streamlit widget tour | Local image, audio, and video files plus uploads | One script per widget. No model | What Streamlit shows, and that each file is its own entry point | [STREAMLIT/](AI%20Programming%20With%20Python/Week%2002/Module%2006%20Streamlit%20%26%20Gemini%20API/STREAMLIT/) |
| Gemini one-shot page | Fixed prompt, text out | `gemini-3-flash-preview` at startup | How the client and `GEMINI_API_KEY` are wired | [app.py](AI%20Programming%20With%20Python/Week%2002/Module%2006%20Streamlit%20%26%20Gemini%20API/STREAMLIT/app.py) |
| Note summary and quiz | Up to 3 note images in, markdown summary, spoken summary, quiz out | Hosted Gemini vision call plus `gTTS`. Difficulty is Easy, Medium, or Hard | Prompting a multimodal API, and keeping the quiz prompt inside the image | [app.py](AI%20Programming%20With%20Python/Week%2002/Module%2007/app.py) |
| AI Code Debugger | Up to 3 error screenshots. Modes: hints, or solution with code | Two Gemini calls: an "issue" pass, then the selected mode | Separating a hint from a full fix in the prompt | [app.py](AI%20Programming%20With%20Python/Week%2002/Module%207.5/app.py) |
| Titanic preprocessing thread | 891 passengers, target `Survived` | Split, train-only age statistics, z-score and IQR, encoders, scalers, then a `ColumnTransformer` | The pieces of a preprocessing pipeline before a model is attached | [ColumnTransformer notebook](Machine%20Learning/Week%2002/Module%2008%20Scaling/Titanic_Feature_Engineering_via_columntransformer.ipynb) |
| Line from scratch | Five salary numbers | Batch gradient descent, learning rate 0.01 | Cost falling from about 790 to about 0 on the training points | [notebook](Machine%20Learning/Week%2003/Module%2010%20Simple%20Linear%20Regression%20Implementation%20and%20Gradient%20Descent/Simple_Linear_Regression.ipynb) |
| IQ and CGPA line | 1,000-row `iq_cgpa_org.csv`, 80/20 | `LinearRegression` | Test R² 0.950, RMSE 0.273 | [notebook](Machine%20Learning/Week%2003/Module%2010%20Simple%20Linear%20Regression%20Implementation%20and%20Gradient%20Descent/Conceptual%20Session/ML_Week_03_CS_01.ipynb) |
| Student-result pipelines | `hsc_result` on the Bangladesh student table | `ColumnTransformer` inside `Pipeline`, linear and SGD | Test R² 0.946 and 0.945. The conceptual session also stores 5-fold R² mean 0.945 | [ML_Pipeline.ipynb](Machine%20Learning/Week%2003/Module%2012%20Multiple%20Linear%20Regression%20with%20Scikit%20Learn/ML_Pipeline.ipynb) |
| Housing practice | 545-row housing file, target `price` | Same pipeline pattern | Test R² about 0.55. Linear regression has the lower saved test RMSE | [notebook](Machine%20Learning/Week%2003/Module%2012%20Multiple%20Linear%20Regression%20with%20Scikit%20Learn/Practice%20Problem/Practice_Problem.ipynb) |
| House-price assignment | 1,000-row assignment file, target `House_Price` | From-scratch step plus SGD and linear pipelines | Test R² 0.998 on this file | [ML_Assignment_02.ipynb](Machine%20Learning/Week%2003/Module%2013%20ML%20Assignment%2002/ML_Assignment_02.ipynb) |
| Titanic logistic regression | `Survived`, stratified 80/20 | Balanced `LogisticRegression` in a pipeline | Test accuracy 0.76, precision 0.67, recall 0.75 | [notebook](Machine%20Learning/Week%2004/Module%2015%20Logistic%20Regression%20Using%20Scikit%20Learn/Logistic_Regression_with_Scikit_Learn.ipynb) |
| Telco churn | 7,043 customers, target `Churn`, downloaded in the notebook | Pipeline, ROC, `RandomizedSearchCV` | Test accuracy 0.804 baseline, ROC AUC 0.836. Tuned test accuracy 0.799 | [notebook](Machine%20Learning/Week%2004/Module%2015%20Logistic%20Regression%20Using%20Scikit%20Learn/Conceptual%20Session/logistic_regression_example.ipynb) |
| Decision-region toy | `make_blobs`, binary or 3-class | Streamlit plus `LogisticRegression` | How penalty, `C`, and the solver move a 2-D boundary | [script](Machine%20Learning/Week%2004/Module%2015%20Logistic%20Regression%20Using%20Scikit%20Learn/Conceptual%20Session/logistic_regression_visulaization.py) |
| Wine KNN | 178 wines, 3 classes | Scaled pipeline and `GridSearchCV` | Best saved setting is 8 neighbors, Manhattan, uniform. Test accuracy 1.0 on 36 rows | [notebook](Machine%20Learning/Week%2004/Module%2016%20K%20Nearest%20Neighbour%28KNN%29/KNN_with_GridSearchCV.ipynb) |
| Adult income midterm | 48,842 census rows | Hours regression, then income classification and a KNN search | Classification test accuracy 0.806 logistic, 0.857 for the searched KNN. Hours R² about 0.18 | [notebook](Machine%20Learning/Week%2004/Module%2017%20ML%20Mid%20Term/Machine_Learning_Mid_Term.ipynb) |
| Iris trees and forest | 150 flowers, 30-row test | Depth comparison, then grid search | Forest search picks entropy and 200 trees. Test accuracy 0.933, training accuracy 1.0 | [notebook](Machine%20Learning/Week%2005/Module%2019%20Random%20forest%20classification/Random_Forest.ipynb) |
| Titanic SVM | `Survived`, stratified split, preprocessing pipeline | `SVC` with `GridSearchCV` | Test accuracy 0.804, precision 0.815, recall 0.638. Train accuracy 0.843 | [notebook](Machine%20Learning/Week%2005/Module%2020%20Support%20Vector%20Machine/Support_vector_Classifier_with_Scikit_Learn.ipynb) |
| Moons and K-Means | `make_moons`, Iris | `DBSCAN` versus `KMeans`. Elbow plot on a toy cloud | Clustering is not a labeled test score | [DBSCAN](Machine%20Learning/Week%2006/Module%2022%20DBSCAN/DBSCAN_using_Scikit_Learn.ipynb), [K-Means](Machine%20Learning/Week%2006/Module%2021%20K%20Means%20Clustering/K_Means_Clustering_using_Scikit_Learn_.ipynb) |
| PCA on Breast Cancer | 30 features, stratified 80/20 | Logistic regression with and without 10 principal components | Test accuracy 0.982 without PCA, 0.974 with 10 components | [PCA.ipynb](Machine%20Learning/Week%2006/Module%2023%20PCA/PCA.ipynb) |
| Final exam | Breast Cancer Wisconsin, benign vs malignant | Two supervised pipelines, then PCA, K-Means, and DBSCAN on the full table | Test accuracy 0.98 logistic, 0.96 forest, on 114 rows. Unsupervised fits are separate | [ML_FINAL.ipynb](Machine%20Learning/Week%2006/Module%2024%20ML%20Final%20Exam/ML_FINAL.ipynb) |

Metrics in this table are copied from notebook outputs. A perfect score on Iris or wine is a small-test-set result.

---

## Assignments and Exams

| Assessment | What was submitted | Dataset and target | What the saved work shows |
|---|---|---|---|
| AI Week 01 exam | Image question notebook, 0 of 5 code cells executed | Not readable from the images | Question packet only |
| AI Practice Days 01 and 02 | Executed solution notebooks | Tiny inputs and local text files | Functions, batches, and safe file reads. See Week 01 |
| AI midterm | [notebook](AI%20Programming%20With%20Python/Week%2003/Module%2011%20Mid%20Term%20Exam/AI_Programming_With_Python_Mid_Term.ipynb), 11 of 19 code cells executed | `staff_data.csv`, which is not in the repo | Partial NumPy and Pandas answers. No stored grade |
| AI final | Blank question file plus two filled notebooks | `school_data.csv`, also not in the repo. Score and attendance are the numeric columns | Average score 67.3 in the saved print. Plots of score by grade and attendance versus score. Questions are marked at 10 points each. No stored grade |
| ML Assignment 01 | [notebook](Machine%20Learning/Week%2001/ML%20Assignment%2001/ML_Assignment_01.ipynb), all 41 code cells executed | Titanic, target `Survived` | EDA, an 80/20 split (712 / 179), and imputers. No classifier |
| ML Assignment 02 | [notebook](Machine%20Learning/Week%2003/Module%2013%20ML%20Assignment%2002/ML_Assignment_02.ipynb), all 26 code cells executed | 1,000-row house file, target `House_Price` | From-scratch cost about 0.0088 after scaling. Test R² 0.9981 (SGD) and 0.9984 (linear). No cross-validation score is saved |
| ML midterm | [notebook](Machine%20Learning/Week%2004/Module%2017%20ML%20Mid%20Term/Machine_Learning_Mid_Term.ipynb), all 78 code cells executed | Adult Income, 48,842 rows | Hours-per-week regression test R² about 0.18. Income classification test accuracy 0.8056 (logistic) and 0.8574 (searched KNN). The handwritten comparison table disagrees with the KNN print. See Week 04 |
| ML final | [notebook](Machine%20Learning/Week%2006/Module%2024%20ML%20Final%20Exam/ML_FINAL.ipynb), 42 of 43 code cells executed | Breast Cancer Wisconsin, target benign/malignant | Test accuracy 0.98 and 0.96 on 114 rows. Feature columns were dropped using the full frame. Clustering is unsupervised |
| Week 05 practice | PDF question sheets only | Iris is used in the lesson notebooks. The SVM practice folder also contains a Breast Cancer CSV | No solution notebooks, and the PDF text did not extract |
| Eid sets | Advanced notebook mostly executed. Beginner notebook fully executed | Adult via UCI, local churn, insurance, happiness. `NYC.csv` is referenced and missing | Optional. The advanced PDF is the question side |

I do not have awarded marks for any of these. The "10 marks" and "20 marks" lines inside the notebooks are the question weights.

---

## Machine Learning Workflow

`Structure.md` lists this order:

```text
Problem definition
Data collection
Exploratory data analysis
Train/test split
Feature engineering and preprocessing
    missing values, outliers if needed, encoding, scaling
ColumnTransformer
Model training
Model evaluation
Hyperparameter tuning
Model deployment and monitoring
```

The notebooks follow that shape in pieces, and they do not all follow it.

EDA comes first, on Titanic, and the split usually comes before imputation. In the feature-engineering notebook the age mean and median are computed on `X_train` and applied to `X_test`, which is the pattern the Week 01 practice write-up argues for. From the student-result notebook onward, imputers and scalers often live inside a `Pipeline`, so a later `fit` on the training fold refits them. `GridSearchCV` and `RandomizedSearchCV` then score those pipelines with cross-validation. That is the careful version, and it is not the only version in the repo.

A few saved results sit outside that pattern. The Python recap picks KNN's `k` by test accuracy. The final exam drops correlated columns after looking at the full Breast Cancer frame. The midterm label-encodes `income` on the whole table before the hours-per-week split, and the written note describes a different target than the code uses. Outlier row removal is pandas filtering, not a transformer step. `ColumnTransformer` in Week 02 is preprocessing only. A full preprocessing-and-model pipeline shows up in Week 03.

Deployment and monitoring are the last line of `Structure.md`. I do not have a saved model, an API for one, a monitoring job, or a dashboard of live predictions. The Streamlit work from the Python course calls Gemini. It is not a deployment of these classical models.

---

## Skills and Learning Outcomes

The files show a path I can actually rerun in places and only read in others.

I can write the Python the later notebooks assume: functions, files, exceptions, and small class hierarchies. I can load a table with Pandas, draw the chart that matches the question, and read a profiling report. On Titanic I can split, impute from the training fold, cap or drop outliers, encode, scale, and pack those steps in a `ColumnTransformer`. From Week 03 I can put that transformer in a `Pipeline` with a linear model, a logistic model, a neighbor model, a tree, a forest, or an SVM, and I can search a small grid.

I have also written gradient descent for a line and for a small multiple regression, and I have a logistic version whose saved loss does not go down. I can tell a test score from a training score, and I can see when a typed comparison table does not match the printed metric. Clustering and PCA are in the repo as unsupervised tools. The last page of `Structure.md` is still an outline.

---

## How to Use

### Clone

```bash
git clone https://github.com/ak1bhasan/ML_Journey.git
cd ML_Journey
```

### A sensible order

1. AI Programming, Weeks 01 through 04, including the practice days before each exam.
2. Machine Learning, Weeks 01 through 06. The Titanic notebooks are sequential. Later weeks assume the split and the encoders.
3. The Eid folder whenever you want extra tables. It is optional, and the advanced notebook expects `NYC.csv` plus a network call for UCI Adult.

When a `Phitron_` notebook and an unprefixed notebook share a folder, start with the unprefixed one if you want the version I ran. Use the prefixed one to see the instructor's original.

### Notebooks

There is no project-wide requirements file. For a local kernel, install what the notebook imports. A practical set for the ML weeks is:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn plotly jupyter
```

Add `openpyxl` and `pyarrow` if you want the Excel and Parquet cells in the Pandas week to load. Add `ydata-profiling` only for the EDA Part 2 report. Add `ucimlrepo` only for the Eid Adult download. Add `torch` only if you want to rerun the untrained recap cell. None of these versions are pinned in the repo.

Several instructor notebooks and both AI exams refer to Google Colab. The instructor conceptual-session notebooks use `/content/...` paths. If you open those locally, point `read_csv` at the CSV in the same folder. My copies generally use a filename only, so the kernel's working directory needs to be the notebook's folder.

Run a notebook from top to bottom. A saved output can be older than the cell above it. Where this README mentions a conflict, the conflict is already in the file.

### Streamlit

Run each app from its own directory. `api_calling` is a local import, and the media scripts use relative paths such as `audio/welcome.mp3`.

```bash
# Widget demos and the one-shot Gemini page
cd "AI Programming With Python/Week 02/Module 06 Streamlit & Gemini API/STREAMLIT"
pip install streamlit python-dotenv google-genai
streamlit run txt_input.py
streamlit run input_element.py
streamlit run image_element.py
streamlit run audio.py
streamlit run video.py
streamlit run app.py

# Note Summary and Quiz Generator
cd "AI Programming With Python/Week 02/Module 07"
pip install -r requirements.txt
streamlit run app.py

# AI Code Debugger
cd "AI Programming With Python/Week 02/Module 7.5"
pip install -r requirements.txt
streamlit run app.py

# Practice-day apps
cd "AI Programming With Python/Week 02/Module 6.5 Practice Day"
streamlit run "Problem 01.py"
streamlit run "Problem 02.py"
streamlit run "Problem 03.py"

# 2-D logistic visualizer, no API key
cd "Machine Learning/Week 04/Module 15 Logistic Regression Using Scikit Learn/Conceptual Session"
pip install streamlit scikit-learn matplotlib numpy
streamlit run logistic_regression_visulaization.py
```

On Windows PowerShell, quote any path that contains `&`.

Every Gemini script reads the key with `load_dotenv()` and `GEMINI_API_KEY` (`os.getenv` or `os.environ.get`). Put a `.env` file in the directory you launch from:

```text
GEMINI_API_KEY=your_key_here
```

Do not commit that file. The note app also needs a network connection for `gTTS`. Calling `gemini-3-flash-preview` is a paid or quota-limited API call. Nothing in these apps trains a model.

### Datasets and assets

| Dataset / asset | Used in | Included or downloaded | Setup notes |
|---|---|---|---|
| `titanic_data_updated.csv` | EDA through logistic regression, SVM, Assignment 01 | Included, copied into many module folders | 891 rows plus header. Target `Survived`. Open the notebook from the folder that holds the CSV |
| `Titanic-Dataset.csv` | Module 01 alongside the updated file | Included | Same columns |
| Student CSV, Excel, Parquet, JSON | AI Pandas and plotting weeks | Included next to the notebooks | `phitron_student_marks.xlsx` needs an Excel engine |
| `sns_data.csv`, `students.csv`, `sales.csv`, `enrollment_data.csv`, IQ and practice CSVs | Plotting modules | Included | Practice notebooks expect those filenames |
| `marks_dataset.csv` | Winsorization and robust scaling | Included | 100 students |
| `iq_cgpa_org.csv` | Week 03 conceptual session | Included | Columns `IQ`, `CGPA` |
| Bangladesh student CSVs | Pipeline lesson and conceptual session | Included | Target `hsc_result`. The pipeline notebook uses the `_updated` file |
| `house_price_regression_dataset.csv` | ML Assignment 02 | Included | Target `House_Price` |
| `Housing.csv`, `Salary_Data.csv`, `Salary Data.csv`, `StudentsPerformance.csv`, `insurance.csv` | Regression practice | Included | `insurance.csv` is also in the Eid folder |
| Diabetes, heart, tips, car prices, HR attrition, `hotel_bookings.csv` | Encoding practice | Included | The hotel file is large and is not what the executed modeling cells load |
| `adult_income.csv` | ML midterm | Included | Target `income` for the classification half |
| Wine, Iris, Breast Cancer, diabetes, California housing | KNN, trees, PCA, scaling practice | Loaded from scikit-learn | No download if scikit-learn's data cache can be built |
| Telco churn CSV | Eid notebook | Included | The Week 04 conceptual session downloads a copy from GitHub instead |
| World Happiness 2021 and the historical report | Eid notebook | Included | |
| `NYC.csv` | One Eid cell, target `trip_duration` | Not included | That cell cannot rerun from this clone |
| `staff_data.csv`, `school_data.csv` | AI midterm and AI final | Not included | Saved outputs assume the file was present on the Colab machine |
| `gk` style images, `welcome.mp3`, `nature.mp4`, sample images | Streamlit demos | Included under `STREAMLIT/` | Paths are relative to that folder |
| UCI Adult via `fetch_ucirepo` | Eid advanced notebook | Downloaded at runtime | Needs `ucimlrepo` and a network connection |
| Seaborn `tips` and `penguins` | EDA and plotting | Downloaded by Seaborn on first use | |

---

## Where this repository stops

Classical models, from a hand-written line to PCA, are as far as these folders go. Neural networks, convolutional models, sequence models, and the NLP preprocessing that goes with them are in my [Deep Learning](https://github.com/ak1bhasan/Deep-Learning) and [Advanced Deep Learning](https://github.com/ak1bhasan/Advanced_Deep_Learning) repositories. They are not modules of this one.

Still outside all three repositories, as far as these course folders show: boosting libraries, experiment trackers, serving a trained scikit-learn model, and monitoring it after deployment. `Structure.md` names the last two. The code does not.

---

## Acknowledgements

The courses are from [Phitron](https://phitron.io). Instructor notebooks are the `Phitron_` files. Slide decks, OneNote-style PDFs, and the practice sheets came with the classes. The Dartmouth summer-project paper and the ML-pipeline slides in Week 03 are reference reading, not my notes.

Datasets and where they enter the work:

- Titanic tables, in the form used throughout the ML weeks.
- UCI Adult / Census Income, as `adult_income.csv` and again through `ucimlrepo` (Barry Becker and Ronny Kohavi).
- Breast Cancer Wisconsin Diagnostic, wine, and Iris, through scikit-learn.
- Pima Indians diabetes, the UCI heart table, the car-price assignment file, IBM HR attrition, and the tips table, in the encoding practice folder.
- The housing-price practice file. The practice notebook points at the Kaggle housing prices dataset as the source of `Housing.csv`.
- IBM telco customer churn, downloaded in the logistic-regression conceptual session and stored again under `Eid Vacation/`.
- World Happiness Report tables in the Eid folder.
- Mall customers, credit-card customers (`CC GENERAL.csv`), letter recognition, UCI credit-card default, and the marketing campaign file, in the clustering and KNN practice folders.
- Student, enrollment, and marks tables written for the Python course.
- Seaborn's built-in `tips` and `penguins` examples.

The Module 7.5 README is the project description for the code debugger, including the demo link.

---

<div align="center">

Learn the step, run the notebook, and read the saved score against the split that produced it.

[Repository on GitHub](https://github.com/ak1bhasan/ML_Journey)

</div>
