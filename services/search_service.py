"""
Search service module for the Image Search App.

This module provides the interface and implementations for image search functionality.
"""
import os
import random
from abc import ABC, abstractmethod
from typing import List


class ImageSearchInterface(ABC):
    """Interface for image search functionality."""
    
    @abstractmethod
    def search(self, query: str, num_results: int = 5) -> List[str]:
        """
        Search for images based on a query.
        
        Args:
            query (str): Search query
            num_results (int): Maximum number of results to return
            
        Returns:
            List[str]: List of image file paths
        """
        pass


class DummyImageSearch(ImageSearchInterface):
    """
    Dummy implementation of image search that returns random images.
    
    This class simulates a search functionality by returning random
    images from a specified folder.
    """
    
    def __init__(self, image_folder: str) -> None:
        """
        Initialize the dummy image search.
        
        Args:
            image_folder (str): Path to folder containing images
        """
        self.image_folder = image_folder
    
    def search(self, query: str, num_results: int = 5) -> List[str]:
        """
        Dummy search function that returns random images from a local folder.
        
        Args:
            query (str): The search query
            num_results (int): Maximum number of results to return
            
        Returns:
            List[str]: List of image file paths
        """
        # Ensure the folder exists
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
            return []
        
        # Get all image files from the folder
        image_files = []
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        
        for file in os.listdir(self.image_folder):
            if any(file.lower().endswith(ext) for ext in valid_extensions):
                image_files.append(os.path.join(self.image_folder, file))
        
        # Simulate "search" by shuffling and returning images
        if not image_files:
            return []
        
        random.shuffle(image_files)
        return image_files[:min(num_results, len(image_files))]