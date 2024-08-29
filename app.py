import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration
st.set_page_config(
    page_title="Excel File Data Analysis",
    layout="wide",  # Set the layout to 'wide'
    initial_sidebar_state="expanded"  # Expand the sidebar initially
)

st.title('Excel File Data Analysis')

st.write("""
This app allows users to upload an Excel file and view data analytics dashboards and visualizations.
""")

# Sidebar for file upload
with st.sidebar:
    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Display data preview and basic analytics in the main page
    st.write("### Data Preview")
    st.dataframe(df.head())

    st.write("### Basic Data Analytics")

    # Show basic statistics
    st.write("Descriptive Statistics")
    st.write(df.describe())

    # Show column names
    st.write("Column Names")
    st.write(df.columns.tolist())

    # Show data types
    st.write("Data Types")
    st.write(df.dtypes)

    # Create two columns for dashboards
    dashboard_col1, dashboard_col2 = st.columns(2)

    with dashboard_col1:
        st.write("### Correlation Heatmap")
        corr = df.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    with dashboard_col2:
        st.write("### Bar Chart Example")
        if st.checkbox("Show Bar Chart"):
            column = st.selectbox("Select column for Bar Chart", df.columns)
            bar_fig, bar_ax = plt.subplots()
            df[column].value_counts().plot(kind='bar', ax=bar_ax)
            st.pyplot(bar_fig)
