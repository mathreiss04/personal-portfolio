import streamlit as st
from about import render_about
from projects import render_projects
# Page configuration
st.set_page_config(layout="wide", page_title="Portfolio")

# Side menu "sidebar"
menu = st.sidebar.radio( 
    'Menu', 
    options=["About Me 🔍", "Projects 🚀"])

# Dictionary to map menu options to rendering functions
menu_functions = {
    "About Me 🔍": render_about, 
    "Projects 🚀": render_projects
}

# Render the selected page
menu_functions[menu]()