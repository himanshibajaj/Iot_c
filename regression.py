# 🚀 Regression Model Implementation using Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# 🟢 Step 1: Load dataset
path = input("Enter full CSV file path: ")
data = pd.read_csv(path)
print("\n✅ Dataset Loaded Successfully!\n")
print(data.head(), "\n")
print("Columns in dataset:", list(data.columns), "\n")

# 🟢 Step 2: Select target column
target_col = input("Enter the target column name (for regression): ")

# Drop target column to form features
X = data.drop(columns=[target_col])
y = data[target_col]

# Encode non-numeric columns (if any)
for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = LabelEncoder().fit_transform(X[col])

# 🟢 Step 3: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🟢 Step 4: Train the Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 🟢 Step 5: Predictions and Evaluation
y_pred = model.predict(X_test)

print("\n📊 Model Performance:")
print("Mean Squared Error:", round(mean_squared_error(y_test, y_pred), 3))
print("R² Score:", round(r2_score(y_test, y_pred), 3))

# 🟢 Step 6: Visualize Actual vs Predicted
plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred, color='teal', alpha=0.7)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("📈 Actual vs Predicted (Regression Output)")
plt.grid(True)
plt.show()

print("\n🎯 Regression Model Implementation Completed Successfully!")
