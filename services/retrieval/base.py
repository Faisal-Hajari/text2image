class BaseRetrival(object): 
    def __init__(self, *args, **kwargs)->None:
        return None 
    
    def insert(self, *args, **kwargs):

        raise NotImplementedError("insert is not implemented")
    
    def search(self, query:str, image_store:list[str])->tuple[str, list[str]]: 
        """
        Search for the query in the image store
        
        args: 
            - query[str]: the search term.
            - image_store[list[str]]: list of image paths
        returns:
            - query[str]: the search term.
            - image_store[list[str]]: list of image paths after filtering
        """
        raise NotImplementedError("search is not implemented")

    def __call__(self, query, image_store):
        return self.search(query, image_store)

    
    def image_embedding(self, image:str): 
        raise NotImplementedError("image_embedding is not implemented")