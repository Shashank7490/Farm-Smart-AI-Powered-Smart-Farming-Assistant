"""
settings.py
------------
Central configuration for the application.
"""

# -------------------------
# App
# -------------------------
APP_NAME = "Farm Smart"
DEFAULT_LANGUAGE = "en"

SUPPORTED_LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Telugu": "te"
}

# -------------------------
# APIs
# -------------------------
OPENWEATHER_API_KEY = "YOUR_API_KEY_HERE"
WEATHER_UNITS = "metric"

# -------------------------
# Models
# -------------------------
SOIL_MODEL_PATH = "models/weights/soil_resnet.pt"
YIELD_MODEL_PATH = "models/weights/yield_model.pkl"
FERTILIZER_MODEL_PATH = "models/weights/fertilizer_model.pkl"

# -------------------------
# Thresholds / Rules
# -------------------------
PEST_RISK_TEMP = 30
PEST_RISK_HUMIDITY = 70