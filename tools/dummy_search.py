import random 
import os   

class DummySearch(object):
    def __init__(self)->None:
        return None 
    
    def __call__(self, query:str, num_images:int=5)->list:
        return self.search(query, num_images)
    
    def search(self, query:str, num_images:int=5)->list:
        """
        Dummy search function that returns random images from a local folder.
        In the future, this would be replaced with actual search functionality.
        
        Args:
            query (str): The search query
            image_folder (str): Path to folder containing images
            
        Returns:
            list: List of image file paths
        """

         # Ensure the folder exists
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
            return []
        
        # Get all image files from the folder
        image_files = []
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        
        for file in os.listdir(image_folder):
            if any(file.lower().endswith(ext) for ext in valid_extensions):
                image_files.append(os.path.join(image_folder, file))
        
        # In a real search, you would filter based on query
        # For now, just return random images if any exist
        if not image_files:
            return []
        
        # Simulate "search" by shuffling and returning images
        cutoff = min(num_images, len(image_files))
        random.shuffle(image_files)[:cutoff]
        return image_files
