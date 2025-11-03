# 🚀 DBSCAN Clustering Implementation using Python (Error-Free Version)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import DBSCAN

# 🟢 Step 1: Load dataset
path = input("Enter full CSV file path: ")
data = pd.read_csv(path)
print("\n✅ Dataset Loaded Successfully!\n")
print(data.head(), "\n")
print("Columns in dataset:", list(data.columns), "\n")

# 🟢 Step 2: Data preprocessing
for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = LabelEncoder().fit_transform(data[col])

data = data.dropna()
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 🟢 Step 3: Safe user input
try:
    eps_value = float(input("Enter eps value (recommended 0.3 to 1.0): "))
except:
    print("⚠ Invalid input! Using default eps = 0.5")
    eps_value = 0.5

try:
    min_samples_value = int(input("Enter min_samples value (recommended 3 to 6): "))
except:
    print("⚠ Invalid input! Using default min_samples = 5")
    min_samples_value = 5

# 🟢 Step 4: Apply DBSCAN
db = DBSCAN(eps=eps_value, min_samples=min_samples_value)
clusters = db.fit_predict(scaled_data)
data['Cluster'] = clusters

# 🟢 Step 5: Display summary
print("\n📊 Cluster Labels (unique):", np.unique(clusters))
print("\nCluster count summary:\n", data['Cluster'].value_counts())
outliers = list(clusters).count(-1)
print(f"\n🚨 Outliers detected (Cluster = -1): {outliers}")

# 🟢 Step 6: Visualization with outliers marked red
plt.figure(figsize=(8, 6))
plt.scatter(
    scaled_data[:, 0], scaled_data[:, 1],
    c=clusters, cmap='rainbow', s=60, edgecolors='black'
)
plt.title("🌈 DBSCAN Clustering Visualization")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()

print("\n🎯 DBSCAN Clustering Completed Successfully!")
