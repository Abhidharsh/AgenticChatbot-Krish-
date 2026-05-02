import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlistUI


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlist UI.
    This function initialized the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.
    """

    ## Load UI
    UI = LoadStreamlistUI()
    user_input = UI.load_streamlistui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Enter your message:")
