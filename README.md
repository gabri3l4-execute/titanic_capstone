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

## 🧱 Project Structure (Not written in stone)

```text
project-root/
├── environment.yml        # Conda environment definition
├── README.md              # This file
├── manage.py              # Django entry point
├── backend/               # Django project & apps
│   ├── settings/
│   ├── apps/
│   └── ml/                # ML-related code (models, inference, utils)
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

Optional sanity check:

```bash
python - <<EOF
import numpy, sklearn
print(numpy.__version__)
print(sklearn.__version__)
EOF
```

---

## ▶️ Running the Development Server

```bash
python manage.py migrate
python manage.py runserver
```

Open your browser at:

```
http://127.0.0.1:8000/
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
