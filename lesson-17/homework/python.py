# 1
import pandas as pd
import numpy as np  # Needed for random salary generation

# Create DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Rename columns using function
df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

# Print first 3 rows
print("First 3 rows:")
print(df.head(3))

# Find mean age
mean_age = df['age'].mean()
print("\nMean age:", mean_age)

# Select and print only 'first_name' and 'city'
print("\nName and City columns:")
print(df[['first_name', 'city']])

# Add 'salary' column with random values
df['salary'] = np.random.randint(4000, 8000, size=len(df))

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))
# 2
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# Max values
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

# Min values
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

# Average values
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())
# 3
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set 'Category' as index
expenses.set_index('Category', inplace=True)

# Maximum expense for each category
print("Max expense per category:")
print(expenses.max(axis=1))

# Minimum expense for each category
print("\nMin expense per category:")
print(expenses.min(axis=1))

# Average expense for each category
print("\nAverage expense per category:")
print(expenses.mean(axis=1))
