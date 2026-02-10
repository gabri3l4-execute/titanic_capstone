# API Documentation


What is API Documentation?
API = Application Programming Interface. In our Django project, this refers to documenting:

The endpoints/routes our application provides
How to interact with them (what data to send, what to expect back)
This helps other developers use our system programmatically


## Overview
This Django application provides the following endpoints:

## Endpoints

### 1. Prediction Endpoint
**URL:** `/predict/`
**Method:** POST
**Content-Type:** application/x-www-form-urlencoded or multipart/form-data

**Request Parameters:**

{
"name": "string (optional)",
"sex": "male" or "female",
"age": "number",
"parch": "number (0+)",
"embarked": "C, Q, or S",
"ticket": "number",
"fare": "number",
"cabin":"A number" "B number" "C number" "D number",
"sibsp": "number (0+)",
}


**Response:**
{
"success": true/false,
"prediction": "Survived" or "Did not survive",
"probability": 0.85,
"message": "Optional message"
}


### 2. History Endpoint
**URL:** `/history/`
**Method:** GET
**Returns:** List of all stored predictions

### 3. Individual Prediction
**URL:** `/history/<id>/`
**Method:** GET
**Returns:** Details of a specific prediction

## Error Responses
All endpoints return standard HTTP status codes:
- 200: Success
- 400: Bad Request (invalid input)
- 500: Server Error




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