# services/location_service.py

import requests

# -----------------------------
# IP-based location detection
# -----------------------------
def get_ip_location():
    """
    Detect user's approximate location using IP.
    Returns: (lat, lon, city) or (None, None, None)
    """
    try:
        response = requests.get("https://ipapi.co/json/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return (
                data.get("latitude"),
                data.get("longitude"),
                data.get("city")
            )
    except Exception:
        pass

    return None, None, None


# -----------------------------
# Reverse geocoding (lat/lon → city)
# -----------------------------
def get_city_from_coords(lat, lon):
    """
    Convert latitude & longitude to city name using OpenStreetMap.
    """
    try:
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {
            "lat": lat,
            "lon": lon,
            "format": "json"
        }
        headers = {"User-Agent": "FarmSmart-App"}

        response = requests.get(url, params=params, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            address = data.get("address", {})
            return (
                address.get("city")
                or address.get("town")
                or address.get("village")
                or address.get("state")
            )
    except Exception:
        pass

    return None


# -----------------------------
# Forward geocoding (place → lat/lon)
# -----------------------------
def geocode_manual_input(place):
    """
    Convert a manually entered place name into (lat, lon, city).
    """
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": place,
            "format": "json",
            "limit": 1
        }
        headers = {"User-Agent": "FarmSmart-App"}

        response = requests.get(url, params=params, headers=headers, timeout=5)
        if response.status_code == 200:
            results = response.json()
            if results:
                lat = float(results[0]["lat"])
                lon = float(results[0]["lon"])
                city = results[0].get("display_name", "").split(",")[0]
                return lat, lon, city
    except Exception:
        pass

    return None, None, None