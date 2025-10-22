import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Cuticulome.db", page_icon="🐜")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/proteins.csv")

df = load_data()

# Title and intro
st.title("🐜 Cuticulome.db — Prototype")
st.markdown("""
A **database of arthropod cuticular proteins**, built to centralize and simplify access to molecular,
functional, and expression information across taxa.

Use the sidebar filters below to explore the data, or switch pages to:
- 🧭 Learn more on the **Help** page  
- 📊 See database summaries in **Statistics**  
- 📫 Find team contacts in **Contact**
""")

# Sidebar filters
st.sidebar.header("Filter Proteins")
species = st.sidebar.multiselect("Select Species", sorted(df["Species"].unique()))
function = st.sidebar.text_input("Search Function Keyword")

# Apply filters
filtered_df = df.copy()
if species:
    filtered_df = filtered_df[filtered_df["Species"].isin(species)]
if function:
    filtered_df = filtered_df[filtered_df["Function"].str.contains(function, case=False, na=False)]

# Display results
st.subheader("Filtered Results")
st.dataframe(filtered_df, use_container_width=True)

# Download button
st.download_button(
    label="⬇️ Download filtered data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="cuticulome_filtered.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.caption("Prototype by Alex Wardale — powered by Streamlit. Navigate using the sidebar.")

