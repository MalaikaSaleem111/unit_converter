import streamlit as st
st.set_page_config(page_title="Unit Converter", layout="centered")


st.title("Unit Converter")
st.write("Welcome to the Unit Converter! Select the units and enter a value to convert.")

# Select conversion category
conversion_type = st.selectbox("Choose a conversion type:",["Lenght", "Weight", "Time", "Temperature", "Frequency"] )

# define conversion
def convert_lenght(value, from_unit, to_unit):
    conversion_factor = {
        "Meter": 1,
        "Kilometer":0.001,
        "Miles": 0.000621371,
        "Foot": 3.28084
    }
    return value * (conversion_factor[to_unit])/ conversion_factor[from_unit]
def convert_time(value, from_unit, to_unit):
    conversion_factor = {
        "Seconds": 1,
        "Minutes": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400
    }
    return value * (conversion_factor[to_unit])/ conversion_factor[from_unit]
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.206244202,
        "Ounce": 35.273990723
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_temperature(value, from_unit, to_unit):
    conversion_factors = {
        "Celsius": 1,
        "Kelvin": 274.15,
        "Fahrenheit": 33.8
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_frequency(value, from_unit, to_unit):
    conversion_factors = {
        "Hertz": 1,
        "Kilohertz": 0.001,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])
# select unit based on conversion type
if conversion_type == "Lenght":
    units = ["Meter", "Kilometer", "Miles", "Foot"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    if st.button("Convert"):
        result = convert_lenght(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

elif conversion_type == "Time":
    units = ["Seconds", "Minutes", "Hour", "Day"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    if st.button("Convert"):
        result = convert_time(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Kelvin", "Fahrenheit"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Frequency":
    units = ["Hertz", "Kilohertz", "Megahertz","Gigahertz"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    if st.button("Convert"):
        result = convert_frequency(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

