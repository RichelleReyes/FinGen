import streamlit as st


def load_chat_window():
    messages = st.container()

    # Predefined conversation
    conversation = [
        ("assistant", "Welcome to the chat! How can I assist you today?"),
        ("user", "Based on my portfolio, what are some good investment options?"),
        (
            "assistant",
            "Taking into account your risk score and your long term goals, I'd recommend investing in a global index fund like VWRA, which places your assets in a diversified index which would steadely make passive income for the following decades.",
        ),
        ("user", "Where can I start investing in VWRA?"),
        (
            "assistant",
            "A good place to start it's GBM+, which is a platform that allows you to invest in a wide range of assets, including VWRA.",
        ),
    ]

    for sender, message in conversation:
        messages.chat_message(sender).write(message)

    # if prompt := st.chat_input("Say something"):
    #     messages.chat_message("user").write(prompt)
    #     messages.chat_message("assistant").write(f"Echo: {prompt}")
