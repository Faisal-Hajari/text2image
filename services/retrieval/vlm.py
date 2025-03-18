from typing import Optional

from transformers import (
    Qwen2_5_VLForConditionalGeneration,
    AutoTokenizer,
    AutoProcessor,
)
from qwen_vl_utils import process_vision_info
import torch

from .base import BaseRetrieval
from services.db import BaseDB
from services.retrieval.torch_utils import get_device

class BinaryQwenVL(BaseRetrieval):
    def __init__(self, system_promt: Optional[str] = "", max_new_tokens:int=128):
        self.system_prompt = system_promt
        self.max_new_tokens = max_new_tokens
        self.device = get_device()
        self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            "Qwen/Qwen2.5-VL-7B-Instruct",
            torch_dtype=torch.bfloat16,
            attn_implementation="flash_attention_2",
            device_map=self.device,
        )
        self.processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")

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
        
        for image_path in image_store:
            input_tensor = self.process_input(query, image_path, self.system_prompt, self.processor)
            input_tensor = input_tensor.to(self.device)
            response = self.generate(input_tensor, self.processor)
            if not self.is_yes(response): 
                image_store.remove(image_path)
        return query, image_store

    
    def process_input(self, query: str, image: str, system_prompt, processor):
        messages = self._generate_message(query, system_prompt, image)
        text = self._apply_chat_template(messages, processor)
        image_inputs, video_inputs = process_vision_info(messages)
        input = processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt",
        )
        return input
    
    
    def is_yes(self, response)->torch.Tensor:
        response = response.lower()
        return 'yes' in response    
    
    def generate(self, input_tensor, processor):
        generated_ids = self.model.generate(**input_tensor, max_new_tokens=self.max_new_tokens)
        generated_ids_trimmed = [
            out_ids[len(in_ids) :] for in_ids, out_ids in zip(input_tensor.input_ids, generated_ids)
        ]
        output_text = processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )
        return output_text[0]
    
    def _apply_chat_template(self, messages:list[dict], processor) -> str:
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        return text

    def _generate_message(self, query:str, system_prompt:str, image:str): 
        messages = []
        if self.system_prompt != "":
            messages.append(
                {
                    "role": "system",
                    "content": [{"type": "text", "text": system_prompt}],
                }
            )
        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": image,
                    },
                    {"type": "text", "text": query},
                ],
            }
        )
        return messages