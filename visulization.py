# -----------------------------------------------------
# Title: To perform Visualization using Python
# -----------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
path = input("Enter full CSV file path: ")
df = pd.read_csv(path)

print("✅ Dataset Loaded Successfully!\n")
print(df.head())

# 1️⃣ Line Chart
plt.figure(figsize=(6,4))
plt.plot(df[df.columns[0]], df[df.columns[1]], color='blue', marker='o')
plt.title("Line Chart")
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.show()

# 2️⃣ Bar Chart
plt.figure(figsize=(6,4))
plt.bar(df[df.columns[0]], df[df.columns[1]], color='orange')
plt.title("Bar Chart")
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.show()

# 3️⃣ Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df[df.columns[0]], df[df.columns[1]], color='green')
plt.title("Scatter Plot")
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.show()

# 4️⃣ Histogram
plt.figure(figsize=(6,4))
sns.histplot(df[df.columns[1]], bins=20, kde=True, color='purple')
plt.title("Histogram")
plt.xlabel(df.columns[1])
plt.show()

# 5️⃣ Pie Chart (if categorical column present)
cat_cols = df.select_dtypes(exclude=['number']).columns
if len(cat_cols) > 0:
    col = cat_cols[0]
    plt.figure(figsize=(6,6))
    df[col].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title(f"Pie Chart of {col}")
    plt.ylabel("")
    plt.show()

print("\n✅ Visualization Completed Successfully!")
