import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load a sample
df = pd.read_csv("metadata.csv", nrows=100000)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers metadata")

# Year range selector
years = df['year'].dropna().astype(int).unique()
min_year, max_year = min(years), max(years)
year_range = st.slider("Select Year Range", min_year, max_year, (2020, 2021))

# Filter data
df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Visualization
st.subheader("Publications by Year")
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
st.pyplot(fig)

# Show top journals
st.subheader("Top Journals")
top_journals = df_filtered['journal'].value_counts().head(1000)
st.bar_chart(top_journals)

# Sample data
st.subheader("Sample Data")
st.dataframe(df_filtered.head(1000))
