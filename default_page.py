import streamlit as st
import stTools as tools


def load_page():
    st.markdown(
        """
            Welcome to :green[FinGEN]! Explore this app to assess and simulate 
            your investment portfolio's risk effortlessly! :green[Risk management] is like 
            :blue[wearing a helmet while riding a bike]—it shields your money during investments. 
            It's a strategy set to understand uncertainties in stocks or bonds.

            Imagine your investment journey as a game; knowing rules and setbacks gives you a competitive edge. 
            :green[Value at Risk (VaR)] and :green[Conditional Value at Risk (CVaR)] aid in smart risk navigation, 
            keeping your game plan robust. Don't worry, I'll explain these concepts in a bit.
            
            
            """
    )

    st.subheader(f"About")
    st.markdown(
        """
            I'm :green[FinGEN], your financial risk management assistant. 
            I'm here to help you understand your portfolio's risk and how to manage it. 
            I'll guide you through the process of building your portfolio and assessing its risk. 
            Let's get started! 
            """
    )

    