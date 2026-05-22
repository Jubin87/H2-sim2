import streamlit as st
import CoolProp.CoolProp as CP

st.title("Hydrogen Refueling Simulator")
st.subheader("Cloud Deployment Test")

# Inputs for the simulation
pressure_bar = st.slider("Storage/Dispenser Pressure (bar)", 100, 700, 350)
temp_c = st.slider("Pre-cooling Temperature (°C)", -40, 20, -40)

# Convert to SI units for CoolProp
P = pressure_bar * 100000  # bar to Pa
T = temp_c + 273.15        # °C to K

try:
    # Calculate density (D) using real-gas properties of Hydrogen
    density = CP.PropsSI('D', 'P', P, 'T', T, 'Hydrogen')
    st.metric(label="Hydrogen Density", value=f"{density:.2f} kg/m³")
except Exception as e:
    st.error(f"Thermodynamic calculation failed: {e}")
