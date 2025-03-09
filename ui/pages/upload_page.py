"""
Upload page module for the Image Search App.

This module provides functionality for uploading new images.
"""
import streamlit as st
import os
import shutil
from typing import List
from PIL import Image
import io

from config import AppConfig


class UploadPage:
    """
    Upload page for the app.
    
    This class allows users to upload new images to the system.
    """
    
    def __init__(self, config: AppConfig) -> None:
        """
        Initialize the upload page.
        
        Args:
            config (AppConfig): Application configuration
        """
        self.config = config
        self.image_folder = config.image_folder
    
    def _save_uploaded_image(self, uploaded_file) -> str:
        """
        Save an uploaded image to the images folder.
        
        Args:
            uploaded_file: Streamlit uploaded file object
            
        Returns:
            str: Path to the saved image
        """
        # Ensure the image folder exists
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
        
        # Save the file
        file_path = os.path.join(self.image_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return file_path
    
    def render(self) -> None:
        """
        Render the upload page.
        """
        st.title("Upload Images")
        
        st.write("Upload new images to include in search results.")
        
        uploaded_files = st.file_uploader(
            "Choose images to upload", 
            type=["jpg", "jpeg", "png", "gif"],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            saved_paths = []
            
            for uploaded_file in uploaded_files:
                try:
                    # Save the image
                    file_path = self._save_uploaded_image(uploaded_file)
                    saved_paths.append(file_path)
                    
                    # Display a success message
                    st.success(f"Saved: {uploaded_file.name}")
                except Exception as e:
                    st.error(f"Error saving {uploaded_file.name}: {e}")
            
            # Display the uploaded images
            if saved_paths:
                st.subheader("Uploaded Images:")
                
                # Display in a 3-column grid
                cols = st.columns(3)
                
                for i, img_path in enumerate(saved_paths):
                    col_index = i % 3
                    with cols[col_index]:
                        try:
                            img = Image.open(img_path)
                            st.image(img, caption=os.path.basename(img_path), use_column_width=True)
                        except Exception as e:
                            st.error(f"Error displaying image: {e}")