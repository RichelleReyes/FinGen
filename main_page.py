import streamlit as st
import side_bar as comp
import stTools as tools
import default_page
import model_page
import model_page_components as mpc

st.set_page_config(
    page_title="FinGEN",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

tools.remove_white_space()

comp.load_sidebar()

model_page.load_page()
