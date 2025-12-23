import streamlit as st
import pandas as pd

st.title("Energy Efficiency App")

st.info("This is an app that takes 8 input features, Relative_Compactness - Surface_Area - Wall_Area - Roof_Area - Overall_Height - " \
"Orientation - Glazing_Area - Glazing_Area_Distribution. To determine the Heating Load and Cooling Load")

with st.expander("Data"):
    st.write("**Cleaned dataset used**")

    energy_df = pd.read_csv("C:\energy-efficiency-app\cleaned_energy_data.csv")
    energy_df
    
    st.write("**X Features**")
    x = energy_df.drop(columns=["Heating_Load","Cooling_Load"])
    x

    st.write("**Y Targets**")
    y = energy_df[["Heating_Load","Cooling_Load"]]
    y

with st.expander("Visulizations"):
    st.write("**HeatMap**")
    st.subheader("The user can see which features are more Correlated to the Target Variables")
    st.image("C:\energy-efficiency-app\Pictures\Heat_map_Energyapp.png")

    st.write("**Cooling Load Distribution**")
    st.subheader("Show how often certain values appear for the Cooling Load")
    st.image("C:\energy-efficiency-app\Pictures\Cooling_Load_Distribution.png")

    st.write("**Heating Load Distribution**")
    st.subheader("Show how often certain values appear for the Heating Load")
    st.image("C:\energy-efficiency-app\Pictures\Heating_Load_Distribution.png")


with st.sidebar:
    st.header("Input Features")

    st.write("Relative_Compactness Feature Configuration")
    relative_compactness = st.slider("Range for Relative_Compactness",0.62, 0.98)
    rc_input = st.number_input("Relative_Compactness",0.00,1.00)

    st.write(" Surface_Area Feature Configuration")
    surface_area =  st.slider("Range for Surface_Area",514.5,808.5)
    sa_input = st.number_input("Surface_Area", 0.00, 1000.00)
    
    st.write("Wall_Area Feature Configuration")
    wall_area = st.slider("Range for Wall_Area",245.0, 416.5)
    wa_input = st.number_input("Wall_Area", 0.00,500.00)
    
    st.write("")