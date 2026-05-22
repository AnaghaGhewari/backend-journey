#Open-Meteo is a completely free weather API - no api key, no signup, we just need to call it.

import requests

def get_pune_weather() -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude" :18.52,
        "longitude": 73.85,
        "current":"tempreature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Asia/Kolkata"

    }

    try:
        r = requests.get(url,params, timeout=5)
        r.raise_for_status()
        data = r.json()

        current = data.get("current",{})

        return{
            "temp_c":current.get("tempreature_2m"),
            "humidity":current.get("relative_humidity_2m"),
            "wind_kmh": current.get("wind_speed_10m")

        }
    except Exception as e:
        return{"error": str(e)}
weather = get_pune_weather()
print(weather)

