#JSON MODULES FOR PYTHON

import json
from datetime import datetime

#JSON is just a string — a piece of text formatted in a specific way. Python's json module converts between that string and Python dicts/lists. That's all it does.
#json.dumps() - Python dict ->JSON string 

data = {
    "name":"Anushka",
    "heart_rate":88,
    "active": True
}

json_data = json.dumps(data)

print(json_data)
print(type(json_data))

#json.loads() - JSON strings -> Python dict/lists

back_to_json = json.loads(json_data)
print(type(back_to_json))
print(back_to_json["name"])

print(json.dumps(data, indent = 4))




#READING AND WRITING TO THE JSON FILES

vital_log = {
    "user_id":1,
    "heart_rate":88,
    "sleep_hrs":6.22,
    "steps":9000,
    "logged_at":datetime.now().isoformat()
}


#Write to the json
with open("vital.json","w") as f:
    json.dump(vital_log,f,indent =4 )

#Read to the json
with open("vital.json", "r") as f:
    loaded = json.load(f)
    print(loaded["heart_rate"])   


    

#Saving multiple records — a list of vitals

import json, os

def save_vital(new_entry: dict, filepath: str = "vitals_log.json"):
    # Load existing data if file exists
    if os.path.exists(filepath):
        with open(filepath) as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(new_entry)

    with open(filepath, "w") as f:
        json.dump(logs, f, indent=2)
    print(f"Saved. Total records: {len(logs)}")

save_vital({"heart_rate": 88, "sleep_hours": 5.5})
save_vital({"heart_rate": 72, "sleep_hours": 7.0})