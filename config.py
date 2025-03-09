"""
Configuration module for the Image Search App.

This module contains the configuration settings used across the application.
"""
from typing import List


class AppConfig:
    """Application configuration for the Image Search App."""
    
    def __init__(
        self, 
        page_title: str = "Image Search App", 
        layout: str = "centered",
        json_file: str = "clicked_images.json", 
        image_folder: str = "images",
        default_num_results: int = 5,
        result_options: List[int] = None
    ) -> None:
        """
        Initialize application configuration.
        
        Args:
            page_title (str): Title of the web page
            layout (str): Streamlit layout type
            json_file (str): Path to the JSON file for storing clicked images
            image_folder (str): Path to the folder containing images
            default_num_results (int): Default number of search results to display
            result_options (List[int], optional): Options for number of results to display
        """
        self.page_title = page_title
        self.layout = layout
        self.json_file = json_file
        self.image_folder = image_folder
        self.default_num_results = default_num_results
        self.result_options = result_options or [1, 5, 10]