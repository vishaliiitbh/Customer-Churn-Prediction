Telco Customer Churn Prediction App
(Live Demo)[https://customer-churn-prediction-project1234.streamlit.app/]

This Streamlit application predicts customer churn in the telecommunications industry. With an intuitive interface, users can input individual customer data or upload a dataset for batch predictions. The model identifies customers likely to discontinue their service, enabling telecom companies to proactively manage customer retention.

📋 Features
Interactive Online Prediction: Manually input customer data to predict the likelihood of churn.
Batch Prediction: Upload a CSV file containing multiple customer records for batch predictions.
Dynamic Data Display: View an overview of the input data for quick insights before making predictions.
Stylish Design: Simple, modern layout with color-coded prediction results for easy readability.

📊 Model Selection Process
To ensure optimal performance, multiple machine learning algorithms were trained and compared using key metrics such as accuracy, precision, recall, and F1-score. After extensive testing, the best-performing model was selected to power this app, providing reliable and accurate predictions.

🚀 Usage
Online Prediction Mode
Open the app and select "Online" in the sidebar.
Enter customer details in the provided fields:
Demographic Data: Senior status, dependents, etc.
Payment Data: Contract type, billing method, monthly charges, etc.
Service Data: Services subscribed to, including multiple lines, internet, streaming services, etc.
Click Predict to view whether the customer is likely to churn.
Batch Prediction Mode
Open the app and select "Batch" in the sidebar.
Upload a CSV file containing customer data.
Click Predict to see predictions for each customer in the file.
CSV Format: Ensure your CSV file includes the following columns:

Copy code
SeniorCitizen, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges
🛠️ Technologies Used
Python: For core scripting and data manipulation.
Streamlit: Web-based user interface.
Joblib: For loading the trained machine learning model.
Pandas: For data manipulation.
scikit-learn and XGBoost: For machine learning model development and evaluation.
