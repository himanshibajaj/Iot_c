# Decision Tree Classification with Visualization
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

# 🟢 Step 1: Load dataset
path = input("Enter full CSV file path: ")
data = pd.read_csv(path)
print("\n✅ Dataset Loaded Successfully!\n")
print(data.head(), "\n")
print("Columns in dataset:", list(data.columns), "\n")

# 🟢 Step 2: Select target column
target_col = input("Enter the target column name (for classification): ")

X = data.drop(columns=[target_col])
y = data[target_col]

# Encode categorical values
for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = LabelEncoder().fit_transform(X[col])

if y.dtype == 'object':
    y = LabelEncoder().fit_transform(y)

# 🟢 Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 🟢 Step 4: Train model
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

# 🟢 Step 5: Evaluate model
y_pred = model.predict(X_test)
print("📊 Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 🟢 Step 6: Visualize Decision Tree
plt.figure(figsize=(14, 8))
plot_tree(
    model,
    filled=True,
    feature_names=X.columns,
    class_names=[str(c) for c in set(y)],
    rounded=True,
    fontsize=10
)
plt.title("🌳 Decision Tree Visualization", fontsize=14)
plt.show()

print("\n🎯 Decision Tree Displayed Successfully!")
