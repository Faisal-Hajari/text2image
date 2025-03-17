
import torch 
from torch import Tensor

from .base import BaseCache

class RamCache(BaseCache): 
    def __inti__(self):
        self.cache:dict = {} 
    
    def __call__(self, query:list[Tensor], image_store:list[str], embedding_fn:callable)->list[Tensor]:
        """takes in a query vector and a list of images. the cache
        check if all images in the store is in the caches if not
        it adds them to the cache, then it returns the image vectors of the 
        relative images."""
        cached_images = self.cache.keys()
        new_images = list(set(image_store) - set(cached_images)) 
        for image in new_images: 
            image_embedding = embedding_fn(image)
            self.cache[image] = image_embedding
        return [self.cache[image] for image in image_store]         
    
    def insert(self, embedding_fn:callable, collection:str):
        pass 