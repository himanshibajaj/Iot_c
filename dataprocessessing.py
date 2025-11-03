# ------------------------------------------------
# UNIVERSAL DATA PREPROCESSING IN PYTHON (NO ERRORS)
# ------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

# Load CSV safely
path = input("Enter full CSV file path: ")
if not os.path.exists(path):
    print("❌ File not found! Check the path.")
    exit()

data = pd.read_csv(path)
print("✅ Dataset Loaded Successfully!\n")
print(data.head(), "\n")

# Remove columns with all unique values (IDs)
unique_cols = [col for col in data.columns if data[col].nunique() == len(data)]
if unique_cols:
    print("⚠ Removing ID-like columns:", unique_cols)
    data = data.drop(columns=unique_cols)

# Drop completely empty columns
data = data.dropna(axis=1, how='all')

# Handle missing values
data = data.fillna(data.mean(numeric_only=True))  # fill numeric
for col in data.select_dtypes(include='object').columns:
    data[col] = data[col].fillna(data[col].mode()[0])  # fill categorical

# Encode categorical columns
le = LabelEncoder()
for col in data.columns:
    if data[col].dtype == object:
        data[col] = le.fit_transform(data[col].astype(str))

# Feature Scaling
scaler = StandardScaler()
scaled_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

# Split into features & target
X = scaled_data.iloc[:, :-1]
y = scaled_data.iloc[:, -1]

# Split train-test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Show summary
print("\n✅ Preprocessing Completed Successfully!")
print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)
print("\nFirst few processed rows:\n", scaled_data.head())
