import torch 
from torch import Tensor
import numpy as np 

from .base import BaseDB
from services.metrics.base_metrics import BaseMetric


class RamDB(BaseDB): 
    def __init__(self, metric:BaseMetric,)->None:
        self.db:dict = {}
        self.metric = metric
        
           
    def search(self, query: Tensor)->list[str]:
        """searches for query in the db using the metric"""
        if self.metric is None: 
            raise ValueError("metric is not set")
        images = list(self.db.keys())
        image_vectors = list(self.db.values())
        idx = self.metric(query, torch.stack(image_vectors))
        images = np.array(images)[idx]
        return images.tolist()
                
    
    def insert(self, image: str, image_vector: Tensor, cache:bool=True) -> None:
        """inserts an image into the cache"""
        if image not in self.db or not cache:
            self.db[image] = image_vector 