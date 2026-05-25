import requests, json, os
from datetime import datetime
from typing import Optional

# --- Step 1: Fetch weather ---
def get_weather() -> dict:
    try:

        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": 18.52, 
                "longitude":73.85,
                "current": "temperature_2m, relative_humidity_2m",
                "timezone": "Asia/Kolkata"
            },
            timeout=5
        )

        r.raise_for_status()

        c = r.json().get("current",{})

        return{
            "temp_c": c.get("temperature_2m",25.0),
            "humidity": c.get("relative_humidity_2m", 50)
        }
    
    except Exception:
        return {
            "temp_c":25.0,"humidity": 50  #safe fallback

        }
    
#---Step 2 calculate risk 
def calculate_risk(
        heart_rate: int,
        sleep_hours: float,
        temp_c: float,
        humidity: int,
        steps: int,
        notes: Optional[str] = None
) -> dict:
    risk_factors = []
    score = 0

    if heart_rate > 100:
        risk_factors.append("elevated heart rate "); score += 2
    if sleep_hours < 6:
        risk_factors.append("low sleep"); score += 2
    if temp_c > 35:
        risk_factors.append("high tempreature"); score += 2
    if humidity > 80:
        risk_factors.append("high humidity"); score += 2
    if steps < 3000:
        risk_factors.append("Lower activity"); score += 2

    level = "low" if score <= 2 else "medium" if score <=4 else "high"

    return{
        "timestamp":datetime.now().isoformat(),
        "vitals": {
            "heart_rate":heart_rate,
            "sleep_hours": sleep_hours,
            "steps":steps
        },
        "weather": {
            "temp_c": temp_c,
            "humidity": humidity,   
        },
        "risk_level":level,
        "risk_score": score,
        "risk_factors":risk_factors,
        "notes": notes

    }   

#--- Step 3 : Save the results 
def save_result(result: dict, filepath: str = "risk_log.json"):
    logs = []

    if os.path.exists(filepath):
        with open(filepath) as f:
            logs = json.load(f)
    logs.append(result)
    with open(filepath,"w") as f:
        json.dump(logs, f, indent= 2)

#--- Step 4: run it---
weather = get_weather()
result = calculate_risk(
        heart_rate=105,
        sleep_hours=4.5,
        temp_c=weather.get("temp_c"),
        humidity=weather["humidity"],
        steps=2000,
        notes="felt very tired and hot today"
    
)   
save_result(result)

#---Step 5 :read back and print summary ---
with open("risk_log.json","r") as f:
    logs = json.load(f)

    last = logs[-1]

    print(f"\n=== VitalGuard Risk Summary ===")
    print(f"Time:        {last['timestamp']}")
    print(f"Risk level:  {last['risk_level'].upper()}")
    print(f"Risk score:  {last['risk_score']}")
    print(f"Factors:     {', '.join(last['risk_factors'])}")
    print(f"Weather:     {last['weather']['temp_c']}°C, {last['weather']['humidity']}% humidity")


              
