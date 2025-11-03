# 🚀 K-Means Clustering Implementation using Python (Any Dataset)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 🟢 Step 1: Load dataset
path = input("Enter full CSV file path: ")
data = pd.read_csv(path)
print("\n✅ Dataset Loaded Successfully!\n")
print(data.head(), "\n")
print("Columns in dataset:", list(data.columns), "\n")

# 🟢 Step 2: Handle non-numeric data
for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = LabelEncoder().fit_transform(data[col])

data = data.dropna()

# 🟢 Step 3: Feature scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 🟢 Step 4: Choose number of clusters
try:
    k = int(input("Enter number of clusters (e.g., 2–5): "))
except:
    print("⚠ Invalid input! Using default k = 3")
    k = 3

# 🟢 Step 5: Apply K-Means
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_data)
data['Cluster'] = kmeans.labels_

# 🟢 Step 6: Results
print("\n📊 Cluster Centers:\n", kmeans.cluster_centers_)
print("\n📈 Inertia (lower = better fit):", kmeans.inertia_)
print("🤖 Silhouette Score:", silhouette_score(scaled_data, kmeans.labels_))

# 🟢 Step 7: Visualize the clusters (first two features)
plt.figure(figsize=(8, 6))
plt.scatter(
    scaled_data[:, 0], scaled_data[:, 1],
    c=kmeans.labels_, cmap='rainbow', s=60, edgecolors='black'
)
plt.title(f"🌈 K-Means Clustering Visualization (k={k})")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()

print("\n🎯 K-Means Clustering Completed Successfully!")
