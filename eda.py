# ------------------------------------------------
# INTERACTIVE EXPLORATORY DATA ANALYSIS (EDA)
# ------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load Dataset
path = input("Enter full CSV file path: ")

if not os.path.exists(path):
    print("❌ File not found! Check the path.")
    exit()

df = pd.read_csv(path)
print("✅ Dataset Loaded Successfully!\n")
print(df.head(), "\n")

# Step 2: Basic Info
print("🔍 Dataset Info:")
print(df.info())

print("\n📊 Statistical Summary:")
print(df.describe())

# Step 3: Missing Values
print("\n❗ Missing Values:")
print(df.isnull().sum())

# Step 4: Clean empty columns
df = df.dropna(axis=1, how='all')

# Step 5: Identify numeric & categorical columns
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

print(f"\n🔢 Numeric Columns: {num_cols}")
print(f"🔤 Categorical Columns: {cat_cols}")

# ------------------------------------------------
# USER-CONTROLLED VISUALIZATIONS
# ------------------------------------------------

# 1️⃣ HISTOGRAM
ans = input("\n📈 Do you want to see a histogram? (yes/no): ").lower()
if ans == 'yes':
    print(f"Available numeric columns: {num_cols}")
    cols = input("Enter column names separated by commas: ").split(',')
    cols = [c.strip() for c in cols if c.strip() in num_cols]
    for col in cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col], kde=True, color='skyblue', bins=20)
        plt.title(f"Histogram of {col}")
        plt.tight_layout()
        plt.show()

# 2️⃣ BOX PLOT
ans = input("\n📦 Do you want to see boxplots? (yes/no): ").lower()
if ans == 'yes':
    print(f"Available numeric columns: {num_cols}")
    cols = input("Enter column names separated by commas: ").split(',')
    cols = [c.strip() for c in cols if c.strip() in num_cols]
    for col in cols:
        plt.figure(figsize=(6,4))
        sns.boxplot(x=df[col], color='salmon')
        plt.title(f"Boxplot of {col}")
        plt.tight_layout()
        plt.show()

# 3️⃣ HEATMAP
ans = input("\n🔥 Do you want to see a correlation heatmap? (yes/no): ").lower()
if ans == 'yes' and len(num_cols) > 1:
    plt.figure(figsize=(10,6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

# 4️⃣ PIE CHART
ans = input("\n🥧 Do you want to see a pie chart? (yes/no): ").lower()
if ans == 'yes' and cat_cols:
    print(f"Available categorical columns: {cat_cols}")
    col = input("Enter column name for pie chart: ").strip()
    if col in cat_cols:
        plt.figure(figsize=(6,6))
        df[col].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
        plt.title(f"Pie Chart of {col}")
        plt.ylabel("")
        plt.show()

# 5️⃣ PAIRPLOT (optional)
ans = input("\n📊 Do you want to see a pairplot? (yes/no): ").lower()
if ans == 'yes' and len(num_cols) > 1 and len(num_cols) <= 6:
    sns.pairplot(df[num_cols])
    plt.suptitle("Pairplot of Numeric Features", y=1.02)
    plt.show()

print("\n✅ Interactive EDA Completed Successfully!")
