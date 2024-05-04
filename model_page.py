import streamlit as st
import stTools as tools
from models.MonteCarloSimulator import Monte_Carlo_Simulator
import model_page_components

def load_page() -> None:
    st.markdown("<h2 style='color: #000; font-size: 3rem;'>Hello, Team</h2>", unsafe_allow_html=True)
    
    # Call other components or functions in your module
    model_page_components.add_portfolio_risk_score(model_page_components.calculate_score())
    model_page_components.add_portfolio_graph()




