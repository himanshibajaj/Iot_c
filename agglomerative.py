# 🚀 Agglomerative (Hierarchical) Clustering using Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# 🟢 Step 1: Load dataset
path = input("Enter full CSV file path: ")
data = pd.read_csv(path)
print("\n✅ Dataset Loaded Successfully!\n")
print(data.head(), "\n")
print("Columns in dataset:", list(data.columns), "\n")

# 🧹 Step 2: Clean data
# Remove unnamed or empty columns
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# Encode categorical columns (like 'diagnosis')
for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = LabelEncoder().fit_transform(data[col])

# Drop ID columns if they exist
if 'id' in data.columns:
    data = data.drop('id', axis=1)

# Drop any rows with missing values
data = data.dropna()

# ✅ Check if dataset is not empty
if data.shape[0] == 0:
    raise ValueError("❌ No valid rows left after cleaning! Check your CSV.")

# 🟢 Step 3: Scale numeric data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 🟢 Step 4: Choose number of clusters
try:
    n_clusters = int(input("Enter number of clusters (e.g., 2–5): "))
except:
    print("⚠ Invalid input! Using default n_clusters = 3")
    n_clusters = 3

# 🟢 Step 5: Apply Agglomerative Clustering
agg = AgglomerativeClustering(n_clusters=n_clusters, metric='euclidean', linkage='ward')
clusters = agg.fit_predict(scaled_data)
data['Cluster'] = clusters

# 🟢 Step 6: Display summary
print("\n📊 Cluster Labels Assigned:")
print(data['Cluster'].value_counts())

# 🟢 Step 7: Plot Dendrogram (Tree)
plt.figure(figsize=(10, 5))
linked = linkage(scaled_data, method='ward')
dendrogram(linked)
plt.title("🌳 Dendrogram (Agglomerative Hierarchical Clustering)")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

# 🟢 Step 8: Scatter plot (first 2 features)
plt.figure(figsize=(8, 6))
plt.scatter(
    scaled_data[:, 0], scaled_data[:, 1],
    c=clusters, cmap='rainbow', s=60, edgecolors='black'
)
plt.title(f"🌈 Agglomerative Clustering Visualization (k={n_clusters})")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()

print("\n🎯 Agglomerative Clustering Completed Successfully!")
