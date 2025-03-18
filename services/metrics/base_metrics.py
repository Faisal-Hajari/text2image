from torch import Tensor

class BaseMetric(object): 
    def __init__(self, *args, **kwargs)->None:
        return None
    
    def __call__(self, query:Tensor, image:Tensor)->list[int]:
        """This function takes in a query and image tensor and returns a list of indexes""" 
        raise NotImplementedError("metric is not implemented")