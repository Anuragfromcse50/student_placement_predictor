import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Load trained model and encoders
# -----------------------------
model = joblib.load("backend/placement_model.pkl")
branch_encoder = joblib.load("backend/branch_encoder.pkl")
target_encoder = joblib.load("backend/target_encoder.pkl")


# -----------------------------
# Page settings
# -----------------------------
st.set_page_config(
    page_title="Student Placement Predictor",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Placement Predictor")
st.write("Enter your details to predict your placement.")


# -----------------------------
# Input fields
# -----------------------------
branch = st.selectbox(
    "Select Branch",
    ["CSE", "IT", "ECE", "EE", "ME", "CE"]
)

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

internships = st.number_input(
    "Number of Internships",
    min_value=0,
    value=0,
    step=1
)

projects = st.number_input(
    "Number of Projects",
    min_value=0,
    value=0,
    step=1
)


# -----------------------------
# Result Popup
# -----------------------------
if st.button("🔮 Predict Placement"):

    try:

        # Encode branch
        branch_encoded = branch_encoder.transform([branch])[0]

        # Create input for model
        input_data = pd.DataFrame({
            "Branch": [branch_encoded],
            "CGPA": [cgpa],
            "No_of_Internships": [internships],
            "No_of_Projects": [projects]
        })

        # Predict
        prediction = model.predict(input_data)

        # Convert prediction back to Yes/No
        result = target_encoder.inverse_transform(prediction)[0]


        # -----------------------------
        # Popup
        # -----------------------------
        @st.dialog("🎓 Placement Result")
        def show_result():

            if result == "Yes":
                st.success("🎉 Congratulations!")
                st.write("Placement Prediction: **YES**")

            else:
                st.error("❌ Placement Prediction: NO")
                st.write("Keep improving your skills and profile.")

            if st.button("Close"):
                st.rerun()


        show_result()


    except Exception as e:

        st.error(f"Error: {e}")