# 1️⃣ Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib


# 2️⃣ Load Data
data = pd.read_csv("loan_dataset.csv")

# Drop missing values
data = data.dropna()


# 3️⃣ Preprocessing (from your notebook)

# Encode target variable
data["Loan_Status"] = data["Loan_Status"].map({'Y': 1, 'N': 0})

# Fix Dependents column
data['Dependents'] = data['Dependents'].replace('3+', 4)

# Encode categorical features
data['Married'] = data['Married'].map({'Yes': 1, 'No': 0})
data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})
data['Self_Employed'] = data['Self_Employed'].map({'Yes': 1, 'No': 0})
data['Education'] = data['Education'].map({'Graduate': 1, 'Not Graduate': 0})
data['Property_Area'] = data['Property_Area'].map({
    'Rural': 0,
    'Semiurban': 1,
    'Urban': 2
})


# 4️⃣ Feature / Label Split
X = data.drop(columns=['Loan_ID', 'Loan_Status'])
y = data['Loan_Status']


# 5️⃣ Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


# 6️⃣ Model (same logic as notebook)
model = SVC(kernel='linear')

model.fit(X_train, y_train)


# 7️⃣ Evaluation (Optional but Good Practice)
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Test Accuracy:", accuracy_score(y_test, test_pred))


# 8️⃣ Save Artifacts (MOST IMPORTANT)
joblib.dump(model, "backend/loan_model.pkl")

print("Model saved successfully ✅")