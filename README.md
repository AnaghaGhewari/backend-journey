# Backend Journey 🚀

Learning backend development using Python and FastAPI.

## Week 1 - HTTP Fundamentals

### Topics Learned
- Client vs Server
- HTTP Requests and Responses
- GET, POST, PUT, DELETE
- Status Codes
- Headers

✅ Day 1 Started
# HTTP Practice Questions

## 1. What is HTTP?
HTTP is a communication protocol used between client and server.

---

## 2. Difference between client and server?

Client requests data.
Server processes request and sends response.

---

## 3. Difference between GET and POST?

GET is used to fetch data.

POST is used to send/create data.

---

## 4. Difference between 401 and 403?

401:
User is not authenticated.

403:
User is authenticated but not allowed.

---

## 5. What is JSON?

JSON is a lightweight data format used in APIs.

Example:

```json
{
  "name": "Raj",
  "age": 20
}
```

---

## 6. What is an endpoint?

An endpoint is a specific route/path on a backend server.

Example:

```text
/users
/login
/products
```

---

## 7. Request-Response Cycle

```text
Client -----> Request -----> Server
Client <----- Response <---- Server
```

# Week 1 - Day 2 REST APIs

## What is REST?

REST stands for Representational State Transfer.

REST APIs:
- use HTTP
- use endpoints
- use JSON
- are stateless

---

## REST Principles

- Client-server architecture
- Stateless communication
- Resource-based URLs
- Uniform interface

---

## Good Endpoint Design

GET /users/5

POST /users

DELETE /users/5

---

## Bad Endpoint Design

GET /getUser?id=5

POST /deleteUser

---

## JSON Example

```json
{
  "user": {
    "name": "Raj",
    "age": 20
  },
  "skills": ["Python", "FastAPI"]
}
```

---

## Important Understanding

URL should represent nouns/resources.

HTTP method should represent action.

# Week 1 - Day 3 Python for Backend

## Topics Covered

- Virtual Environments
- Type Hints
- Decorators
- Exception Handling
- Dictionaries and Lists
- Backend-style Validation

---

# 1. Virtual Environments

A virtual environment isolates project dependencies.

Why it is important:
- prevents package conflicts
- keeps projects organized
- used in professional backend development

Commands used:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

---

# 2. Type Hints

Type hints specify expected data types.

Example:

```python
def calculate_risk(
    heart_rate: int,
    sleep_hours: float
) -> dict:
```

Benefits:
- improves readability
- helps validation
- heavily used in FastAPI
- reduces bugs

---

# 3. Decorators

Decorators wrap functions and add extra behavior.

Example:

```python
@app.get("/users")
```

FastAPI uses decorators to register API routes.

Custom decorator example:

```python
@log_time
def predict_risk():
```

This decorator measured execution time.

---

# 4. Exception Handling

Exception handling prevents backend crashes.

Example:

```python
try:
    value = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Backend systems use exception handling to:
- validate input
- handle runtime errors
- return safe responses

---

# 5. Dictionaries and Lists

Dictionaries store key-value pairs.

Example:

```python
{
    "risk": "high"
}
```

Lists store multiple values.

Example:

```python
[89, 90, 95]
```

These structures are heavily used in APIs.

---

# 6. Backend Validation Logic

Created a validation function for:
- heart rate
- sleep hours
- step count

Validation checks:
- heart rate range
- sleep range
- negative steps

Returned structured backend-style responses.

Example response:

```python
{
    "valid": False,
    "errors": [
        "heart_rate must be between 30 and 220"
    ]
}
```

---

# Important Learnings

- FastAPI relies heavily on type hints and decorators
- Backend systems validate all user input
- Exception handling is critical for stable APIs
- Virtual environments are standard backend practice
- Dictionaries are commonly returned as JSON responses

---

# Files Created

```text
day3/
├── 01_type_hints.py
├── 02_decorators.py
├── 03_exceptionalhandling.py
└── 04_final_practice.py
```

---

# Progress

Completed Day 3 backend Python fundamentals successfully 🚀