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