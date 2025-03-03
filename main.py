import streamlit as st
from PIL import Image
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        max-width: 800px;
        margin: 0 auto;
    }
    .stSelectbox {
        margin-bottom: 1rem;
        background-color: #f8f9fa;
        border-radius: 8px;
    }
    .result-container {
        background: linear-gradient(135deg, #6B73FF 0%, #000DFF 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        text-align: center;
    }
    h1 {
        background: linear-gradient(120deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3rem !important;
        margin-bottom: 2rem !important;
    }
    .stButton button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .category-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    .stNumberInput {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🌈 Unit Converter")
st.markdown("Convert between different units ✨")

# Create conversion categories
conversion_categories = {
    "Length": {
        "units": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "factors": {
            "Meters": 1,
            "Kilometers": 0.001,
            "Miles": 0.000621371,
            "Feet": 3.28084,
            "Inches": 39.3701
        }
    },
    "Weight": {
        "units": ["Kilograms", "Grams", "Pounds", "Ounces"],
        "factors": {
            "Kilograms": 1,
            "Grams": 1000,
            "Pounds": 2.20462,
            "Ounces": 35.274
        }
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"],
    }
}

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Select Category", list(conversion_categories.keys()))

# Get units for selected category
units = conversion_categories[category]["units"]

with col1:
    from_unit = st.selectbox("From Unit", units)
with col2:
    to_unit = st.selectbox("To Unit", units)

# Input value
value = st.number_input("Enter Value", value=0.0)

# Conversion logic
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return ((value - 32) * 5/9) + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return ((value - 273.15) * 9/5) + 32
        else:
            return value
    else:
        # For Length and Weight
        factors = conversion_categories[category]["factors"]
        base_value = value / factors[from_unit]
        return base_value * factors[to_unit]

# Calculate result
result = convert_units(value, from_unit, to_unit, category)

# Display result in a nice container with animation
st.markdown("<div class='result-container'>", unsafe_allow_html=True)
st.markdown(f"### ✨ Result")
st.markdown(f"## {value:,.2f} {from_unit}")
st.markdown(f"### = ")
st.markdown(f"## {result:,.2f} {to_unit}")
st.markdown("</div>", unsafe_allow_html=True)

# Add some helpful information with better styling
with st.expander("💡 Quick Guide"):
    st.markdown("""
    <div style='background: #f8f9fa; padding: 1rem; border-radius: 8px;'>
    <h4>How to use this converter:</h4>
    
    1. 📊 Select your conversion category
    2. 🔄 Choose your units (from/to)
    3. 📝 Enter your value
    4. ✨ Get instant results!
    </div>
    """, unsafe_allow_html=True)

# Footer with gradient
st.markdown("---")
st.markdown("""
    <div style='text-align: center; background: linear-gradient(45deg, #FF6B6B22, #4ECDC422); 
                padding: 1rem; border-radius: 10px;'>
        Made with 💖 Shazia Samma<br>
        <a href='https://github.com/Shaziasama' target='_blank'>
            <img src='https://img.shields.io/badge/GitHub-View_Project-blue?style=for-the-badge&logo=github' alt='GitHub'/>
        </a>
    </div>
""", unsafe_allow_html=True) 