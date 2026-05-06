# ================================================================
# WEATHER TOOL
# Each tool file has TWO things:
# 1. SCHEMA  - tells LLM what this tool does
# 2. FUNCTION - actual Python code that runs
# ================================================================

import requests
from config.settings import WEATHER_API_KEY


# ── PART 1: SCHEMA (What LLM sees) ──────────────────────────────
SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for any city. Use when user asks about weather, temperature, rain, conditions.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name e.g. London, Berlin, New York, Paris"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Temperature unit. Default celsius for UK/EU"
                }
            },
            "required": ["city"]
        }
    }
}


# ── PART 2: FUNCTION (What actually runs) ───────────────────────
def get_weather(city: str, unit: str = "celsius") -> dict:
    """
    Gets weather for a city
    Production: replace mock with real OpenWeatherMap API
    """
    
    # ── REAL API CALL (uncomment for production) ─────────────
    # response = requests.get(
    #     "https://api.openweathermap.org/data/2.5/weather",
    #     params={
    #         "q": city,
    #         "appid": WEATHER_API_KEY,
    #         "units": "metric" if unit == "celsius" else "imperial"
    #     }
    # )
    # return response.json()
    
    # ── MOCK DATA (for development) ──────────────────────────
    mock_data = {
        "London":   {"temp": 12, "condition": "Rainy",  "humidity": 85, "wind": "15km/h"},
        "Berlin":   {"temp": 8,  "condition": "Cloudy", "humidity": 72, "wind": "10km/h"},
        "New York": {"temp": 18, "condition": "Sunny",  "humidity": 60, "wind": "20km/h"},
        "Paris":    {"temp": 10, "condition": "Foggy",  "humidity": 90, "wind": "5km/h"},
    }
    
    result = mock_data.get(city, {"error": f"City '{city}' not found"})
    result["unit"] = unit
    result["city"] = city
    return result