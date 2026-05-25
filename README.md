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

# Week 1 - Day 4 JSON Mastery + API Calling

## Topics Covered

- JSON module
- json.dumps() and json.loads()
- Reading and writing JSON files
- Nested JSON handling
- Query parameters
- Headers and API keys
- Error handling in API calls
- Robust API calling patterns

---

# 1. JSON Module

Python provides a built-in `json` module for working with JSON data.

Used for:
- APIs
- configuration files
- backend communication
- storing structured data

Import:

```python
import json
```

---

# 2. json.dumps()

Converts Python object → JSON string.

Example:

```python
import json

data = {
    "name": "Bubble",
    "age": 20
}

json_string = json.dumps(data)

print(json_string)
```

---

# 3. json.loads()

Converts JSON string → Python object.

Example:

```python
import json

json_data = '{"name":"Bubble"}'

data = json.loads(json_data)

print(data)
```

---

# 4. Reading and Writing JSON Files

Writing JSON:

```python
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
```

Reading JSON:

```python
with open("data.json", "r") as file:
    data = json.load(file)
```

---

# 5. Nested JSON

Real APIs return deeply nested JSON.

Example:

```json
{
  "user": {
    "name": "Bubble",
    "address": {
      "city": "Pune"
    }
  }
}
```

Accessing nested data:

```python
data["user"]["address"]["city"]
```

---

# 6. Safe Dictionary Access

Using `.get()` prevents crashes.

Unsafe:

```python
data["phone"]
```

Safer:

```python
data.get("phone")
```

---

# 7. Query Parameters

Query parameters filter/search API data.

Example URL:

```text
/users?city=Pune
```

Using query params with requests:

```python
params = {
    "city": "Pune"
}

requests.get(url, params=params)
```

---

# 8. Headers and API Keys

Headers send extra request information.

Example:

```python
headers = {
    "Authorization": "Bearer token"
}
```

API keys help authenticate requests.

---

# 9. Error Handling in API Calls

Backend systems must safely handle:
- timeouts
- network failures
- invalid responses
- HTTP errors

Example:

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Request timed out")
```

---

# 10. Robust API Calling Pattern

Professional backend flow:

```text
Call API
↓
Check status
↓
Handle errors
↓
Parse JSON
↓
Return structured response
```

---

# 11. Mini VitalGuard Weather Integration

Built a mini system that:
- fetched weather data from API
- calculated health risk
- saved results into JSON file
- generated structured summaries

Concepts practiced:
- API calling
- JSON persistence
- risk calculation
- file handling
- structured backend responses

---

# Important Learnings

- APIs may fail unexpectedly
- JSON structure must stay consistent
- `.get()` is safer than direct dictionary access
- Query parameters customize API responses
- Backend systems should never crash on bad responses

---

# Files Created

```text
day4/
├── 01_json_basics.py
├── 02_nested_json.py
├── 03_api_calls.py
├── 04_headers_and_keys.py
├── 05_final_challenge.py
```

---

# Progress

Completed Day 4 JSON and API fundamentals successfully 🚀

# Week 1 - Day 5 Backend Integration + Final Practice

## Topics Covered

- Combining multiple backend concepts
- API integration
- Risk calculation logic
- JSON persistence
- Structured backend responses
- File handling
- Debugging backend systems

---

# 1. Combining Backend Concepts

Day 5 focused on integrating everything learned so far:

- HTTP
- REST APIs
- JSON
- Type hints
- Decorators
- Exception handling
- API requests
- File persistence

---

# 2. Weather API Integration

Used Open-Meteo API to:
- fetch live weather data
- access nested JSON safely
- handle API failures gracefully

Example API request:

```python
requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 18.52,
        "longitude": 73.85
    }
)
```

---

# 3. Risk Calculation System

Built custom backend logic to calculate risk based on:
- heart rate
- sleep hours
- temperature
- humidity
- activity level

Example:

```python
if heart_rate > 100:
    risk_factors.append("elevated heart rate")
```

---

# 4. Structured Backend Responses

Returned organized backend-style dictionaries.

Example:

```python
{
    "risk_level": "high",
    "risk_score": 8
}
```

---

# 5. JSON Persistence

Stored results into:

```text
risk_log.json
```

Concepts practiced:
- reading files
- writing files
- appending records
- persistent storage

---

# 6. Backend Debugging

Debugged multiple realistic backend issues:

- KeyError
- JSONDecodeError
- inconsistent key names
- missing values
- NoneType comparison errors

Important lesson:

```text
Consistent JSON structure is critical in backend systems.
```

---

# 7. Safe API Handling

Learned to safely handle:
- failed requests
- missing fields
- network errors
- invalid responses

Used:
- `.get()`
- `try-except`
- fallback values

---

# 8. Important Backend Concepts Learned

## Backend systems should:
- validate all input
- handle API failures safely
- return structured responses
- persist important data
- avoid crashes

---

# 9. Files Created

```text
day5/
├── 01_weather_api.py
├── 02_risk_calculation.py
├── 03_json_storage.py
├── 04_debugging_practice.py
├── 05_final_challenge.py
```

---

# 10. Biggest Learnings

- Backend engineering is heavily pattern-based
- Debugging is a major developer skill
- APIs often return unpredictable data
- Understanding logic matters more than memorizing syntax
- Real projects are built step-by-step through practice

---

# Progress

Completed Week 1 backend fundamentals successfully 🚀
Built first mini backend-style VitalGuard prototype.