# Titanic++ Survival Prediction System

A Django web application that predicts the survival outcome of Titanic passengers using a machine learning model. Users can input passenger details, get real-time predictions, and view prediction history.

---

## Features

- **Prediction Form**: Enter passenger details (age, sex, class, fare, etc.) to get survival prediction.
- **Prediction History**: View all past predictions stored in the database.
- **ML Model Integration**: Pre-trained model (Random Forest) loaded via joblib.
- **Responsive UI**: Simple and clean interface built with Bootstrap.

---

## Django + ML Project

This repository contains a **simple, beginner‑friendly Django project** with a clear path toward adding **machine‑learning features later**.

The goal of this README is to help **any teammate** clone the repo and get a working Django server running **without prior context**.

---

## 🧰 Tech Stack

- **Python:** 3.11
- **Django:** 5.2 (LTS)
- **Environment management:** Conda (Miniconda)
- **Database**: SQLite (development) / PostgreSQL (production)
- **ML libraries (installed but optional):** NumPy, SciPy, scikit‑learn, pandas, joblib
- **Deployment**: Gunicorn, Nginx, Docker (optional)

---

## 📦 Prerequisites

You need the following installed locally:

- **Git**
  [https://git-scm.com/](https://git-scm.com/)

- **Miniconda** (recommended) or Anaconda
  [https://www.anaconda.com/docs/getting-started/miniconda/install](https://www.anaconda.com/docs/getting-started/miniconda/install)

Verify installation:

```bash
git --version
conda --version
```

---

## 📁 Project Structure

```text

titanic_capstone/
├── db.sqlite3
├── environment.yml      # Conda environment definition
├── LICENSE
├── manage.py
├── backend/             # Django project (settings, URLs, ASGI/WSGI)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── docs/               # Documentations
│   ├── API.md
│   ├── CONTRIBUTING.md
│   ├── README.md
│   └── USER_GUIDE.md
├── ML/                 # ML artifacts and experimentation code and Dataset directory
│   ├── __init__.py
│   ├── Advanced_Evaluation.ipynb
│   ├── EDA.ipynb
│   ├── featureEngineering.ipynb
│   ├── titanic_capstone.ipynb
│   ├── titanic_clean_train.csv
│   ├── titanic_cleaned_test_data.csv
│   ├── titanic_cleaned_training_data_FE.csv
│   ├── titanic_cleaned_training_data.csv
│   ├── titanic_predictions_output.csv
│   ├── model_training/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── evaluate.py
│   │   ├── model_definition.py
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   ├── utils.py
│   │   ├── __pycache__/
│   │   └── artifacts/
│   │       └── metrics.json
│   └── titanic_data/
│       ├── gender_submission.csv
│       ├── test.csv
│       └── train.csv
├── notebooks/          # Exploratory workbooks (01_eda_template.ipynb)
│   └── 01_eda_template.ipynb
└── webapp/             # Django app (views, models, migrations, tests)
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── __pycache__/
    ├── management/
    │   ├── __init__.py
    │   ├── __pycache__/
    │   └── commands/
    │       ├── __init__.py
    │       ├── import_passengers.py
    │       └── __pycache__/
    ├── migrations/
    │   ├── __init__.py
    │   ├── 0001_initial.py
    │   ├── 0002_alter_passenger_age.py
    │   ├── 0003_alter_passenger_age_alter_predictionrecord_age.py
    │   ├── 0004_remove_features_json.py
    │   ├── 0005_remove_features_json.py
    │   ├── 0006_alter_predictionrecord_age.py
    │   ├── 0007_remove_predictionrecord_cabin_and_more.py
    │   ├── 0008_predictionrecord_v2.py
    │   ├── 0009_delete_predictionrecord_v2.py
    │   ├── 0010_predictionrecord_rating.py
    │   └── __pycache__/
    ├── static/
    │   └── webapp/
    │       └── images/
    └── templates/
        └── webapp/
            ├── base.html
            ├── home.html
            ├── prediction_form.html
            ├── prediction_list.html
            ├── results.html
            └── partials/
                └── prediction.html

```

> 💡 At a minimum you need `backend/`, `webapp/`, and `manage.py` to run Django.

---

## Installation Steps

### Clone repository

you need to have same structure as main(copy url from github main):

```bash
git clone [repository-url]
```

## 🐍 Environment Setup

### 1️⃣ Create the Conda environment

From the project root:

```bash
conda env create -f environment.yml
```

This installs:

- Python 3.11
- Django 5.2
- Scientific libraries (for future ML work)

### 2️⃣ Activate the environment

```bash
conda activate titanic_capstone_ml
```

### 3️⃣ Verify

```bash
python --version
django-admin --version
```

Expected:

- Python 3.11.x
- Django 5.2

---

## ▶️ Running the Django Project

Apply initial migrations:

```bash
python manage.py migrate
```

Load ML model:

```bash
python -m ml.model_training.train
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

You should see the project page in the browser's window.

---

## Machine Learning Model

- Model type: [e.g., Random Forest Model]
- Features used: [
  list key features: 
  Name, Pclass, Sex, Age, Parch (parent or children), Embarked, Fare, SibSp,
  ]
- Accuracy: [85%]
- Training process: [
  Load cleaned training dataset,
  Perform train test split,
  Train Logistic Regression mode,
  Sve trained model(titanic_model.pkl),
  Verify model loads correctly
]

---

## API Documentation

See API.md for details.

---

## Architecture Diagram

The system follows a typical Django MVT (Model-View-Template) architecture with an integrated machine learning component.

**Components:**

- **Browser**: User interface (HTML forms, Bootstrap).
- **Django Server**: Handles HTTP requests, serves templates, processes forms.
- **Views**:
  - `predict_view`: Receives form data, calls ML predictor, stores result in DB.
  - `history_view`: Queries database and displays past predictions.
- **ML Predictor**: Loads the pre-trained model (`model.pkl`) and makes predictions using `joblib` and `scikit-learn`.
- **Database**: Stores prediction history (SQLite/PostgreSQL).
- **API Endpoint**: Optional JSON API for external clients.

**Data Flow:**

1. User submits prediction form → POST request to Django.
2. View extracts data, validates using Django Form.
3. View passes data to `preprocess.py` which preprocesses and calls model.
4. Prediction result is returned to view.
5. View saves result (input + output) to database.
6. View renders result template with prediction.
7. History page queries database and displays records.

[User Browser] → [Django Web Server] → [ML Model] → [Database]
       ↓               ↓                  ↓           ↓
    HTML Forms     Views/Logic       .pkl file   SQLite/PostgreSQL
       ↓               ↓                  ↓           ↓
  [Results Page] [Process Data]   [Make Prediction] [Store Data]

---

## Deployment

See DEPLOY.md for production deployment instructions.

---

## Contributing

See CONTRIBUTING.md for details.

---

## License

[MIT]

---

## Team Members & Responsible Tasks

- [Bharathi]:
Feature Engineering & EDA with Visualizations
Advanced Evaluation & Result Page & History Page
- [Gabriela]:
GitHub Setup & Documentation & Django Project Setup
Model Training & Database Persistence & History Page
- [Saranya]:
Data Inspection & Analysis & Missing Data Handling
Testing Framework & Homepage & Model Integration
- [Siying]:
Database Model Design & Prediction form
Documentation & Error Handling & User Experience

---

## 📦 Dependency Management Rules

- Use **Conda** for all dependencies
- Do **not** install NumPy / SciPy / scikit‑learn with `pip`
- Update dependencies only via `environment.yml`

To apply changes:

```bash
conda env update -f environment.yml --prune
```

---

## 🧠 About the `ml/` Folder

The `ml/` folder is reserved for **future machine‑learning code**.

At this stage:

- It may be empty or not included
- It is **not required** to run Django

When ML is added later:

- Models will be loaded lazily
- No ML code will run at Django startup

---

## 🧪 Common Issues

**Django commands fail**

- Make sure the Conda environment is activated

---

## 📚 Common Commands

```bash
conda activate titanic_capstone_ml
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```

---

Happy hacking 👋
