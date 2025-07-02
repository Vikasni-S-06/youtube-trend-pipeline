import streamlit as st
from scripts.etl_pipeline import load_data, clean_data, transform_data

st.title("📺 YouTube Trending Data Dashboard")

data_path = "data/USvideos.csv"
df = load_data(data_path)
df = clean_data(df)
top_channels, top_videos = transform_data(df)

st.subheader("Top 10 Trending Channels")
st.bar_chart(top_channels)

st.subheader("Top 10 Most Viewed Videos")
st.bar_chart(top_videos)
