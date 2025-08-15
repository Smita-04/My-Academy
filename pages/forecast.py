import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go
import streamlit.components.v1 as components
import time

# Load models
scaler = joblib.load("data/Models/sc.pkl")
model = joblib.load("data/Models/xgboost_regressor_r2_0_92_v1.pkl")

# Page setup
st.set_page_config(page_title="Fashion Demand Forecast", layout="wide")

# Custom Background and Styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #e0c3fc, #8ec5fc);
            font-family: 'Segoe UI', sans-serif;
            color: #3c096c;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #3c096c !important;
        }
        input {
            border-radius: 8px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.title("📈 Fashion Demand Forecast")
st.markdown("Predict fashion demand based on weather and product factors. Enter details below:")

# Input Form
with st.form(key="forecast_form"):
    st.markdown("<h3 style='color:#7b2cbf;'>🔎 Enter Details:</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        date = st.date_input("Date:")
        hour = st.text_input("Hour:", placeholder="")
        temperature = st.text_input("Temperature (°C):", placeholder="")
        humidity = st.text_input("Humidity (%):", placeholder="")
        visibility = st.text_input("Visibility (km):", placeholder="")
        sku = st.text_input("SKU:", placeholder="")
        wind_speed = st.text_input("Wind Speed (km/h):", placeholder="")

    with col2:
        rainfall = st.text_input("Rainfall (mm):", placeholder="")
        snowfall = st.text_input("Snowfall (cm):", placeholder="")
        solar_radiation = st.text_input("Solar Radiation (MJ/m²):", placeholder="")

        st.markdown("### 📅 Select Days:")
        monday = st.checkbox("Monday")
        tuesday = st.checkbox("Tuesday")
        saturday = st.checkbox("Saturday")
        sunday = st.checkbox("Sunday")

    submit_button = st.form_submit_button("🚀 Get Forecast")

# On Submit
if submit_button:
    try:
        features = np.array([
            float(hour),
            float(temperature),
            float(humidity),
            float(wind_speed),
            float(visibility),
            float(solar_radiation),
            float(rainfall),
            float(snowfall),
            float(sku),
            date.day,
            date.month,
            date.year,
            int(monday),
            int(saturday),
            int(sunday),
            int(tuesday)
        ]).reshape(1, -1)

        with st.spinner('🔄 Running Prediction...'):
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)

            scaled_features = scaler.transform(features)
            prediction = model.predict(scaled_features)[0]

        # Popup alert
        components.html("""
        <script>
            alert('✅ Prediction complete! Scroll down to view result 📈');
        </script>
        """)

        st.success(f"🎯 Predicted Demand: {round(prediction, 2)}")

        st.markdown("<a href='#chart-section'>👉 Go to Chart</a>", unsafe_allow_html=True)
        st.markdown("<h2 id='chart-section'>📊 Prediction Visualization</h2>", unsafe_allow_html=True)

        fig = go.Figure(data=[
            go.Bar(name='Predicted Demand', x=["Predicted Demand"], y=[prediction], marker_color='#4cc9f0')
        ])
        fig.update_layout(
            title="Fashion Demand Forecast",
            yaxis_title="Demand",
            plot_bgcolor='#f3e9ff',
            paper_bgcolor='#f3e9ff',
            font=dict(color="#3c096c"),
            height=500,
            transition=dict(duration=700),
        )
        st.plotly_chart(fig, use_container_width=True)

    except ValueError:
        st.error("⚠️ Please enter valid numeric values in all fields.")
