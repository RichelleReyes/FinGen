import streamlit as st
import stTools as tools
import side_bar_components


def load_sidebar() -> None:
    # inject custom CSS to set the width of the sidebar
    tools.create_side_bar_width()

    st.sidebar.markdown("<h2 style='text-align: center; color: #000; font-size: 4rem;'>FinGEN</h2>", unsafe_allow_html=True)

    # add portfolio tab components
    st.sidebar.title("Portfolio Building")
    side_bar_components.load_sidebar_investment_percentage(st.sidebar)
    side_bar_components.load_sidebar_goals(st.sidebar)
    side_bar_components.load_sidebar_risk_tolerance(st.sidebar)
    side_bar_components.load_sidebar_timeframe(st.sidebar)
    
    st.session_state["generate_analysis"] = st.sidebar.button("Generate Analysis",
                                                           key="side_bar_load_portfolio",
                                                           on_click=tools.click_button_port)
