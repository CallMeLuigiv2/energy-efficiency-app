
# ⚡ Energy Efficiency Predictor

## 📌 Overview
An End-to-End Machine Learning application that predicts the Heating and Cooling loads of a building based on its geometry (Surface Area, Height, etc.).
**Goal:** Help architects design energy-efficient buildings before construction begins.

## 🛠️ Tech Stack
* **Language:** Python
* **ML Library:** Scikit-Learn (K-Nearest Neighbors Regressor)
* **Web Framework:** Streamlit
* **Data Processing:** Pandas & NumPy

## 📊 Key Results
* **Model Accuracy:** ~94% R² Score
* **Key Insight:** Features like *Overall Height* and *Relative Compactness* had the strongest correlation with energy usage.

## 🚀 How to Run Locally
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`