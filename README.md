# 🏨 hotel_project_jenkins

A Django REST Framework project for managing users and hotel orders, with Jenkins CI integration for testing using `pytest`, `pytest-django`, and `pytest-cov`.

---

## 🚀 Features

- Custom `User` model with UUID primary key
- Order model linked to User
- Full CRUD API for users and orders
- Class-based ViewSets and Serializers
- REST endpoints via Django REST Framework
- Automated testing pipeline with Jenkins + `pytest`

---

## 🧪 Run Tests Manually

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate virtualenv
Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run tests

```bash
pytest --cov=hotel --cov-report=html
```

---

## 🛠 Project Structure

```bash
hotel_project/
├── hotel/                 
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests/
├── hotel_project/
│   ├── settings.py
│   ├── urls.py
│   └── test_settings.py
├── requirements.txt
├── conftest.py
├── pytest.ini
└── Jenkinsfile
```

---

## ⚙️ Jenkins CI Setup

Prerequisites
- Jenkins installed
- Python + pip installed on agent
- Git repo connected to Jenkins

---

## ⚙️ API Endpoints

| Method | Endpoint             | Description  |
| ------ | -------------------- | ------------ |
| GET    | `/api/users/`        | List users   |
| POST   | `/api/users/`        | Create user  |
| PUT    | `/api/users/<uuid>/` | Update user  |
| DELETE | `/api/users/<uuid>/` | Delete user  |
| GET    | `/api/orders/`       | List orders  |
| POST   | `/api/orders/`       | Create order |
| PUT    | `/api/orders/<uuid>` | Update order |
| DELETE | `/api/orders/<uuid>` | Delete order |

---

## ✅ Tech Stack

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Pytest
- Jenkins
- python-decouple

---