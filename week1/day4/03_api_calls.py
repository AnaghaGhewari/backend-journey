#Production backend code never makes a raw requests.get() without timeout, error handling, and status checks. Learn the right pattern once and always use it.
import requests
import json


def safe_get(url: str,
             params: dict = None) -> dict:
    try:
        response = requests.get(
            url,
            params = params,
            timeout= 5
        )
        response.raise_for_status() #raises on 4XX and 5XX
        return {"ok": True,
                "data":response.json()}
    
    except requests.exceptions.Timeout:
        return{"ok": False,
               "error": "Request timed out"}
    
    except requests.exceptions.HTTPError as e:
        return{"ok": False,
               "error":f"HTTP{e.response.status_code}"}
    
    except requests.exceptions.ConnectionError:
        return{"ok": False,
               "error":"No internet connection"}
    except Exception as e:
        return{"ok": False,
               "error":f"Unexpected:{e}"}
    

# QUERY PARAMETERS -Filtering Results via URL

# Query params go after ? in the URL
# /vitals?date=2025-06-01&limit=10
# requests builds this for you automatically

response = requests.get(
    "http://jsonplaceholder.typicode.com/posts",

    params={
        "userID": 1,
        "_limit":3
    }
)

print(response.url)

print(len(response.json()))


#POST REQUEST - Sending JSON data

new_vitals = {
    "heart_rate": 88,
    "sleep_hours": 5.22,
    "steps":4200
}

response = requests.get(
    "http://jsonplaceholder.typicode.com/posts",
    json=new_vitals,
    timeout=5
)

try:
    data = response.json()
except ValueError:
    print("Response is not valid JSON")    


