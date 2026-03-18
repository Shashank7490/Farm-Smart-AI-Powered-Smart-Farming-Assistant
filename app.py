import streamlit as st

from config.settings import APP_NAME
from services.weather_service import get_weather
from services.location_service import get_ip_location
from models.soil_model import predict_soil_type_from_pil
from models.yield_model import predict_yield
from ui.components import render_gauge
from ui.navigation import render_back_button


def main():
    st.set_page_config(page_title=APP_NAME, layout="wide")
    st.title(APP_NAME)

    render_back_button()

    # Example flow
    city = get_ip_location()
    weather = get_weather(city)

    st.subheader("Current Weather")
    render_gauge("Temperature", weather["temp"], 0, 50)
    render_gauge("Humidity", weather["humidity"], 0, 100)

    # Placeholder for model usage
    # yield_value = predict_yield([...])
    # st.metric("Expected Yield", f"{yield_value:.2f} tons/ha")


if __name__ == "__main__":
    main()