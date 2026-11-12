
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('churn_model.pkl')

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a customer is likely to leave the service.")

st.divider()

with st.form("customer_form"):

    st.subheader("Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior_citizen = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])

    with col2:
        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=100,
            value=12
        )

        phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        if phone_service == "Yes":
            multiple_lines = st.selectbox(
                "Multiple Lines",
                ["Yes", "No"]
            )
        else:
            multiple_lines = "No phone service"
            st.info("Multiple Lines: No phone service")

    st.divider()

    st.subheader("Internet Services")

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    if internet_service != "No":

        col1, col2 = st.columns(2)

        with col1:
            online_security = st.selectbox(
                "Online Security", ["Yes", "No"]
            )
            online_backup = st.selectbox(
                "Online Backup", ["Yes", "No"]
            )
            device_protection = st.selectbox(
                "Device Protection", ["Yes", "No"]
            )

        with col2:
            tech_support = st.selectbox(
                "Tech Support", ["Yes", "No"]
            )
            streaming_tv = st.selectbox(
                "Streaming TV", ["Yes", "No"]
            )
            streaming_movies = st.selectbox(
                "Streaming Movies", ["Yes", "No"]
            )

    else:
        online_security = "No internet service"
        online_backup = "No internet service"
        device_protection = "No internet service"
        tech_support = "No internet service"
        streaming_tv = "No internet service"
        streaming_movies = "No internet service"

        st.info("Internet add-on services: No internet service")

    st.divider()

    st.subheader("Account Information")

    col1, col2 = st.columns(2)

    with col1:
        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

    with col2:
        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )

    submitted = st.form_submit_button(
        "Predict Churn",
        use_container_width=True
    )


if submitted:

    # Binary Encoding
    binary_mapping = {
        "Yes": 1,
        "No": 0,
        "Male": 1,
        "Female": 0
    }

    # Feature Engineering

    num_services = (
        int(phone_service == "Yes")
        + int(multiple_lines == "Yes")
        + int(internet_service != "No")
        + sum([
            int(online_security == "Yes"),
            int(online_backup == "Yes"),
            int(device_protection == "Yes"),
            int(tech_support == "Yes"),
            int(streaming_tv == "Yes"),
            int(streaming_movies == "Yes")
        ])
    )

    num_protection_services = sum([
        int(online_security == "Yes"),
        int(online_backup == "Yes"),
        int(device_protection == "Yes"),
        int(tech_support == "Yes")
    ])

    if tenure <= 12:
        tenure_group = "New"
    elif tenure <= 24:
        tenure_group = "Short"
    elif tenure <= 48:
        tenure_group = "Medium"
    else:
        tenure_group = "Long"

    # Prepare input data
    input_data = pd.DataFrame([{
        'gender': binary_mapping[gender],
        'SeniorCitizen': senior_citizen,
        'Partner': binary_mapping[partner],
        'Dependents': binary_mapping[dependents],
        'tenure': tenure,
        'PhoneService': binary_mapping[phone_service],
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': binary_mapping[paperless_billing],
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'NumServices': num_services,
        'NumProtectionServices': num_protection_services,
        'TenureGroup': tenure_group
    }])

    # Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.divider()
    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        if prediction == 1:
            st.error("⚠️ Customer is likely to Churn")
        else:
            st.success("✅ Customer is likely to Stay")

    with col2:
        st.metric(
            "Churn Probability",
            f"{probability * 100:.2f}%"
        )

    st.progress(float(probability))

    st.caption(
        "The probability is a model estimate, not a guarantee "
        of the customer's future behavior."
    )
