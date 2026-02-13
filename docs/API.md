# API Documentation

The application provides a REST API endpoint for making predictions programmatically.

What is API Documentation?
API = Application Programming Interface. In our Django project, this refers to documenting:

The endpoints/routes our application provides
How to interact with them (what data to send, what to expect back)
This helps other developers use our system programmatically

---

## Overview

This Django application provides the following endpoints:

---

## Base URL

`http://127.0.0.1:8000/` for local

---

## Endpoints

### 1. Prediction Endpoint

**URL:** `/predict/`
**Method:** POST
**Content-Type:** application/x-www-form-urlencoded or multipart/form-data
**Request Parameters:**
{
    "name": "string",
    "sex": "male" or "female",
    "age": "number",
    "pclass": "1st" or "2nd" or "3rd",
    "parch": "number (0+)",
    "embarked": "C, Q, or S",
    "fare": "number",
    "sibsp": "number (0-10)",
}
**Response:**
Code: 200
Content:
{
    "survived": true,
    "prediction": "Survived" or "Did not survive",
    "probability": 0.85,
}
**Error Response:**
Code: 400(Bad Request) - Invalid input data
Content:
{
    "error": "Invalid value for sex. Must be 'male' or 'female'."
}

---

### 2. History Endpoint

**URL:** `/history/`
**Method:** GET
**Returns:** List of all stored predictions result, probability, timestamp

---

## Error Responses

All endpoints return standard HTTP status codes:

- 200: Success
- 400: Bad Request (invalid input)
- 500: Server Error

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