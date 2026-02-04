# Django + ML Project (Beginner Friendly)

This repository is the starting point for a **Django web application** that also uses **Python machine‑learning libraries** (NumPy, scikit‑learn).
It is designed to be **easy to set up**, **reproducible**, and **safe for beginners**.

The project uses **Miniconda** to manage Python and dependencies.

---

## 🚀 What This Project Is

- A Django **5.2 (LTS)** backend
- Running on **Python 3.14**
- With a scientific stack (**NumPy**, **scikit‑learn**, **SciPy**, **pandas**)
- Managed via a **Conda environment** for reliability

This setup is suitable for:

- Learning Django
- Adding basic ML / data‑processing features
- Growing into a production‑ready backend later ^^

---

## 📦 Prerequisites

Before you start, make sure you have:

- **Git**
- **Miniconda** (recommended) or Anaconda

Check installation:

```bash
git --version
conda --version
```

---

## 🧱 Project Structure

```text
project-root/
├── backend/              # Django project config (settings.py, urls.py, etc.)
├── core/                 # Django app
├── ml/                   # ML-related code (models, inference, utils)
├── manage.py
├── environment.yml
├── README.md
└── .gitignore
```

---

## 🐍 Environment Setup (Step‑by‑Step)

### 1️⃣ Create the Conda environment

From the project root:

```bash
conda env create -f environment.yml
```

This will:

- Install Python 3.14
- Install Django 5.2
- Install NumPy, scikit‑learn, and other dependencies

### 2️⃣ Activate the environment

```bash
conda activate django-ml
```

### 3️⃣ Verify installation

```bash
python --version
# Python 3.14.x

django-admin --version
# 5.2
```

---

## ▶️ Creating the Django Project

Create the Django project inside your repo:

```bash
django-admin startproject backend .
```

This creates the `backend/` folder with `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`.

### 1️⃣ Create a Django app

```bash
python manage.py startapp core
```

Register it in `backend/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

## ▶️ Running the Development Server

```bash
python manage.py migrate
python manage.py runserver
```

Open your browser at:

```
http://127.0.0.1:8000/
```

You should see the Django welcome page.

---

## 📄 First Django View + URL (No ML yet)

Create a simple view in `core/views.py`:

```python
from django.http import HttpResponse


def ping(request):
    return HttpResponse("pong")
```

Add a URL for it in `core/urls.py`:

```python
from django.urls import path
from .views import ping

urlpatterns = [
    path('ping/', ping),
]
```

Include the app URLs in `backend/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

Visit:

```
http://127.0.0.1:8000/ping/
```

You should see:

```
pong
```

---

## 📁 Environment Management Rules

- **Do not** install NumPy / SciPy / scikit‑learn with `pip`
- Always update dependencies via `environment.yml`
- If you add a new package:

```bash
conda env update -f environment.yml --prune
```

---

## 🧪 Development Tips

- Use virtual environments **only through Conda**
- Restart the server after dependency changes
- Commit `environment.yml`, not a raw `conda env export`

---

## ❓ Common Issues

**Problem:** `ModuleNotFoundError`

- Make sure the Conda environment is activated

**Problem:** Conda solve takes a long time

- Ensure only `conda-forge` is used

---

## 📚 Useful Commands Cheat Sheet

```bash
conda activate django-ml
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```

---

## 📌 Next Steps

Some ideas for extending this project:

- [TODO]

---

## 📝 License

Choose a license before publishing (MIT is common for learning projects).

---

Happy hacking 👋
