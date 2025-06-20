import streamlit as st
from data_loader import load_data
from charts import (
    valuation_bar_chart,
    growth_scatter_plot,
    funding_per_employee_chart,
    valuation_per_employee_chart,
    headcount_vs_valuation_chart,
    funding_vs_founding_year
)

import base64
from pathlib import Path

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title='Seekr vs Peers | Analytics',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# ---- BACKGROUND IMAGE (BASE64) ----
def set_bg_from_local(png_file):
    with open(png_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    bg_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

set_bg_from_local("pure.webp")

# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        .caption-text {
            font-size: 0.9rem;
            color: #BBBBBB;
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .stTabs [data-baseweb="tab-list"] {
            margin-bottom: 20px;
        }
        h1, h2, h3 {
            color: #FAFAFA;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---- TITLE & INTRO ----
st.title("🧠 Seekr vs the AI World")
st.markdown("A deep-dive into how **Seekr** compares to the top players in the AI startup ecosystem using publicly available data.")

# ---- LOAD DATA ----
df = load_data()

# ---- CHART TABS ----
tabs = st.tabs([
    "📈 Growth vs Funding",
    "💸 Capital Intensity",
    "👥 Headcount vs Valuation",
    "📅 Year Founded vs Funding",
    "🏆 Valuation Leaders"
])

with tabs[0]:
    st.header("Growth vs Funding")
    st.plotly_chart(growth_scatter_plot(df), use_container_width=True)
    st.markdown('<div class="caption-text">Each company’s funding is compared against its employee growth rate. Seekr appears as a high-growth, well-funded outlier.</div>', unsafe_allow_html=True)

with tabs[1]:
    st.header("Capital Intensity")
    st.plotly_chart(funding_per_employee_chart(df), use_container_width=True)
    st.plotly_chart(valuation_per_employee_chart(df), use_container_width=True)
    st.markdown('<div class="caption-text">These charts assess capital intensity by dividing funding and valuation by headcount.</div>', unsafe_allow_html=True)

with tabs[2]:
    st.header("Headcount vs Valuation")
    st.plotly_chart(headcount_vs_valuation_chart(df), use_container_width=True)
    st.markdown('<div class="caption-text">This scatter plot shows how company valuations correlate with team size.</div>', unsafe_allow_html=True)

with tabs[3]:
    st.header("Funding vs Founding Year")
    st.plotly_chart(funding_vs_founding_year(df), use_container_width=True)
    st.markdown('<div class="caption-text">Visualizing the speed of fundraising relative to founding date.</div>', unsafe_allow_html=True)

with tabs[4]:
    st.header("Valuation Leaders")
    st.plotly_chart(valuation_bar_chart(df), use_container_width=True)
    st.markdown('<div class="caption-text">This chart ranks the top 10 companies by valuation.</div>', unsafe_allow_html=True)
