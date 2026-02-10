## Titanic++ Survival Prediction System -SR

# Project Overview
- Brief description: A machine learning system that predicts Titanic passenger survival
- Purpose: Capstone project integrating ML, web development, and DevOps
- Key technologies: Python, Django, Scikit-learn, PostgreSQL/SQLite


# Django + ML Project

This repository contains a **simple, beginner‑friendly Django project** with a clear path toward adding **machine‑learning features later**.

The goal of this README is to help **any teammate** clone the repo and get a working Django server running **without prior context**.

---

## 🎯 Project Purpose

- Provide a **clean Django 5.2 (LTS)** starting point
- Use **Python 3.11** managed via **Miniconda**
- Keep the setup simple and reproducible
- Prepare the ground for adding ML (NumPy / scikit‑learn) later

At this stage, the project is **pure Django**. No ML code is required to run it.

---

## 🧰 Tech Stack

- **Python:** 3.11
- **Django:** 5.2 (LTS)
- **Environment management:** Conda (Miniconda)
- **ML libraries (installed but optional):** NumPy, SciPy, scikit‑learn, pandas

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
project-root/
├── backend/              # Django project (settings, URLs, ASGI/WSGI)
├── webapp/               # Django app (views, models, migrations, tests)
├── data/                 # Dataset directory (empty for now)
├── ml/                   # ML artifacts and experimentation code (currently empty)
├── notebooks/            # Exploratory workbooks (01_eda_template.ipynb)
├── db.sqlite3
├── environment.yml       # Conda environment definition
├── manage.py
├── README.md
└── .gitignore
```

> 💡 At a minimum you need `backend/`, `webapp/`, and `manage.py` to run Django.

---

## Steps

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
[instructions?]


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

- Model type: [e.g., Random Forest Classifier?]
- Features used: [
  list key features: 
  Name,Sex, Age, Parch (parent or children), Embarked
  optional:Ticket, Fare, Cabin, SibSp 
  ]
- Accuracy: [performance metrics?]
- Training process: [brief description?]


---

## System Architecture
[Refer to architecture diagram in docs/png?]


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


## License
[?]



---

## 🔌 Example Endpoint (Sanity Check)

This project includes a minimal endpoint to confirm everything works.

### View (`webapp/views.py`)

```python
from django.http import HttpResponse


def ping(request):
    return HttpResponse("pong")
```

### URL configuration (`webapp/urls.py`)

```python
from django.urls import path
from .views import ping

urlpatterns = [
    path("ping/", ping),
]
```

### Project URLs (`backend/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("webapp.urls")),
]
```

Test it in the browser:

```
http://127.0.0.1:8000/ping/
```

Expected response:

```
pong
```

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
