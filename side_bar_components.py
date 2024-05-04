import streamlit as st
import stTools as tools
import datetime as dt
import random


def load_sidebar_investment_percentage(port_tab: st.sidebar.tabs) -> None:
    st.session_state["stock_percentage"] = port_tab.number_input("Enter Stock Percentage",
                                                     key="side_bar_stock_percentage")
    st.session_state["bonds_percentage"] = port_tab.number_input("Enter Bonds Percentage",
                                                     key="side_bar_bonds_percentage")
    st.session_state["real_estate_percentage"] = port_tab.number_input("Enter Real Estate Percentage",
                                                     key="side_bar_real_estate_percentage")
    st.session_state["cash_percentage"] = port_tab.number_input("Enter Cash Percentage",
                                                     key="side_bar_cash_percentage")


def load_sidebar_goals(port_tab: st.sidebar.tabs) -> None:
    st.session_state["goal"] = port_tab.selectbox("Select Goal",
                                                           ["Growth", "Income", "Wealth Preservation"],
                                                           index=0,
                                                           key="side_bar_portfolio_name")

def load_sidebar_risk_tolerance(port_tab: st.sidebar.tabs) -> None:
    # Map text labels to numerical values
    risk_tolerance_mapping = {
        "Conservative": 1,
        "Medium": 2,
        "Aggresive": 3
    }

    # Display the slider with text options
    selected_risk_tolerance = port_tab.select_slider(
        "Risk Tolerance",
        options=list(risk_tolerance_mapping.keys()),
        format_func=lambda option: option  # Display text labels as-is
    )

    # Retrieve the numerical value corresponding to the selected text option
    risk_tolerance_value = risk_tolerance_mapping[selected_risk_tolerance]

    # Store the selected risk tolerance value in session state
    st.session_state["risk_tolerance_value"] = risk_tolerance_value


def load_sidebar_timeframe(port_tab: st.sidebar.tabs) -> None:
    # Map text labels to numerical values
    timeframe_mapping = {
        "Short-term": 1,
        "Medium-term": 2,
        "Long-term": 3
    }

    # Display the slider with text options
    selected_timeframe = port_tab.select_slider(
        "Time Frame",
        options=list(timeframe_mapping.keys()),
        format_func=lambda option: option  # Display text labels as-is
    )

    # Retrieve the numerical value corresponding to the selected text option
    timeframe_value = timeframe_mapping[selected_timeframe]

    # Store the selected timeframe value in session state
    st.session_state["timeframe_value"] = timeframe_value