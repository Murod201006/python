import pandas as pd
####1
# 1
df = pd.read_csv("task/sales_data.csv")

category_stats = df.groupby("Category").agg(
    Total_Quantity_Sold=("Quantity", "sum"),
    Average_Price=("Price", "mean"),
    Max_Quantity_Sold_Single_Transaction=("Quantity", "max")
)
# 2
top_products = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_sellers = top_products.loc[top_products.groupby("Category")["Quantity"].idxmax()]
# 3
df["Total_Sales"] = df["Quantity"] * df["Price"]
highest_sales_date = df.groupby("Date")["Total_Sales"].sum().idxmax()


####2
import pandas as pd

# 1
df = pd.read_csv("task/customer_orders.csv")

orders_per_customer = df.groupby("CustomerID")["OrderID"].nunique()
active_customers = orders_per_customer[orders_per_customer >= 20].index
filtered_df = df[df["CustomerID"].isin(active_customers)]
# 2
avg_price_per_customer = df.groupby("CustomerID")["Price"].mean()
high_value_customers = avg_price_per_customer[avg_price_per_customer > 120].index
# 3
product_totals = df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Price", lambda x: (x * df.loc[x.index, "Quantity"]).sum())
)
filtered_products = product_totals[product_totals["Total_Quantity"] >= 5]


####3
import pandas as pd
import sqlite3

# 1
conn = sqlite3.connect("task/population.db")
df = pd.read_sql("SELECT * FROM population", conn)
conn.close()
# 2
salary_bands = pd.read_excel("task/population salary analysis.xlsx")
# 3
def categorize_salary(salary):
    row = salary_bands[(salary_bands["Min"] <= salary) & (salary <= salary_bands["Max"])]
    return row["Category"].values[0] if not row.empty else "Unknown"

df["SalaryCategory"] = df["Salary"].apply(categorize_salary)
# 4
from numpy import median

salary_stats = df.groupby("SalaryCategory").agg(
    Population_Percent=("Salary", lambda x: len(x)/len(df)*100),
    Average_Salary=("Salary", "mean"),
    Median_Salary=("Salary", median),
    Population_Count=("Salary", "count")
)
# 5
state_salary_stats = df.groupby(["State", "SalaryCategory"]).agg(
    Population_Percent=("Salary", lambda x: len(x)/len(df[df["State"] == x.name[0]])*100),
    Average_Salary=("Salary", "mean"),
    Median_Salary=("Salary", median),
    Population_Count=("Salary", "count")
)
