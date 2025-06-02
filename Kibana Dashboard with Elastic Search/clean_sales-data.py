import pandas as pd

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="ISO-8859-1")

# Rename columns for consistency
df = df.rename(columns={
    'Order ID': 'order_id',
    'Order Date': 'order_date',
    'Region': 'region',
    'State': 'state',
    'Product Name': 'product',
    'Category': 'category',
    'Sub-Category': 'sub_category',
    'Customer Name': 'customer_name',
    'Sales': 'sales',
    'Profit': 'profit'
})

# Keep only relevant columns
df = df[['order_id', 'order_date', 'region', 'state', 'product', 'category',
         'sub_category', 'customer_name', 'sales', 'profit']]

# Convert date format to ISO 8601
df['order_date'] = pd.to_datetime(df['order_date']).dt.strftime('%Y-%m-%d')

# Remove rows with missing sales or order_id
df = df.dropna(subset=['order_id', 'sales'])

# Save cleaned data
df.to_csv("clean_sales_data.csv", index=False)
print("✅ Cleaned dataset saved as clean_sales_data.csv")
