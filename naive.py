
# ---------------------------------------------------
# UNIVERSAL NAIVE BAYES CLASSIFIER (ERROR-FREE)
# ---------------------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import os
import numpy as np

# ---------------------------------------------------
# Step 1: Load CSV
# ---------------------------------------------------
filename = input("Enter CSV file path: ")

if not os.path.exists(filename):
    print("❌ File not found! Check your path.")
    exit()

df = pd.read_csv(filename)
print("✅ Dataset Loaded Successfully!")
print(df.head(), "\n")

# ---------------------------------------------------
# Step 2: Remove useless columns automatically
# (ID columns / columns with all unique values)
# ---------------------------------------------------
unique_cols = [col for col in df.columns if df[col].nunique() == len(df)]
if unique_cols:
    print("⚠ Removing unique ID-like columns:", unique_cols)
    df = df.drop(columns=unique_cols)

# Drop fully empty columns
df = df.dropna(axis=1, how='all')

# If dataset becomes empty
if df.shape[1] < 2:
    print("❌ Not enough usable columns after cleaning!")
    exit()

# ---------------------------------------------------
# Step 3: Ask user for target column
# ---------------------------------------------------
print("Columns:", list(df.columns))
target_column = input("Enter your target column (categorical preferred): ")

if target_column not in df.columns:
    print("❌ Target column not found!")
    exit()

# ---------------------------------------------------
# Step 4: Handle numeric target safely
# ---------------------------------------------------
if pd.api.types.is_numeric_dtype(df[target_column]):
    print("⚠ Numeric target detected → converting into 3 class bins")

    try:
        df[target_column + "_cat"] = pd.qcut(
            df[target_column], 
            q=3, 
            labels=['low', 'medium', 'high'],
            duplicates="drop"
        )
        target_column = target_column + "_cat"
    except Exception:
        print("⚠ Could not bin numeric target. Converting to labels by median split.")
        median_val = df[target_column].median()
        df[target_column + "_cat"] = np.where(
            df[target_column] >= median_val, "high", "low"
        )
        target_column = target_column + "_cat"

# ---------------------------------------------------
# Step 5: Preprocessing
# ---------------------------------------------------
df = df.dropna()  # remove missing rows

# Encode categoricals
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == object:
        df[col] = le.fit_transform(df[col].astype(str))

# ---------------------------------------------------
# Step 6: Split Data
# ---------------------------------------------------
X = df.drop(columns=[target_column])
y = df[target_column]

if len(df) < 2:
    print("❌ Not enough samples after preprocessing!")
    exit()

test_size = 0.3
if len(df) * test_size < 1:
    test_size = 0.2

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42
)

# ---------------------------------------------------
# Step 7: Train Model
# ---------------------------------------------------
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ---------------------------------------------------
# Step 8: Results
# ---------------------------------------------------
print("\n📌 Naive Bayes Accuracy:", accuracy_score(y_test, y_pred))
print("📌 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\n✅ Classification Completed Successfully!")
