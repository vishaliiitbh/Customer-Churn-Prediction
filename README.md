URL of the deployed app - https://customer-churn-prediction-project1234.streamlit.app/
##Telco Customer Churn Prediction App
This is a Streamlit application for predicting customer churn in the telecommunications industry. With an intuitive interface, users can input individual customer data or upload a dataset for batch predictions. The model identifies which customers are likely to discontinue their service, enabling telecom companies to take proactive steps for customer retention.

##Features
Interactive Online Prediction: Users can manually input customer data to predict the likelihood of churn.
Batch Prediction: Users can upload a CSV file containing multiple customer records for batch predictions.
Dynamic Data Display: View an overview of the input data, providing quick insight before making predictions.
Stylish Design: Simple and modern layout with color-coded prediction results (e.g., success/warning) for easy readability.
##Model Selection Process
To ensure optimal performance, various machine learning algorithms were trained, and their performance was compared based on key metrics like accuracy, precision, recall, and F1-score. 
After testing multiple models, the best-performing model was chosen to power this app.
##Usage
Online Prediction Mode
Launch the app and select "Online" in the sidebar.
Enter customer details in the provided fields:
Demographic Data: Senior status, dependents, etc.
Payment Data: Contract type, billing method, monthly charges, etc.
Service Data: Services subscribed to, including multiple lines, internet, streaming services, etc.
Click Predict. The app will display whether the customer is likely to churn.
Batch Prediction Mode
Launch the app and select "Batch" in the sidebar.
Upload a CSV file containing customer data.
Click Predict. The app will display predictions for each customer in the file.
##Technologies Used
Python
Streamlit: For web-based user interface
Joblib: For loading the trained machine learning model
Pandas: For data manipulation
scikit-learn and XGBoost: For machine learning model development and evaluation
