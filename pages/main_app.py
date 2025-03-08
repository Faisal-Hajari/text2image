import streamlit as st
import os
import json
import random
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Image Search App",
    layout="centered"
)

# Function to save clicked image data to JSON


# Main app layout
st.title("Image Search App")

# Search bar
search_query = st.text_input("Enter your search query:", key="search_input")

# Number of results dropdown
num_results = st.selectbox(
    "Number of results to display:",
    options=[1, 5, 10],
    index=1  # Default to 5                       
)

# Search button
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

# Instructions for first-time users
with st.expander("How to use this app"):
    st.markdown("""
    1. Enter your search query in the search bar
    2. Select how many images you want to see (1, 5, or 10)
    3. Click the "Search" button
    4. Click the "Select" button under any image you're interested in
    5. The selected images will be saved to a JSON file with your search query
    
    Note: For this demo, add some image files to a folder named "images" in the same directory as this app.
    """)


class LandingPage: 
    def __init__(self, json_file:str="clicked_images.json", image_folder:str="images")->None:
        self.json_file = json_file
        self.image_folder = image_folder    

    def _save_clicked_image(self, image_path, search_query):
        """
        Save information about clicked images to a JSON file.
        
        Args:
            image_path (str): Path to the clicked image
            search_query (str): The search query that produced this image
        """
        json_file = "clicked_images.json"
        image_name = os.path.basename(image_path)
        
        # Load existing data or create new
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}
        
        # Update data
        if image_name not in data:
            data[image_name] = []
        
        # Add search query to the list if not already present
        if search_query not in data[image_name]:
            data[image_name].append(search_query)
        
        # Save updated data
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
    

    def run_page(): 
        # Page config 
        st.set_page_config(
            page_title="Image Search App",
            layout="centered"
        )
        st.title("Image Search App")

        
