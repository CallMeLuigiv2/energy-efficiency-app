import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
import joblib

pipeline = joblib.load("model.pkl")

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
    rc_input = st.number_input("Relative_Compactness",0.62,0.98)

    st.write(" Surface_Area Feature Configuration")
    sa_input = st.number_input("Surface_Area", 514.5,808.5)
    
    st.write("Wall_Area Feature Configuration")
    wa_input = st.number_input("Wall_Area",245.0,416.5)
    
    st.write("Roof_Area Feature Congfiguration")
    ra_input = st.number_input("Roof_Area",110.25,220.5)

    st.write("Overall_Height Feature Congfiguration")
    oh_input = st.number_input("Overall_Height",3.5,7.0)

    st.write("Orientation Feature Congfiguration")
    ori_input = st.number_input("Orientation",2,5)


    st.write("Glazing_Area Feature Congfiguration")
    ga_input = st.number_input("Glazing_Area",0.0,0.4)

    st.write("Glazing_Area_Distribution Feature Congfiguration")
    gad_input = st.number_input("Glazing_Area_Distribution",0,5)


if st.button("Predict Energy Efficiency"):
    
 
    input_data = pd.DataFrame({
        'Relative_Compactness': [rc_input],   
        'Surface_Area': [sa_input],          
        'Wall_Area': [wa_input],
        'Roof_Area': [ra_input],
        'Overall_Height': [oh_input],
        'Orientation': [ori_input],
        'Glazing_Area': [ga_input],
        'Glazing_Area_Distribution': [gad_input]
    })

    prediction = pipeline.predict(input_data)

 
    heating_load = prediction[0][0]
    cooling_load = prediction[0][1]

    
    st.success("Prediction Successful!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Heating Load", value=f"{heating_load:.2f} kWh")
    with col2:
        st.metric(label="Cooling Load", value=f"{cooling_load:.2f} kWh")