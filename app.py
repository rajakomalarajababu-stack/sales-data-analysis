import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Title
st.title("Sales Data Analysis Dashboard")

# Load dataset
df = pd.read_csv("sales_data.csv", encoding='latin1')

# Show first rows
st.subheader("Dataset")
st.write(df.head())

# Total Sales
total_sales = df['Sales'].sum()
st.metric("Total Sales", total_sales)

# Total Profit
total_profit = df['Profit'].sum()
st.metric("Total Profit", total_profit)

# Region-wise Sales
st.subheader("Region Wise Sales")

region_sales = df.groupby('Region')['Sales'].sum()

fig, ax = plt.subplots()

sns.barplot(
    x=region_sales.index,
    y=region_sales.values,
    ax=ax
)

st.pyplot(fig)