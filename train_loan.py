import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv("loan_dataset.csv")

data = data.dropna()

data["Loan_Status"] = data["Loan_Status"].map({'Y': 1, 'N': 0})

data['Dependents'] = data['Dependents'].replace('3+', 4)

data['Married'] = data['Married'].map({'Yes': 1, 'No': 0})
data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})
data['Self_Employed'] = data['Self_Employed'].map({'Yes': 1, 'No': 0})
data['Education'] = data['Education'].map({'Graduate': 1, 'Not Graduate': 0})
data['Property_Area'] = data['Property_Area'].map({
    'Rural': 0,
    'Semiurban': 1,
    'Urban': 2
})

X = data.drop(columns=['Loan_ID', 'Loan_Status'])
y = data['Loan_Status']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


model = SVC(kernel='linear')

model.fit(X_train, y_train)

test_pred = model.predict(X_test)

print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Test Accuracy:", accuracy_score(y_test, test_pred))


joblib.dump(model, "backend/loan_model.pkl")

print("Model saving successful")
