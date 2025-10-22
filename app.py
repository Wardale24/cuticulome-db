import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/proteins.csv")

df = load_data()

# App title
st.title("🪶 Cuticulome (Prototype)")
st.write("A database of arthropod cuticular proteins — prototype version")

# Sidebar filters
st.sidebar.header("Filter Proteins")
species = st.sidebar.multiselect("Select Species", sorted(df["Species"].unique()))
function = st.sidebar.text_input("Search Function Keyword")

filtered_df = df.copy()
if species:
    filtered_df = filtered_df[filtered_df["Species"].isin(species)]
if function:
    filtered_df = filtered_df[filtered_df["Function"].str.contains(function, case=False, na=False)]

st.dataframe(filtered_df, use_container_width=True)

# Download option
st.download_button(
    label="Download filtered data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="cuticulome_filtered.csv",
    mime="text/csv"
)

st.markdown("---")
st.caption("Prototype by Alex Wardale — powered by Streamlit.")
