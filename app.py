import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Set page title
st.title("BMI Calculator")

# Add description
st.write("Calculate your Body Mass Index (BMI) by entering your weight and height below.")

# Create input fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=500.0, value=70.0)
height = st.number_input("Enter your height (m)", min_value=0.1, max_value=3.0, value=1.70)

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    bmi_status = get_bmi_status(bmi)
    
    # Display results
    st.write(f"Your BMI is: {bmi:.2f}")
    st.write(f"Status: {bmi_status}")
    
    # Add a color-coded status indicator
    if bmi_status == "Normal weight":
        st.success(f"Your BMI indicates you are at a {bmi_status.lower()}")
    elif bmi_status == "Underweight":
        st.warning(f"Your BMI indicates you are {bmi_status.lower()}")
    else:
        st.error(f"Your BMI indicates you are {bmi_status.lower()}")

