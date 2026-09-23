"""Karuna M Naik — portfolio entry point."""
import streamlit as st

from components.helpers import load_css
from components.layout import footer, hero, nav
from components.sections import (about, contact, education, experience,
                                 projects, resume, skills)

st.set_page_config(
    page_title="Karuna M Naik | Python & Full-Stack Developer",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()
nav()
hero()
about()
projects()
experience()
skills()
education()
resume()
contact()
footer()
