import streamlit as st

import model_page_components
from chat import load_chat_window


def load_page() -> None:
    st.markdown(
        "<h2 style='color: #000; font-size: 3rem;'>Hello, Team</h2>",
        unsafe_allow_html=True,
    )

    # Call other components or functions in your module
    model_page_components.add_portfolio_risk_score(
        model_page_components.calculate_score()
    )
    if st.session_state["generate_analysis"]:  # Check if button is clicked
        model_page_components.add_portfolio_graph()
        model_page_components.add_risk_profile_chart()
    selected_scenario = model_page_components.add_simulation_scenarios()

    if selected_scenario is not None:
        # st.session_state["generate_analysis"] = False
        asset_data = model_page_components.generate_asset_data(selected_scenario)
        st.plotly_chart(model_page_components.visualize_asset_data(asset_data))
        load_chat_window()
