import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("⚾ 2024 Breakout Pitchers – Kluber Model")

# Load data
df = pd.read_csv("breakout_data.csv")

# Color formatting
def color_score(val):
    color = "green" if val == 5 else "orange" if val >= 3 else "red"
    return f"color: {color}"

# Show the table
styled_df = df.style.applymap(color_score, subset=["Kluber Score"])
st.dataframe(styled_df, use_container_width=True)
