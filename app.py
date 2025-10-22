import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/proteins.csv")

df = load_data()

# App title
st.title("🐜 Cuticulome.db - Prototype")
st.write("A database of arthropod cuticular proteins — prototype version")

st.markdown("""
Welcome to the **Cuticulome Database** — a curated collection of arthropod cuticular proteins.

Use the sidebar to navigate between:
- 🧭 **Help**: Learn about the database and its columns  
- 📊 **Statistics**: View summary statistics  
- 📫 **Contact**: Reach the maintainers  
""")

# Load example data
@st.cache_data
def load_data():
    return pd.read_csv("data/cuticular_proteins.csv")

df = load_data()
st.subheader("Preview of the database")
st.dataframe(df.head(10))

st.markdown("---")
st.caption("Prototype by Alex Wardale — powered by Streamlit.")
