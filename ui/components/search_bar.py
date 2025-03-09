"""
Search bar component for the Image Search App.

This module provides a UI component for the search functionality.
"""
import streamlit as st
from typing import List, Callable, Tuple


class SearchBar:
    """
    Search bar component for the image search app.
    
    This component renders a search input field, options for the
    number of results to display, and a search button.
    """
    
    def __init__(
        self, 
        search_callback: Callable[[str, int], None],
        result_options: List[int] = None, 
        default_index: int = 1
    ) -> None:
        """
        Initialize the search bar component.
        
        Args:
            search_callback (Callable[[str, int], None]): Callback function for search
            result_options (List[int], optional): Options for number of results to display
            default_index (int): Default index in the result options list
        """
        self.search_callback = search_callback
        self.result_options = result_options or [1, 5, 10]
        self.default_index = default_index
    
    def render(self) -> Tuple[str, int, bool]:
        """
        Render the search bar component.
        
        Returns:
            Tuple[str, int, bool]: Tuple containing the search query, 
                                  number of results, and whether search button was clicked
        """
        search_query = st.text_input("Enter your search query:", key="search_input")
        
        num_results = st.selectbox(
            "Number of results to display:",
            options=self.result_options,
            index=self.default_index
        )
        
        search_clicked = st.button("Search")
        
        return search_query, num_results, search_clicked