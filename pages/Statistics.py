import streamlit as st
import pandas as pd

st.title("📊 Database Statistics")

@st.cache_data
def load_data():
    return pd.read_csv("data/cuticular_proteins.csv")

df = load_data()

st.write(f"**Total entries:** {len(df)}")

# Optional: show counts by species
if "Species" in df.columns:
    species_counts = df["Species"].value_counts()
    st.bar_chart(species_counts)

st.markdown("""
These statistics update automatically as new entries are added.
""")

