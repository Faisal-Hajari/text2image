from typing import Optional

import torch
from torch import Tensor
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

from services.retrieval.base import BaseRetrival
from services.retrieval.torch_utils import get_device
from services.cache import BaseCache
class Clip(BaseRetrival):  
    def __init__(self, 
                 model_name:Optional[str]= None, 
                 cache:Optional[BaseCache]= None, 
                 metric:Optional[callable]= None
                ) -> None: #TODO: add cache class
        super().__init__()
        self.device = get_device()
        (model_name := model_name or "openai/clip-vit-base-patch32")
        self.model = CLIPModel.from_pretrained(model_name).to(self.device)
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.cache = cache
        self.metric = metric
        

    @torch.no_grad()
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
        #func 1 : 
        query_tokenized = self.processor(text=query, return_tensors="pt")
        query_features = self.model.get_text_features(**query_tokenized.to(self.device))

        if self.cache: 
            image_features = self.cache(query_features, image_store, self.image_embedding) #TODO: should we handle the inserstion to the db here ? what will be the benifit of using another function ? 
        else: 
           image_features = self.image_embedding(image_store)


        mask = self.metric(query_features, image_features)
        image_store = image_store[mask]
        return query, image_store

    def insert(self, *args, **kwargs):
        """ what should this do ?
        """
        pass 
    
    def image_embedding(self, image_store:list[str])->Tensor:
        images_processed = self.processor(images=[Image.open(image) for image in image_store], return_tensors="pt")
        image_features = self.model.get_image_features(**images_processed.to(self.device))
        return image_features
    
    @staticmethod
    def list_models(model_name:str)->list[str]:
        """this should return a list of models that can be passed as model name for the class""" 
        pass