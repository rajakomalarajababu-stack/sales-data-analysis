import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Interactive Sales Data Dashboard")

# User uploads dataset
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(
        uploaded_file,
        encoding='latin1'
    )

    st.subheader("Dataset Preview")
    st.write(df.head())

    # Region filter
    regions = df["Region"].unique()

    selected_region = st.selectbox(
        "Select Region",
        regions
    )

    filtered_df = df[
        df["Region"] == selected_region
    ]

    st.subheader("Filtered Data")
    st.write(filtered_df)

    total_sales = filtered_df["Sales"].sum()

    total_profit = filtered_df["Profit"].sum()

    col1,col2 = st.columns(2)

    col1.metric(
        "Total Sales",
        f"${total_sales:,.2f}"
    )

    col2.metric(
        "Total Profit",
        f"${total_profit:,.2f}"
    )

    st.subheader(
        "Category Sales"
    )

    category_sales = filtered_df.groupby(
        "Category"
    )["Sales"].sum()

    fig,ax = plt.subplots()

    sns.barplot(
        x=category_sales.index,
        y=category_sales.values,
        ax=ax
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

else:

    st.info(
        "Upload CSV file to continue"
    )