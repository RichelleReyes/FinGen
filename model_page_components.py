import streamlit as st
import pandas as pd
import stTools as tools
import side_bar_components as side_bar
import plotly.express as px
import plotly.graph_objs as go
import numpy as np


def add_portfolio_risk_score(risk_score: float) -> None:
    # Define the color based on the risk score range
    if 0 <= risk_score <= 35:
        color = "green"
    elif 36 <= risk_score <= 75:
        color = "blue"
    elif 76 <= risk_score <= 100:
        color = "red"
    else:
        color = "black"  # Default color (if score is out of expected range)

    # Use Markdown to display the risk score with styled color
    st.markdown(f"<h3 style='color: {color};'>Portfolio Risk Score: {risk_score}</h3>", unsafe_allow_html=True)

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


risk_ratings = {'Stocks': 0.8, 'Bonds': 0.6, 'Real Estate': 0.2, 'Cash': 0.1}

def add_risk_profile_chart():
    # Sample data for portfolio composition (replace with your actual data)
    portfolio_data = {
        'Asset Class': ['Stocks', 'Bonds', 'Real Estate', 'Cash'],
        'Percentage': [st.session_state.stock_percentage, st.session_state.bonds_percentage, st.session_state.real_estate_percentage, st.session_state.cash_percentage]  # Example percentages (sums to 100%)
    }

    # Create a DataFrame from the portfolio data
    df_portfolio = pd.DataFrame(portfolio_data)

    # Add a new column for risk rating
    df_portfolio['Risk Rating'] = df_portfolio['Asset Class'].map(risk_ratings)

    # Create a bar chart to compare risk profiles
    st.subheader("Risk Profile by Asset Class")
    fig = px.bar(df_portfolio, x='Asset Class', y='Risk Rating', 
                 title='Risk Profile of Portfolio Assets',
                 color='Risk Rating')
    st.plotly_chart(fig)

def add_simulation_scenarios():
    st.subheader("Select Scenario:")
    selected_scenario = st.radio("Choose scenario:",
                                [None,
                                "Scenario 1: Economic downturn",
                                "Scenario 2: Market boom",
                                "Scenario 3: Global pandemic",
                                "Scenario 4: Market crash",])
    return selected_scenario

# Function to generate synthetic asset data for a given scenario
def generate_asset_data(scenario):
    # Define the number of days for which data will be generated
    num_days = 365
    
    # Initialize empty DataFrame to store asset data
    asset_data = pd.DataFrame({"Date": pd.date_range(start="2024-01-01", periods=num_days)})
    
    # Generate synthetic data based on the selected scenario
    if scenario == "Scenario 1: Economic downturn":
        # Generate synthetic data representing stock prices under economic downturn
        stock_prices = np.random.normal(loc=30, scale=3, size=num_days)  # Example synthetic data
        bond_prices = np.random.normal(loc=30, scale=3, size=num_days)  # Example synthetic data
        real_estate_prices = np.random.normal(loc=30, scale=3, size=num_days)  # Example synthetic data
        cash_values = np.random.normal(loc=30, scale=3, size=num_days)  # Example synthetic data
        
    elif scenario == "Scenario 2: Market boom":
        # Generate synthetic data representing stock prices under market boom
        stock_prices = np.random.normal(loc=250000, scale=10000, size=num_days)  # Example synthetic data
        bond_prices = np.random.normal(loc=250000, scale=10000, size=num_days)  # Example synthetic data
        real_estate_prices = np.random.normal(loc=250000, scale=10000, size=num_days)  # Example synthetic data
        cash_values = np.random.normal(loc=250000, scale=10000, size=num_days)  # Example synthetic data

    elif scenario == "Scenario 3: Global pandemic":
        # Generate synthetic data representing stock prices during a global pandemic
        stock_prices = np.random.normal(loc=900, scale=15, size=num_days)
        bond_prices = np.random.normal(loc=900, scale=15, size=num_days)
        real_estate_prices = np.random.normal(loc=900, scale=15, size=num_days)
        cash_values = np.random.normal(loc=900, scale=15, size=num_days)

    elif scenario == "Scenario 4: Market crash":
        # Generate synthetic data representing stock prices during a market crash
        stock_prices = np.random.normal(loc=160000, scale=3000, size=num_days)
        bond_prices = np.random.normal(loc=160000, scale=3000, size=num_days)
        real_estate_prices = np.random.normal(loc=160000, scale=3000, size=num_days)
        cash_values = np.random.normal(loc=160000, scale=3000, size=num_days)

        
    # Define similar synthetic data generation for other scenarios
    
    # Add asset data to the DataFrame
    asset_data["Stock_Price"] = stock_prices
    asset_data["Bond_Price"] = bond_prices
    asset_data["Real_Estate_Price"] = real_estate_prices
    asset_data["Cash_Value"] = cash_values
    
    return asset_data

def visualize_asset_data(asset_data):
    # Create a time series plot using Plotly
    fig = go.Figure()

    # Add traces for each asset
    fig.add_trace(go.Scatter(x=asset_data["Date"], y=asset_data["Stock_Price"], mode='lines', name='Stock Price', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=asset_data["Date"], y=asset_data["Bond_Price"], mode='lines', name='Bond Price', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=asset_data["Date"], y=asset_data["Real_Estate_Price"], mode='lines', name='Real Estate Price', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=asset_data["Date"], y=asset_data["Cash_Value"], mode='lines', name='Cash Value', line=dict(color='orange')))
    
    # Customize layout
    fig.update_layout(title='Asset Price Over Time',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      template='plotly_white')
    
    return fig

def add_markdown() -> None:
    st.markdown(
        """
        Please see below for your portfolio returns after risk simulation! 
        
        Caring about :green[risk management], :green[VaR], :green[CVaR], and :green[alpha] is like 
        putting on your gaming headset—it helps you play the investment game smarter, 
        protecting your money and aiming for a high score in the financial world.
        """
    )
