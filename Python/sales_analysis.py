# ==============================
# 1. Import Libraries
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ==============================
# 2. Load Data
# ==============================

# Read CSV file
df = pd.read_csv("Data/sales_data.csv")

# Display first 5 rows
print(df.head())


# ==============================
# 3. Data Cleaning
# ==============================

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Check duplicate rows
print("Duplicate rows:", df.duplicated().sum())


# Convert Date column to datetime

df["Date"] = pd.to_datetime(df["Date"])

# Extract Year and Month

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

print(df.head())



# ==============================
# 4. Exploratory Data Analysis
# ==============================

# Total Sales

total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)


# Total Quantity Sold

total_quantity = df["Quantity"].sum()

print("Total Quantity:", total_quantity)


# Sales by Product

product_sales = df.groupby("Product")["Sales"].sum()

product_sales_sorted = product_sales.sort_values(ascending=False)

print(product_sales_sorted)



# Sales by Region

region_sales = df.groupby("Region")["Sales"].sum()

region_sales_sorted = region_sales.sort_values(ascending=False)

print(region_sales_sorted)



# Sales by Category

category_sales = df.groupby("Category")["Sales"].sum()

category_sales_sorted = category_sales.sort_values(ascending=False)

print(category_sales_sorted)



# Monthly Sales Analysis

monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales = monthly_sales.sort_index()

print(monthly_sales)



# ==============================
# 5. Data Visualization
# ==============================


# Monthly Sales Trend

plt.figure(figsize=(8,5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.savefig("Visualizations/monthly_sales.png")

plt.show()



# Top Products Chart

plt.figure(figsize=(8,5))

plt.bar(
    product_sales_sorted.index,
    product_sales_sorted.values
)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.savefig("Visualizations/product_sales.png")

plt.show()



# Sales by Region Chart

plt.figure(figsize=(8,5))

plt.bar(
    region_sales_sorted.index,
    region_sales_sorted.values
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.savefig("Visualizations/region_sales.png")

plt.show()



# Sales by Category Chart

plt.figure(figsize=(8,5))

sns.barplot(
    x=category_sales_sorted.index,
    y=category_sales_sorted.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.savefig("Visualizations/category_sales.png")

plt.show()



# ==============================
# 6. Export Clean Data
# ==============================


df.to_csv("Data/sales_cleaned.csv", index=False)

print("Cleaned data exported successfully")
