import streamlit as st

st.set_page_config(
    page_title="Kalkulator Analisis Kuantitatif",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');
 
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
 
.main > div {
    padding-top: 2rem;
    padding-bottom: 3rem;
}
 
.badge {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #5F5E5A;
    border: 1px solid #D3D1C7;
    border-radius: 999px;
    padding: 4px 14px;
    margin-bottom: 1rem;
}
 
.main-title {
    font-family: 'DM Serif Display', serif;
    font-size: 42px;
    line-height: 1.15;
    color: #1a1a1a;
    margin: 0 0 0.5rem;
}
 
.main-title em {
    font-style: italic;
    color: #1D9E75;
}
 
.subtitle {
    font-size: 15px;
    color: #6b6b6b;
    line-height: 1.6;
    max-width: 560px;
    margin-bottom: 2rem;
}
 
.divider {
    border: none;
    border-top: 1px solid #e8e8e8;
    margin: 0.5rem 0 2rem;
}
 
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #9a9a9a;
    margin-bottom: 1rem;
}
 
.module-card {
    background: #ffffff;
    border: 1px solid #e8e8e8;
    border-radius: 14px;
    padding: 1.4rem 1.4rem 1.1rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, transform 0.15s;
    height: 100%;
    cursor: pointer;
}
 
.module-card:hover {
    border-color: #aaa;
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
}
 
.card-accent {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 14px 14px 0 0;
}
 
.card-icon {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    margin-bottom: 0.9rem;
}
 
.card-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.06em;
    color: #b0b0b0;
    margin: 0 0 4px;
}
 
.card-title {
    font-size: 15px;
    font-weight: 500;
    color: #1a1a1a;
    margin: 0 0 7px;
    line-height: 1.3;
}
 
.card-desc {
    font-size: 13px;
    color: #7a7a7a;
    line-height: 1.55;
    margin: 0 0 1rem;
}
 
.tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}
 
.tag {
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    padding: 2px 9px;
    border-radius: 999px;
    border: 1px solid #e0e0e0;
    color: #7a7a7a;
}
 
.footer-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 1.5rem;
    border-top: 1px solid #e8e8e8;
    margin-top: 1rem;
}
 
.footer-text {
    font-size: 12px;
    color: #b0b0b0;
}
 
.footer-text b {
    color: #6b6b6b;
}
 
.formula-box {
    background: #f7f9fc;
    border: 1px solid #e0eaf5;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #185FA5;
    text-align: center;
    letter-spacing: 0.04em;
    margin-top: 0.5rem;
}
 
/* Streamlit button override */
div.stButton > button {
    background: transparent;
    border: 1px solid #d0d0d0;
    border-radius: 10px;
    color: #1a1a1a;
    font-size: 13px;
    font-weight: 500;
    padding: 8px 20px;
    transition: background 0.15s;
}
div.stButton > button:hover {
    background: #f5f5f5;
    border-color: #aaa;
    color: #1a1a1a;
}
</style>
