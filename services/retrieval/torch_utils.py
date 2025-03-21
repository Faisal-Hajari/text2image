import torch 


def get_device()->torch.device: 
    return torch.device("cuda:2" if torch.cuda.is_available() else "cpu")