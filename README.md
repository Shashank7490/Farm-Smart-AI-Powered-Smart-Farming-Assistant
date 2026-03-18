# Farm-Smart-AI-Powered-Smart-Farming-Assistant
An end-to-end precision agriculture platform that helps Indian farmers make data-driven decisions on crop selection, fertilizer use, weather risk, and IoT hardware management — in their own language.

Overview

Farm Smart is a multilingual Streamlit web application designed for Indian farmers. It integrates machine learning models, real-time weather APIs, CNN-based soil analysis, OCR document parsing, and IoT hardware management into a single unified dashboard. The platform was built with simplicity and accessibility at its core. Every design decision — from the UI layout to the underlying architecture — was made with a non-technical farming audience in mind. All ML models run locally on-device with no dependency on paid cloud APIs or external ML platforms, keeping the tool lightweight, affordable, and functional even in low-connectivity rural environments. The only external calls made are to free, open APIs (Open-Meteo for weather, Nominatim for geocoding) that require no API keys or subscriptions. The platform supports 8 Indian languages and translates every output, alert, and recommendation automatically — so farmers can use it entirely in their own language without any technical knowledge.


Key Features

Crop Recommendation

Two-stage ML pipeline (Random Forest / XGBoost) recommending the best crops based on live soil and weather inputs
Takes NPK values, soil type, temperature, humidity, and rainfall as inputs
Outputs top crop suggestions ranked by predicted yield (kg/ha)

Weather-Based Advisory

Fetches live forecasts and 10-year historical climatology via Open-Meteo API (async)
Generates risk-level advisories: High Rain Risk, Water Stress, Pest Alert, or Favorable
Pest outbreak prediction for crops like Paddy, Wheat, and Cotton based on temperature and humidity thresholds

Fertilizer Recommender

XGBoost-powered fertilizer recommendation with budget filtering
Ranks fertilizers by value-for-money (suitability score / cost per kg)
Farmer-friendly output with plain-language explanations (e.g. "Very cheap", "Good for your soil")

Soil Type Identification

CNN (ResNet-18) model classifies soil type from a photo upload
XGBoost pipeline for tabular soil feature classification
OCR (Tesseract + pdf2image) extracts NPK values directly from soil test report PDFs

Unknown Crop Advisor (Miscellaneous)

Recommends nutrients and fertilizers for crops not in the training set
Uses crop similarity scoring against known profiles (duration, water need, soil type, crop type)
Outputs confidence level and NPK guidance

IoT Hardware Manager

Dashboard to monitor and control Smart Sprinklers, Mist Humidifiers, Soil Moisture Monitors, and Field Cameras
Live Plotly gauge charts for real-time soil moisture readings
Sensor calibration controls

Multilingual Support

Supports English, Hindi, Telugu, Tamil, Kannada, Malayalam, Marathi, and Bengali
Powered by Google Translate (deep-translator) — every alert, label, and recommendation is translated on the fly


Repository Structure

FarmProject/
│
├── app.py                              # Entry point (stable version)
├── appO.py                             # Main Streamlit application
│
├── config/
│   └── settings.py                     # App-wide configuration & constants
│
├── data/
│   ├── Crop_recommendation.csv         # Crop recommendation training data
│   ├── crop_yield.csv                  # Crop yield dataset
│   └── Custom_Crops_yield_Historical_Dataset.csv  # Extended yield history
│
├── logic/
│   ├── advisory.py                     # Weather risk & pest advisory engine
│   └── similarity.py                   # Crop similarity scoring logic
│
├── models/
│   ├── CNNforSoilType.pth              # ResNet-18 soil type classifier (PyTorch)
│   ├── crop_model.pkl                  # Crop recommendation model (v1)
│   ├── crop_model1.pkl                 # Crop recommendation model (v2)
│   ├── crop_recommendation_model.pkl   # Crop recommendation model (primary)
│   ├── crop_recommendation_model1.pkl  # Crop recommendation model (secondary)
│   ├── fertilizer_recommender_xgb.joblib  # XGBoost fertilizer recommender
│   ├── label_encoder.pkl               # Label encoder for soil/crop classes
│   ├── mlp_yield_predictor.pkl         # MLP yield prediction model
│   ├── xgboost_full_pipeline.pkl       # XGBoost soil classification pipeline
│   ├── model_loader.py                 # Centralised model loading utilities
│   ├── soil_model.py                   # Soil model inference logic
│   └── yield_model.py                  # Yield model inference logic
│
├── services/
│   ├── location_service.py             # GPS, IP geolocation & reverse geocoding
│   ├── translation_service.py          # Google Translate integration
│   └── weather_service.py             # Open-Meteo API (live + historical, async)
│
├── ui/
│   ├── components.py                   # Reusable Streamlit UI components
│   └── navigation.py                   # Sidebar & page routing
│
├── utils/
│   └── helpers.py                      # Shared helper functions
│
└── other_necessities/                  # Images and PDFs for testing purposes



ML Models

Model                              Task                                  Framework

Random Forest / XGBoost            Crop recommendation                   Scikit-learn / XGBoost
MLP                                Yield prediction (kg/ha)              PyTorch / Scikit-learn
ResNet-18 (CNN)                    Soil type from image                  PyTorch + torchvision
XGBoost Pipeline                   Tabular soil classification           XGBoost + joblib
XGBoost                            Fertilizer recommendation             XGBoost + joblib
Rule-based engine                  Pest risk advisory                    Custom (temp + humidity thresholds)
Crop similarity scorer             Unknown crop recommendation           Custom (attribute matching)
Tesseract OCR                      NPK extraction from PDF reports       pytesseract + pdf2image


External APIs

API                             Purpose

Open-Meteo Forecast             Live 7-day weather forecast
Open-Meteo Archive              10-year historical climatology (async)
ip-api.com                      IP-based geolocation fallback
Nominatim (OpenStreetMap)       Reverse geocoding & city search
Google Translate                Multilingual output translation



Getting Started

Prerequisites

pip install streamlit numpy pandas requests joblib plotly
pip install torch torchvision
pip install xgboost scikit-learn
pip install deep-translator streamlit-js-eval
pip install aiohttp nest_asyncio
pip install pdf2image pytesseract pillow

#For OCR to work, install Tesseract and Poppler:

# macOS

brew install tesseract poppler

#Running the App

git clone https://github.com/<your-username>/FarmProject.git
cd FarmProject
streamlit run appO.py



Tech Stack

Python 3.10+,
Streamlit,
PyTorch + torchvision,
XGBoost + Scikit-learn,
Plotly,
aiohttp + asyncio,
Tesseract OCR + pdf2image,
deep-translator,
Open-Meteo API,
Nominatim


Supported Languages

English · Hindi · Telugu · Tamil · Kannada · Malayalam · Marathi · Bengali


License

This project is licensed under the MIT License. See LICENSE for details.


Acknowledgements

Open-Meteo for free weather and historical climate data
Tesseract OCR for open-source OCR
PyTorch and torchvision for the CNN pipeline
Streamlit for rapid UI development
