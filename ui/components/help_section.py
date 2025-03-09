"""
Help section component for the Image Search App.

This module provides a UI component for displaying help information.
"""
import streamlit as st


class HelpSection:
    """
    Component for displaying help information.
    
    This component renders an expandable section with usage instructions.
    """
    
    def render(self) -> None:
        """
        Render the help section component.
        
        Displays an expander with instructions on how to use the app.
        """
        with st.expander("How to use this app"):
            st.markdown("""
            1. Enter your search query in the search bar
            2. Select how many images you want to see (1, 5, or 10)
            3. Click the "Search" button
            4. Click the "Select" button under any image you're interested in
            5. The selected images will be saved to a JSON file with your search query
            
            Note: For this demo, add some image files to a folder named "images" in the same directory as this app.
            """)