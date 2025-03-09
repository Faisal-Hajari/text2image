"""
Image search page module for the Image Search App.

This module provides the search page functionality.
"""
import streamlit as st
from typing import List

from ui.components.search_bar import SearchBar
from ui.components.image_grid import ImageGrid
from ui.components.help_section import HelpSection
from services.search_service import ImageSearchInterface
from models.image_data import ImageDataStore
from config import AppConfig


class ImageSearchPage:
    """
    Image search page for the app.
    
    This class handles the image search functionality, displays search results,
    and allows users to select images.
    """
    
    def __init__(
        self, 
        config: AppConfig,
        search_service: ImageSearchInterface,
        data_store: ImageDataStore
    ) -> None:
        """
        Initialize the image search page.
        
        Args:
            config (AppConfig): Application configuration
            search_service (ImageSearchInterface): Service for searching images
            data_store (ImageDataStore): Store for clicked image data
        """
        self.config = config
        self.search_service = search_service
        self.data_store = data_store
        self.search_results: List[str] = []
        self.current_query = ""
        
        # Initialize components
        self.search_bar = SearchBar(
            self.handle_search,
            result_options=self.config.result_options,
            default_index=self.config.result_options.index(self.config.default_num_results)
        )
        self.image_grid = ImageGrid(self.handle_image_click)
        self.help_section = HelpSection()
    
    def handle_search(self, query: str, num_results: int) -> None:
        """
        Handle search requests.
        
        Args:
            query (str): Search query
            num_results (int): Number of results to display
        """
        self.current_query = query
        self.search_results = self.search_service.search(query, num_results)
    
    def handle_image_click(self, image_path: str, search_query: str) -> None:
        """
        Handle image click events.
        
        Args:
            image_path (str): Path to the clicked image
            search_query (str): Search query that produced the image
        """
        self.data_store.save_clicked_image(image_path, search_query)
    
    def render(self) -> None:
        """
        Render the image search page.
        """
        st.title("Image Search")
        
        # Render components
        query, num_results, search_clicked = self.search_bar.render()
        
        # Handle search if button clicked or query exists
        if search_clicked or query:
            if query:
                self.handle_search(query, num_results)
                if self.search_results:
                    self.image_grid.render(self.search_results, query, num_results)
            else:
                st.info("Please enter a search query")
        
        self.help_section.render()