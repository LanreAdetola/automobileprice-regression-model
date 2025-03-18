import streamlit as st
import requests

# ✅ Replace with your actual Azure REST API endpoint
API_URL = st.secrets["azure"]["API_URL"]

# ✅ Replace with your Azure ML API key
API_KEY = st.secrets["azure"]["API_KEY"]

st.title("Car Price Prediction")
st.write("Enter car details to predict the price")

# Input fields
symboling = st.number_input("Symboling", min_value=-3, max_value=3, value=0)
normalized_losses = st.text_input("Normalized Losses (NaN if missing)", value="NaN")
make = st.selectbox("Make", ["alfa-romero", "toyota", "honda", "bmw"])
fuel_type = st.selectbox("Fuel Type", ["gas", "diesel"])
aspiration = st.selectbox("Aspiration", ["std", "turbo"])
num_of_doors = st.selectbox("Number of Doors", ["two", "four"])
body_style = st.selectbox("Body Style", ["convertible", "sedan", "hatchback", "wagon", "hardtop"])
drive_wheels = st.selectbox("Drive Wheels", ["rwd", "fwd", "4wd"])
engine_location = st.selectbox("Engine Location", ["front", "rear"])
wheel_base = st.number_input("Wheel Base", min_value=80.0, max_value=120.0, value=88.6)
length = st.number_input("Length", min_value=140.0, max_value=210.0, value=168.8)
width = st.number_input("Width", min_value=60.0, max_value=80.0, value=64.1)
height = st.number_input("Height", min_value=40.0, max_value=70.0, value=48.8)
curb_weight = st.number_input("Curb Weight", min_value=1000, max_value=5000, value=2548)
engine_type = st.selectbox("Engine Type", ["dohc", "ohc", "l", "ohcf", "ohcv", "rotor"])
num_of_cylinders = st.selectbox("Number of Cylinders", ["two", "three", "four", "five", "six", "eight", "twelve"])
engine_size = st.number_input("Engine Size", min_value=60, max_value=500, value=130)
fuel_system = st.selectbox("Fuel System", ["mpfi", "2bbl", "mfi", "1bbl", "spfi", "idi"])
bore = st.number_input("Bore", min_value=2.0, max_value=4.5, value=3.47)
stroke = st.number_input("Stroke", min_value=2.0, max_value=4.5, value=2.68)
compression_ratio = st.number_input("Compression Ratio", min_value=5.0, max_value=20.0, value=9.0)
horsepower = st.number_input("Horsepower", min_value=50, max_value=500, value=111)
peak_rpm = st.number_input("Peak RPM", min_value=4000, max_value=8000, value=5000)
city_mpg = st.number_input("City MPG", min_value=5, max_value=100, value=21)
highway_mpg = st.number_input("Highway MPG", min_value=5, max_value=100, value=27)

if st.button("Predict Price"):
    # Prepare input data
    input_data = {
    "Inputs": {
        "WebServiceInput0":[
    {
        "symboling": symboling,
        "normalized-losses": None if normalized_losses == "NaN" else float(normalized_losses),
        "make": make,
        "fuel-type": fuel_type,
        "aspiration": aspiration,
        "num-of-doors": num_of_doors,
        "body-style": body_style,
        "drive-wheels": drive_wheels,
        "engine-location": engine_location,
        "wheel-base": wheel_base,
        "length": length,
        "width": width,
        "height": height,
        "curb-weight": curb_weight,
        "engine-type": engine_type,
        "num-of-cylinders": num_of_cylinders,
        "engine-size": engine_size,
        "fuel-system": fuel_system,
        "bore": bore,
        "stroke": stroke,
        "compression-ratio": compression_ratio,
        "horsepower": horsepower,
        "peak-rpm": peak_rpm,
        "city-mpg": city_mpg,
        "highway-mpg": highway_mpg
    }
    ]
    },
    "globalParameters": {}
}
    
    # Set headers with API key
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Send request to Azure ML API
    response = requests.post(API_URL, json=input_data, headers=headers)

    if response.status_code == 200:
        result = response.json()

        predicted_price = result["Results"]["WebServiceOutput0"][0]["predicted_price"]
        st.success(f"Estimated Price: ${predicted_price:,.2f}")