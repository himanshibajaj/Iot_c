# 🚀 Association Rule Mining using Apriori Algorithm (Auto handles numeric data)
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import matplotlib.pyplot as plt

# 🟢 Step 1: Load dataset
path = input("Enter full CSV file path: ")
data = pd.read_csv(path)

print("\n✅ Dataset Loaded Successfully!\n")
print(data.head(), "\n")
print("Columns in dataset:", list(data.columns), "\n")

# 🧹 Step 2: Preprocessing - Convert numeric to categorical
df = data.copy()

for col in df.select_dtypes(include=[np.number]).columns:
    # Convert numeric to bins (Low, Medium, High)
    df[col] = pd.qcut(df[col], q=3, labels=['Low', 'Medium', 'High'])

print("⚙️ Converted numeric columns into categories...\n")

# 🟢 Step 3: One-hot encode categorical data
df_encoded = pd.get_dummies(df)

print("✅ Data ready for Apriori!\n")
print(df_encoded.head(), "\n")

# 🟢 Step 4: Generate frequent itemsets
try:
    min_sup = float(input("Enter minimum support (e.g., 0.2): "))
except:
    min_sup = 0.2

frequent_itemsets = apriori(df_encoded, min_support=min_sup, use_colnames=True)
print("\n📊 Frequent Itemsets:")
print(frequent_itemsets.head())

# 🟢 Step 5: Generate Association Rules
try:
    min_conf = float(input("Enter minimum confidence (e.g., 0.6): "))
except:
    min_conf = 0.6

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_conf)
rules = rules.sort_values(by="lift", ascending=False)

print("\n🔍 Top Association Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())

# 🟢 Step 6: Visualization
plt.figure(figsize=(7,5))
plt.scatter(rules['support'], rules['confidence'], s=100, c=rules['lift'], cmap='viridis')
plt.title('📈 Support vs Confidence (Colored by Lift)')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.colorbar(label='Lift')
plt.grid(True)
plt.show()

print("\n🎯 Association Rule Mining Completed Successfully!")
