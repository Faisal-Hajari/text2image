"""
Application state module for the Image Search App.

This module provides utilities for managing application state.
"""
import streamlit as st


def initialize_session_state() -> None:
    """
    Initialize the Streamlit session state with default values.
    """
    if 'search_history' not in st.session_state:
        st.session_state.search_history = []
    
    if 'last_query' not in st.session_state:
        st.session_state.last_query = ""


def clear_search_history() -> None:
    """
    Clear the search history from the session state.
    """
    st.session_state.search_history = []
    st.session_state.last_query = ""