import streamlit as st
import streamlit.components.v1 as components

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        'kilograms': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        return (value * 9/5) + 32 if to_unit == 'Fahrenheit' else value + 273.15
    if from_unit == 'Fahrenheit':
        return (value - 32) * 5/9 if to_unit == 'Celsius' else ((value - 32) * 5/9) + 273.15
    if from_unit == 'Kelvin':
        return value - 273.15 if to_unit == 'Celsius' else ((value - 273.15) * 9/5) + 32

def main():
    st.set_page_config(page_title="Unit Converter App", page_icon="🔄", layout="centered")
    
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }
            .stApp {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            .css-1d391kg { text-align: center; }
            .stButton>button {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                transition: 0.3s;
            }
            .stButton>button:hover {
                background-color: #0056b3;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🔄 Unit Converter App")
    
    category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])
    
    if category == "Length":
        units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches']
        convert_function = length_converter
    elif category == "Weight":
        units = ['kilograms', 'grams', 'pounds', 'ounces']
        convert_function = weight_converter
    else:
        units = ['Celsius', 'Fahrenheit', 'Kelvin']
        convert_function = temperature_converter
    
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        result = convert_function(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")
    
if __name__ == "__main__":
    main()
