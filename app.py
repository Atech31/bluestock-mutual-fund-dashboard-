import streamlit as st

st.set_page_config(page_title="Bluestock Mutual Fund Analytics", layout="wide")

st.title("📊 Bluestock Mutual Fund Analytics Dashboard")
st.write("Interactive Mutual Fund Performance, Risk Metrics, and Industry Overview")

# Paste your Power BI iFrame Embed URL below
powerbi_embed_url = "PASTE_YOUR_POWER_BI_EMBED_URL_HERE"

st.components.v1.iframe(powerbi_embed_url, height=800, scrolling=True)
