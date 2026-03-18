"""
logic/advisory.py

Contains all agricultural intelligence logic:
- Pest & disease risk analysis
- Fertilizer recommendation
- Advisory generation
- Farmer-friendly formatting

No UI, no API calls, no model loading.
"""

from typing import Dict, List


# --------------------------------------------------
# Utility
# --------------------------------------------------

def similarity_score(a: str, b: str) -> float:
    """Simple similarity score between two strings (0–1)."""
    a, b = a.lower(), b.lower()
    matches = sum(1 for ch in a if ch in b)
    return matches / max(len(a), len(b), 1)


# --------------------------------------------------
# Pest & Disease Risk
# --------------------------------------------------

def check_pest_risk(weather: Dict, crop: str) -> List[str]:
    """
    Estimate pest/disease risk based on weather patterns.
    """
    risks = []

    temp = weather.get("temperature", 0)
    humidity = weather.get("humidity", 0)
    rainfall = weather.get("rainfall", 0)

    if humidity > 70 and temp > 25:
        risks.append("High fungal disease risk")

    if rainfall > 20:
        risks.append("Increased pest infestation risk")

    if temp > 35:
        risks.append("Heat stress risk for crop")

    if not risks:
        risks.append("Low pest and disease risk")

    return risks


# --------------------------------------------------
# Fertilizer Recommendation
# --------------------------------------------------

def recommend_fertilizers(soil_type: str, crop: str) -> Dict[str, str]:
    """
    Rule-based fertilizer recommendation.
    """

    soil_type = soil_type.lower()
    crop = crop.lower()

    recommendations = {
        "nitrogen": "Urea",
        "phosphorus": "DAP",
        "potassium": "MOP"
    }

    if soil_type in ["sandy", "sandy loam"]:
        recommendations["organic"] = "Compost / FYM"

    if soil_type in ["clay", "clayey"]:
        recommendations["micronutrients"] = "Zinc + Boron"

    if crop in ["rice", "paddy"]:
        recommendations["nitrogen"] = "Neem-coated Urea"

    if crop in ["wheat", "maize"]:
        recommendations["potassium"] = "Sulphate of Potash"

    return recommendations


# --------------------------------------------------
# Advisory Generation
# --------------------------------------------------

def generate_advisory(
    crop: str,
    soil_type: str,
    weather: Dict,
    yield_prediction: float | None = None
) -> Dict:
    """
    Generate a complete advisory object.
    """

    pest_risks = check_pest_risk(weather, crop)
    fertilizers = recommend_fertilizers(soil_type, crop)

    advisory = {
        "crop": crop,
        "soil_type": soil_type,
        "pest_risk": pest_risks,
        "fertilizers": fertilizers,
        "irrigation_advice": irrigation_advice(weather),
    }

    if yield_prediction is not None:
        advisory["yield_estimate"] = round(yield_prediction, 2)

    return advisory


# --------------------------------------------------
# Irrigation Advice
# --------------------------------------------------

def irrigation_advice(weather: Dict) -> str:
    """
    Simple irrigation recommendation.
    """
    rainfall = weather.get("rainfall", 0)
    temp = weather.get("temperature", 0)

    if rainfall > 25:
        return "Avoid irrigation due to sufficient rainfall"

    if temp > 32:
        return "Increase irrigation frequency"

    return "Maintain regular irrigation schedule"


# --------------------------------------------------
# Farmer-Friendly Output
# --------------------------------------------------

def farmer_friendly_output(advisory: Dict) -> str:
    """
    Convert advisory dictionary into readable text.
    """

    lines = []

    lines.append(f"🌾 Crop: {advisory['crop'].title()}")
    lines.append(f"🌱 Soil Type: {advisory['soil_type'].title()}")

    if "yield_estimate" in advisory:
        lines.append(f"📊 Expected Yield: {advisory['yield_estimate']} tons/hectare")

    lines.append("\n🐛 Pest & Disease Risk:")
    for risk in advisory["pest_risk"]:
        lines.append(f"  • {risk}")

    lines.append("\n🧪 Fertilizer Recommendation:")
    for nutrient, fert in advisory["fertilizers"].items():
        lines.append(f"  • {nutrient.title()}: {fert}")

    lines.append(f"\n💧 Irrigation Advice: {advisory['irrigation_advice']}")

    return "\n".join(lines)