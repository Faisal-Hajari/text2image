from torch import Tensor
from services.metrics.base_metrics import BaseMetric
from typing import Optional


class BaseDB(object):
    def __init__(self, metric:Optional[BaseMetric], *args, **kwargs):
        """ this function initializes the database with the args and kwargs passed
        to it. It also takes a metric that compare and filter the images"""
        self.metric = metric

    def search(self, query: Tensor) -> list[str]:
        """this function takes a query vector and return a list of image paths"""
        raise NotImplementedError
    
    
    def insert(self, image: str, image_vector: Tensor) -> None:
        """this this function takes an image path and a corresponding vector 
        to the image and stores the image in the database""" 
        raise NotImplementedError

    def clear(self) -> None:
        """this function clears the database"""
        raise NotImplementedError