import streamlit as st
import pandas as pd
import stTools as tools
import side_bar_components as side_bar
import plotly.express as px

def add_portfolio_returns_graphs(portfolio_df: pd.DataFrame) -> None:
    tools.create_line_chart(portfolio_df)
    # st.line_chart(portfolio_df, use_container_width=True, height=500, width=250)


def add_download_button(df: pd.DataFrame) -> None:
    # convert my_portfolio_returns ndarray to dataframe
    df = pd.DataFrame(df)

    col1, col2, col3, col4 = st.columns(4)

    with col4:
        st.download_button(label="Download Portfolio Returns",
                           data=df.to_csv(),
                           file_name="Portfolio Returns.csv",
                           mime="text/csv")


def add_portfolio_risk_score(risk_score: float) -> None:
    st.header(f"Portfolio Risk Score: {risk_score}")

def calculate_score():
    stock_percentage_risk = 0.8
    bonds_percentage_risk = 0.6
    real_estate_percentage_risk = 0.2
    cash_percentage_risk = 0.1

    risk_score = (
        stock_percentage_risk * st.session_state.stock_percentage
        + bonds_percentage_risk * st.session_state.bonds_percentage
        + real_estate_percentage_risk * st.session_state.real_estate_percentage
        + cash_percentage_risk * st.session_state.cash_percentage
    )

    return risk_score

def add_portfolio_graph():
    # Sample data for portfolio composition (replace with your actual data)
    portfolio_data = {
        'Asset Class': ['Stocks', 'Bonds', 'Real Estate', 'Cash'],
        'Percentage': [st.session_state.stock_percentage, st.session_state.bonds_percentage, st.session_state.real_estate_percentage, st.session_state.cash_percentage]  # Example percentages (sums to 100%)
    }

    # Create a DataFrame from the portfolio data
    df_portfolio = pd.DataFrame(portfolio_data)

    # Display the portfolio composition as a pie chart using Plotly
    st.subheader("Current Portfolio Composition")
    fig = px.pie(df_portfolio, values='Percentage', names='Asset Class', 
                title='Portfolio Composition', 
                color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig)


def add_markdown() -> None:
    st.markdown(
        """
        Please see below for your portfolio returns after risk simulation! 
        
        Caring about :green[risk management], :green[VaR], :green[CVaR], and :green[alpha] is like 
        putting on your gaming headset—it helps you play the investment game smarter, 
        protecting your money and aiming for a high score in the financial world.
        """
    )
