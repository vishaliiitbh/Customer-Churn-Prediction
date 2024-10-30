import streamlit as st
import pandas as pd
from PIL import Image
import joblib

# Load the model from disk
model = joblib.load(r"./Models/ml_model.sav")

# Import python scripts
from preprocessing import preprocess

# Custom CSS for styling
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f4f7;  /* Light grey background */
    }
    .sidebar .sidebar-content {
        background: #ffffff;  /* White background for sidebar */
        border-radius: 5px;   /* Rounded corners */
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1); /* Subtle shadow for depth */
    }
    .css-1d391kg {
        background-color: rgba(255, 255, 255, 0.7); /* Background for main container */
        border-radius: 10px; /* Rounded corners */
        padding: 20px; /* Padding for the content */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #0072B5; /* Change heading color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


def main():
    # Setting Application title
    st.title('🌟 Telco Customer Churn Prediction App 🌟')

    # Setting Application description
    st.markdown("""
        📈 **Predicting Customer Churn in Telecommunications: A Dynamic Streamlit App**
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Setting Application sidebar
    image = Image.open('image1.png')
    st.sidebar.image(image)
    st.sidebar.title("Menu")
    add_selectbox = st.sidebar.selectbox("How would you like to predict?", ("Online", "Batch"))
    st.sidebar.info('This app is created to predict Customer Churn')

    # Online prediction
    if add_selectbox == "Online":
        st.info("Input data below")
        st.markdown("<h3>Demographic data</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            seniorcitizen = st.selectbox('Senior Citizen:', ('Yes', 'No'))
            dependents = st.selectbox('Dependent:', ('Yes', 'No'))

        with col2:
            tenure = st.slider('Tenure (months):', min_value=0, max_value=72, value=0)
            contract = st.selectbox('Contract Type:', ('Month-to-month', 'One year', 'Two year'))

        st.markdown("<h3>Payment data</h3>", unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            paperlessbilling = st.selectbox('Paperless Billing:', ('Yes', 'No'))
            PaymentMethod = st.selectbox('Payment Method:', (
            'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
        with col4:
            monthlycharges = st.number_input('Monthly Charges:', min_value=0, max_value=150, value=0)
            totalcharges = st.number_input('Total Charges:', min_value=0, max_value=10000, value=0)

        st.markdown("<h3>Services signed up for</h3>", unsafe_allow_html=True)
        col5, col6 = st.columns(2)
        with col5:
            mutliplelines = st.selectbox("Multiple Lines:", ('Yes', 'No', 'No phone service'))
            phoneservice = st.selectbox('Phone Service:', ('Yes', 'No'))
            internetservice = st.selectbox("Internet Service:", ('DSL', 'Fiber optic', 'No'))

        with col6:
            onlinesecurity = st.selectbox("Online Security:", ('Yes', 'No', 'No internet service'))
            onlinebackup = st.selectbox("Online Backup:", ('Yes', 'No', 'No internet service'))
            techsupport = st.selectbox("Tech Support:", ('Yes', 'No', 'No internet service'))
            streamingtv = st.selectbox("Streaming TV:", ('Yes', 'No', 'No internet service'))
            streamingmovies = st.selectbox("Streaming Movies:", ('Yes', 'No', 'No internet service'))

        # Data Preparation
        data = {
            'SeniorCitizen': seniorcitizen,
            'Dependents': dependents,
            'tenure': tenure,
            'PhoneService': phoneservice,
            'MultipleLines': mutliplelines,
            'InternetService': internetservice,
            'OnlineSecurity': onlinesecurity,
            'OnlineBackup': onlinebackup,
            'TechSupport': techsupport,
            'StreamingTV': streamingtv,
            'StreamingMovies': streamingmovies,
            'Contract': contract,
            'PaperlessBilling': paperlessbilling,
            'PaymentMethod': PaymentMethod,
            'MonthlyCharges': monthlycharges,
            'TotalCharges': totalcharges
        }
        features_df = pd.DataFrame.from_dict([data])
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Overview of Input:")
        st.dataframe(features_df.style.highlight_max(axis=0))

        # Preprocess inputs
        preprocess_df = preprocess(features_df, 'Online')
        if st.button('Predict'):
            prediction = model.predict(preprocess_df)
            if prediction == 1:
                st.warning('🚨 **Yes, the customer will terminate the service.** 🚨', icon="⚠️")
            else:
                st.success('🎉 **No, the customer is happy with Telco Services!** 🎉', icon="✅")

    # Batch prediction
    else:
        st.subheader("Upload Dataset for Batch Prediction")
        uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.write(data.head())
            st.markdown("<hr>", unsafe_allow_html=True)
            preprocess_df = preprocess(data, "Batch")
            if st.button('Predict'):
                prediction = model.predict(preprocess_df)
                prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
                prediction_df = prediction_df.replace({
                    1: '🚨 Yes, the customer will terminate the service.',
                    0: '🎉 No, the customer is happy with Telco Services.'
                })

                st.markdown("<hr>", unsafe_allow_html=True)
                st.subheader('Batch Prediction Results')
                st.write(prediction_df)


if __name__ == '__main__':
    main()
