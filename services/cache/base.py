from torch import Tensor

class BaseCache(object):
    def __init__(self, *args, **kwargs): 
        pass 

    def __call__(self, query:list[Tensor], image_store:list[str], embedding_fn:callable):
        """takes in a query vector and a list of images. the cache
        check if all images in the store is in the caches if not
        it adds them to the cache, then it returns the image vectors of the 
        relative images."""
        pass 
    
    def insert(self, embedding:callable, collection:str):
        pass 
    