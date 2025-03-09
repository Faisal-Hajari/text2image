"""
Navigation module for the Image Search App.

This module provides sidebar navigation with tabs and action buttons.
"""
import streamlit as st
from typing import Dict, Callable, Any


class Navigation:
    """
    Navigation component for the image search app.
    
    This component renders a sidebar with tabs and action buttons,
    allowing the user to navigate between different pages of the app.
    """
    
    def __init__(
        self, 
        title: str = "Navigation",
        tabs: Dict[str, Callable[[], None]] = None,
        buttons: Dict[str, Callable[[], None]] = None
    ) -> None:
        """
        Initialize the navigation component.
        
        Args:
            title (str): Title for the navigation sidebar
            tabs (Dict[str, Callable[[], None]]): Dictionary mapping tab names to page functions
            buttons (Dict[str, Callable[[], None]]): Dictionary mapping button names to action functions
        """
        self.title = title
        self.tabs = tabs or {}
        self.buttons = buttons or {}
    
    def render(self) -> None:
        """
        Render the navigation sidebar and execute the selected page function.
        """
        st.sidebar.title(self.title)
        
        # Render action buttons
        for name, func in self.buttons.items():
            if st.sidebar.button(name):
                func()
        
        # Render tabs and select the active one
        if self.tabs:
            app_tab = st.sidebar.radio("Select Page", list(self.tabs.keys()))
            
            # Call the function associated with the selected tab
            self.tabs[app_tab]()
    
    def add_tab(self, name: str, func: Callable[[], None]) -> None:
        """
        Add a tab to the navigation.
        
        Args:
            name (str): Name of the tab
            func (Callable[[], None]): Function to call when the tab is selected
        """
        self.tabs[name] = func
    
    def add_button(self, name: str, func: Callable[[], None]) -> None:
        """
        Add an action button to the navigation.
        
        Args:
            name (str): Name of the button
            func (Callable[[], None]): Function to call when the button is clicked
        """
        self.buttons[name] = func


def custom_sidebar_style() -> None:
    """
    Apply custom CSS to reduce sidebar width and style the app.
    """
    st.markdown(
        """
        <style>
        /* Reduce sidebar width */
        .css-1d391kg {
            width: 180px;
        }
        .css-1d391kg .css-1q8dd3e {
            width: 180px;
        }
        .css-1d391kg .css-1v3fz7d {
            width: 180px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )