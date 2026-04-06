import streamlit as st
import requests

# -----------------------------------
# Page Config (VERY IMPORTANT)
# -----------------------------------
st.set_page_config(
    page_title="Loan Prediction System",
    layout="wide"
)

st.title("!!Loan Prediction System!!")

st.divider()

# -----------------------------------
# Layout using Columns
# -----------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Applicant Information")

    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    st.subheader("Financial Details")

    ApplicantIncome = st.number_input("Applicant Income", min_value=0)
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
    LoanAmount = st.number_input("Loan Amount", min_value=0)
    Loan_Amount_Term = st.number_input("Loan Amount Term", min_value=0)
    Credit_History = st.selectbox("Credit History", [1, 0])

Property_Area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

st.divider()

# -----------------------------------
# Encoding Logic
# -----------------------------------
gender_map = {"Male": 1, "Female": 0}
married_map = {"Yes": 1, "No": 0}
education_map = {"Graduate": 1, "Not Graduate": 0}
self_emp_map = {"Yes": 1, "No": 0}
property_map = {"Rural": 0, "Semiurban": 1, "Urban": 2}
dependents_map = {"0": 0, "1": 1, "2": 2, "3+": 4}


# -----------------------------------
# Predict Button (Centered)
# -----------------------------------
center_col = st.columns([1, 2, 1])[1]

with center_col:
    if st.button("Predict Loan Status", use_container_width=True):

        data = {
            "Gender": gender_map[Gender],
            "Married": married_map[Married],
            "Dependents": dependents_map[Dependents],
            "Education": education_map[Education],
            "Self_Employed": self_emp_map[Self_Employed],
            "ApplicantIncome": ApplicantIncome,
            "CoapplicantIncome": CoapplicantIncome,
            "LoanAmount": LoanAmount,
            "Loan_Amount_Term": Loan_Amount_Term,
            "Credit_History": Credit_History,
            "Property_Area": property_map[Property_Area]
        }

        try:
            response = requests.post(
                "http://backend:8000/predict",
                json=data
            )

            result = response.json()

            st.divider()

            if result["prediction"] == 1:
                st.success("!!Loan Approved!!")
                st.balloons()
            else:
                st.error("//Loan Rejected\\")

        except:
            st.error("Backend not running. Start FastAPI first.")