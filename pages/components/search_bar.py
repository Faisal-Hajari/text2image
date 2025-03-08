import streamlit as st
import os
import json
import random
from PIL import Image
from typing import List 

class SearchBar(): 
    def __init__(self, number_of_results:List[int]= [1, 5, 10], number_of_results_default_index:int=1)->None:
        self.number_of_results = number_of_results
        self.number_of_results_default_index = number_of_results_default_index
        return None
    
    def search_bar(self)->None: 
        # search bar
        search_query = st.text_input("Enter your search query:", key="search_input")
        num_results = st.selectbox(
            "Number of results to display:",
            options=self.number_of_results,
            index=self.number_of_results_default_index  # Default to 5                 
        )
        if st.button("Search") or search_query:
            if search_query:
                # Get search results
                results = search_images(search_query)
                
                if not results:
                    st.warning("No images found. Please add images to the 'images' folder.")
                else:
                    # Limit results based on dropdown selection
                    results = results[:min(num_results, len(results))]
                    
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
                                    save_clicked_image(img_path, search_query)
                                    st.success(f"Image saved to clicked_images.json!")
                            except Exception as e:
                                st.error(f"Error displaying image: {e}")
            else:
                st.info("Please enter a search query")
