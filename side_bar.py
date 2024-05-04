import streamlit as st
import stTools as tools
import side_bar_components


def load_sidebar() -> None:
    # inject custom CSS to set the width of the sidebar
    tools.create_side_bar_width()

    st.sidebar.markdown("<h2 style='text-align: center; color: #FF4B4B; font-size: 4rem;'>FinGEN</h2>", unsafe_allow_html=True)

    # add portfolio tab components
    st.sidebar.markdown("<h2 style='text-align: center; color: #000; font-size: 2rem;'>Portfolio Building</h2>", unsafe_allow_html=True)
    st.sidebar.title("Assets")
    side_bar_components.load_sidebar_investment_percentage(st.sidebar)
    st.sidebar.title("Goal")
    side_bar_components.load_sidebar_goals(st.sidebar)
    st.sidebar.title("Risk Tolerance")
    side_bar_components.load_sidebar_risk_tolerance(st.sidebar)
    st.sidebar.title("Time Frame")
    side_bar_components.load_sidebar_timeframe(st.sidebar)
    
    if "percentage_valid" in st.session_state:
        st.session_state["generate_analysis"] = st.sidebar.button("Generate Analysis",
                                                           key="side_bar_load_portfolio",
                                                           on_click=tools.click_button_port)
