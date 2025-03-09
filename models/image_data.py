"""
Image data module for the Image Search App.

This module handles the storage and retrieval of image click data.
"""
import os
import json
from typing import Dict, List


class ImageDataStore:
    """
    Handles storage and retrieval of image click data.
    
    This class provides methods to save and retrieve information about
    clicked images and their associated search queries.
    """
    
    def __init__(self, json_file: str) -> None:
        """
        Initialize the image data store.
        
        Args:
            json_file (str): Path to the JSON file for storing clicked images
        """
        self.json_file = json_file
    
    def save_clicked_image(self, image_path: str, search_query: str) -> None:
        """
        Save information about clicked images to a JSON file.
        
        Args:
            image_path (str): Path to the clicked image
            search_query (str): The search query that produced this image
        """
        image_name = os.path.basename(image_path)
        
        # Load existing data or create new
        data = self._load_data()
        
        # Update data
        if image_name not in data:
            data[image_name] = []
        
        # Add search query to the list if not already present
        if search_query not in data[image_name]:
            data[image_name].append(search_query)
        
        # Save updated data
        self._save_data(data)
    
    def _load_data(self) -> Dict[str, List[str]]:
        """
        Load image data from JSON file.
        
        Returns:
            Dict[str, List[str]]: Dictionary mapping image names to search queries
        """
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}
    
    def _save_data(self, data: Dict[str, List[str]]) -> None:
        """
        Save image data to JSON file.
        
        Args:
            data (Dict[str, List[str]]): Dictionary mapping image names to search queries
        """
        with open(self.json_file, 'w') as f:
            json.dump(data, f, indent=4)