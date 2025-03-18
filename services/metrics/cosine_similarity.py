from .base_metrics import BaseMetric
from torch import Tensor
import torch


class CosineSimilarity(BaseMetric):
    def __init__(self, threshold:float= 0.2, normalize:bool=True, sort:bool=False)->None:
        self.threshold = threshold
        self.normalize = normalize
        self.sort_flag = sort

    def __call__(self, query:Tensor, image:Tensor, )->list[int]:
        """This function takes in a query and image tensor and returns a list of indexes""" 
        similarity = self.similarity(query, image, self.normalize)
        index = self.sort(similarity) if self.sort_flag else self.mask(similarity, self.threshold)
        return index
    
    def sort(self, similarity:Tensor)->list[int]:
        return similarity.argsort(descending=True).tolist()
    
    def mask(self, similarity:Tensor, threshold:float)->list[int]:
        mask = similarity>=threshold
        mask = mask.nonzero().squeeze()
        mask = mask.tolist()
        return mask
        
        
    def similarity(self, query:Tensor, image:Tensor, normalize:bool)->Tensor:
        if normalize: 
            similarity = torch.cosine_similarity(query, image)
        else: 
            similarity = query@image.T
        return similarity
