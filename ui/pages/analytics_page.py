"""
Analytics page module for the Image Search App.

This module provides analytics for image search data.
"""
import streamlit as st
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

from models.image_data import ImageDataStore


class AnalyticsPage:
    """
    Analytics page for the app.
    
    This class displays analytics and insights based on image search data.
    """
    
    def __init__(self, data_store: ImageDataStore) -> None:
        """
        Initialize the analytics page.
        
        Args:
            data_store (ImageDataStore): Store for clicked image data
        """
        self.data_store = data_store
    
    def _get_analytics_data(self) -> Tuple[Dict[str, int], Dict[str, int]]:
        """
        Process and extract analytics data from the image store.
        
        Returns:
            Tuple[Dict[str, int], Dict[str, int]]: Image counts and query counts
        """
        # Load data
        data = self.data_store._load_data()
        
        if not data:
            return {}, {}
        
        # Count images by query
        query_counts: Dict[str, int] = {}
        for image_name, queries in data.items():
            for query in queries:
                if query in query_counts:
                    query_counts[query] += 1
                else:
                    query_counts[query] = 1
        
        # Count images
        image_counts = {img: len(queries) for img, queries in data.items()}
        
        return image_counts, query_counts
    
    def render(self) -> None:
        """
        Render the analytics page.
        """
        st.title("Search Analytics")
        
        image_counts, query_counts = self._get_analytics_data()
        
        if not image_counts and not query_counts:
            st.info("No search data available yet. Try searching and clicking on some images first.")
            return
        
        # Display top queries
        st.subheader("Top Search Queries")
        if query_counts:
            query_df = pd.DataFrame(
                {"Query": list(query_counts.keys()), "Count": list(query_counts.values())}
            ).sort_values("Count", ascending=False)
            
            st.dataframe(query_df)
            
            # Create a bar chart for queries
            fig, ax = plt.subplots(figsize=(10, 6))
            top_queries = query_df.head(10)
            ax.bar(top_queries["Query"], top_queries["Count"])
            ax.set_title("Top 10 Search Queries")
            ax.set_xlabel("Query")
            ax.set_ylabel("Count")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("No query data available.")
        
        # Display top clicked images
        st.subheader("Top Clicked Images")
        if image_counts:
            image_df = pd.DataFrame(
                {"Image": list(image_counts.keys()), "Clicks": list(image_counts.values())}
            ).sort_values("Clicks", ascending=False)
            
            st.dataframe(image_df)
        else:
            st.info("No image click data available.")