import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cuticulome Mini Database", page_icon="🪶", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/proteins.csv")

df = load_data()

st.title("🪶 Cuticulome Mini Database (Prototype)")
st.write("""
A pilot database of arthropod cuticular proteins with hierarchical taxonomy filters.
Explore by Family → Genus → Species and download your filtered results.
""")

# --- Sidebar Filters ---
st.sidebar.header("🧬 Filter Proteins")

# Family selection
families = sorted(df["Family"].unique())
selected_family = st.sidebar.selectbox("Select Family", ["All"] + families)

# Filter by selected family
if selected_family != "All":
    df_filtered = df[df["Family"] == selected_family]
else:
    df_filtered = df.copy()

# Genus selection
genera = sorted(df_filtered["Genus"].unique())
selected_genus = st.sidebar.selectbox("Select Genus", ["All"] + genera)

if selected_genus != "All":
    df_filtered = df_filtered[df_filtered["Genus"] == selected_genus]

# Species selection
species = sorted(df_filtered["Species"].unique())
selected_species = st.sidebar.selectbox("Select Species", ["All"] + species)

if selected_species != "All":
    df_filtered = df_filtered[df_filtered["Species"] == selected_species]

# Function keyword filter
function_keyword = st.sidebar.text_input("Search Function Keyword")
if function_keyword:
    df_filtered = df_filtered[df_filtered["Function"].str.contains(function_keyword, case=False, na=False)]

# --- Display filtered table ---
st.dataframe(df_filtered, use_container_width=True)

# --- Download filtered data ---
st.download_button(
    label="⬇️ Download filtered data as CSV",
    data=df_filtered.to_csv(index=False),
    file_name="cuticulome_filtered.csv",
    mime="text/csv"
)

st.markdown("---")
st.caption("Prototype by Alex Wardale — Powered by Streamlit.")
