from typing import Optional

import torch
from torch import Tensor
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

from services.retrieval.base import BaseRetrieval
from services.retrieval.torch_utils import get_device
from services.db import BaseDB


class Clip(BaseRetrieval):
    def __init__(
        self,
        db:BaseDB,
        model_name: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.device = get_device()
        (model_name := model_name or "openai/clip-vit-base-patch32")
        self.model = CLIPModel.from_pretrained(model_name).to(self.device)
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.db = db

    @torch.no_grad()
    def __call__(self, query: list[str], image_store: list[str]) -> tuple[str, list[str]]:
        """
        Search for the query in the image store

        args:
            - query[list[str]]: the search term.
            - image_store[list[str]]: list of image paths
        returns:
            - query[list[str]]: the search term.
            - image_store[list[str]]: list of image paths after filtering
        """
        return self.search(query, image_store)
        
    @torch.no_grad()
    def search(self, query: list[str], image_store: list[str]) -> tuple[str, list[str]]:
        """
        Search for the query in the image store

        args:
            - query[list[str]]: the search term.
            - image_store[list[str]]: list of image paths
        returns:
            - query[list[str]]: the search term.
            - image_store[list[str]]: list of image paths after filtering
        """
        query_features = self.text_embedding(query)
        image_features = self.image_embedding(image_store)
        
        for image_path, image_feature in zip(image_store, image_features):
            self.db.insert(image_path, image_feature)
        image_store = self.db.search(query_features)
        return query, image_store
    
    @torch.no_grad()
    def image_embedding(self, image_store: list[str]) -> Tensor:
        images_processed = self.processor(
            images=[Image.open(image) for image in image_store], return_tensors="pt"
        )
        image_features = self.model.get_image_features(
            **images_processed.to(self.device)
        )
        return image_features

    @torch.no_grad()
    def text_embedding(self, query: list[str]):
        query_tokenized = self.processor(text=query, return_tensors="pt")
        query_features = self.model.get_text_features(**query_tokenized.to(self.device))
        return query_features


    @staticmethod
    def list_models(model_name: str) -> list[str]:
        """this should return a list of models that can be passed as model name for the class"""
        pass
