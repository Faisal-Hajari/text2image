"""
Image grid component for the Image Search App.

This module provides a UI component for displaying images in a grid layout.
"""
import streamlit as st
from typing import List, Callable
from PIL import Image


class ImageGrid:
    """
    Component for displaying images in a grid layout.
    
    This component renders images in a grid and provides buttons
    for selecting images.
    """
    
    def __init__(self, image_click_callback: Callable[[str, str], None]) -> None:
        """
        Initialize the image grid component.
        
        Args:
            image_click_callback (Callable[[str, str], None]): Callback function for image clicks
        """
        self.image_click_callback = image_click_callback
    
    def render(self, image_paths: List[str], search_query: str, num_results: int) -> None:
        """
        Render the image grid component.
        
        Args:
            image_paths (List[str]): List of image file paths
            search_query (str): Current search query
            num_results (int): Number of results to display
        """
        if not image_paths:
            st.warning("No images found. Please add images to the 'images' folder.")
            return
        
        # Limit results based on dropdown selection
        results = image_paths[:min(num_results, len(image_paths))]
        
        # Display images in a grid
        cols = 3 if num_results > 3 else num_results
        
        # Create columns for displaying images
        image_cols = st.columns(cols)
        
        # Display each image with a click button
        for i, img_path in enumerate(results):
            col_index = i % cols
            with image_cols[col_index]:
                try:
                    img = Image.open(img_path)
                    st.image(img, use_container_width=True)
                    
                    # Button to "click" on the image
                    if st.button(f"Select", key=f"btn_{i}"):
                        self.image_click_callback(img_path, search_query)
                        st.success(f"Image saved to clicked_images.json!")
                except Exception as e:
                    st.error(f"Error displaying image: {e}")