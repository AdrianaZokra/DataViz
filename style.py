import streamlit as st
import toml

with open('theme_config.toml', 'r') as config_file:
    theme_config = toml.load(config_file)

def set_style():
    return st.markdown(
        f"""
    <style>
    .stApp {{
        background-color: {theme_config['theme']['backgroundColor']};
        font-family: {theme_config['theme']['font']};
    }}
    .stButton {{
        background-color: {theme_config['theme']['primaryColor']};
    }}
    </style>
    """,
        unsafe_allow_html=True
    )
