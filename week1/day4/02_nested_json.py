#Real API responses are never flat. They look like this — nested dicts inside lists inside dicts. You need to navigate them safely or your code crashes on missing keys.
response = {
    "status":"ok",
    "data": {
        "users":{
            "id":1,
            "name":"Mohit",
            "vitals":[
                {type: "heart_rate","value": 88,"unit":"bpm"},
                {type: "sleep","value":5.22,"unit":"hours"}
            ]
        },
        "risk":{
            "score": 0.73,
            "level":"high",
            "factors":["low_sleep","elevated_hr"]
        }
    }
}

#Access nested values

name = response["data"]["users"]["name"]
risk_score = response["data"]["risk"]["score"]
first_hr = response["data"]["users"]["vitals"][0]["value"]
factors = response ["data"]["risk"]["factors"]

print(name,risk_score,first_hr,factors)

#this access methon may lead to crash or missing  a key

#Safe Access with GET() - Never crashes or gives missing keys

#UNSAFE CRASHES IF THE KEY DOESN'T EXIST
score = response["data"]["risk"]["score"]

#SAFE - RETURNS NONE OR ADEFAULT IF THE KEY IS MISSING

score = response.get("data", {}).\
                 get("risk", {}).\
                 get("score", 0.0)   # returns 0.0 if missing
        


#Even safer wrap it in try/except for deeply nested access
try:
    hr = response["data"]["users"]["vitals"][0]["value"]
except (KeyError, IndexError, TypeError):
    hr = None
    print("Heart rate not found in response")

#Loop Through Nested Lists - Getting all vital values

vitals = ["data"]["user"]["vitals"]

for vital in vitals:
    print(f"{vital['type']}: {vital['value']} {vital['unit']}")
hr_readings = [v for v in vitals if v["type"]=="heart_rate"] 
print(hr_readings)        