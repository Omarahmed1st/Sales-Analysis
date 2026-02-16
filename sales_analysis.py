import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Superstore.csv", encoding='latin1')

# Show first rows
print(df.head())

# Basic Info
print(df.info())

# Drop missing values
df = df.dropna()

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# =========================
# 1️⃣ Total Revenue
# =========================
total_revenue = df['Sales'].sum()
print("Total Revenue:", round(total_revenue, 2))

# =========================
# 2️⃣ Top 5 Products
# =========================
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:\n", top_products)

# =========================
# 3️⃣ Top 5 Cities
# =========================
top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Cities:\n", top_cities)

# =========================
# 4️⃣ Most Profitable Segment
# =========================
segment_profit = df.groupby('Segment')['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Segment:\n", segment_profit)

# =========================
# 5️⃣ Monthly Sales Trend
# =========================
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(figsize=(10,5))
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
