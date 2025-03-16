import torch 
from torch import Tensor

def cosine_similarity(text_vectors:Tensor, image_vectors:Tensor, threshold:float=0.20, normalize:bool=True) -> list[int]: 
    #TODO: should this sort ? 
    """takes a text vector and image vectors and return the indexes of the images that passed the threshold
     
      args: 
       - text_vectors[Tensor]: text vector of size [1, D]
       - image_vectors[Tensor]: image vector of size [num of images, D]
       - threshold[float]: the cutoff for the similarity {0.0, 1.0}
       - normalize[bool]: if true we normalize the vectors.
        
      returns: 
       - indexes[list[int]]: the list of vectors to keep 
    """
    if normalize: 
        similarity = torch.cosine_similarity(text_vectors, image_vectors)
    else: 
        similarity = text_vectors@image_vectors.T
    
    mask = similarity>=threshold
    index = mask.nonzero()
    index = index.tolist()
    return index