import requests
from datetime import datetime, timedelta
import streamlit as st

from config.settings import WEATHER_API_KEY

# -----------------------------
# Base configuration
# -----------------------------
BASE_URL = "https://api.openweathermap.org/data/2.5"
UNITS = "metric"


# -----------------------------
# Current Weather
# -----------------------------
@st.cache_data(show_spinner=False)
def get_weather(city: str) -> dict:
    """
    Fetch current weather conditions for a given city.

    Returns:
        dict with temperature, humidity, rainfall, wind_speed, description
    """
    try:
        url = f"{BASE_URL}/weather"
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": UNITS
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "rainfall": data.get("rain", {}).get("1h", 0.0),
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
        }

    except Exception as e:
        return {
            "error": f"Failed to fetch weather: {e}"
        }


# -----------------------------
# Forecast (Next 5–7 Days)
# -----------------------------
@st.cache_data(show_spinner=False)
def get_weather_forecast(city: str) -> list:
    """
    Fetch 5-day / 3-hour forecast and aggregate it day-wise.

    Returns:
        List of daily summaries
    """
    try:
        url = f"{BASE_URL}/forecast"
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": UNITS
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        daily_data = {}

        for entry in data["list"]:
            date = entry["dt_txt"].split(" ")[0]

            if date not in daily_data:
                daily_data[date] = {
                    "temps": [],
                    "humidity": [],
                    "rainfall": 0.0
                }

            daily_data[date]["temps"].append(entry["main"]["temp"])
            daily_data[date]["humidity"].append(entry["main"]["humidity"])
            daily_data[date]["rainfall"] += entry.get("rain", {}).get("3h", 0.0)

        forecast = []
        for date, values in daily_data.items():
            forecast.append({
                "date": date,
                "avg_temp": sum(values["temps"]) / len(values["temps"]),
                "avg_humidity": sum(values["humidity"]) / len(values["humidity"]),
                "total_rainfall": values["rainfall"]
            })

        return forecast

    except Exception as e:
        return [{"error": f"Failed to fetch forecast: {e}"}]


# -----------------------------
# Weather for a Target Week
# -----------------------------
def get_real_weather_for_target_week(city: str, target_date: datetime) -> dict:
    """
    Estimate weather around a target date using available forecast data.

    If the date is beyond forecast range, uses nearest available day.
    """
    forecast = get_weather_forecast(city)

    if not forecast or "error" in forecast[0]:
        return {"error": "Forecast data unavailable"}

    target_str = target_date.strftime("%Y-%m-%d")

    # Exact match
    for day in forecast:
        if day.get("date") == target_str:
            return day

    # Nearest date fallback
    nearest_day = min(
        forecast,
        key=lambda d: abs(
            datetime.strptime(d["date"], "%Y-%m-%d") - target_date
        )
    )

    return nearest_day