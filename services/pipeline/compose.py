from services.retrieval import BaseRetrival

class ComposeRetrivals(object): 
    def __init__(self, retrievals: list[BaseRetrival]): 
        self.retrievals = retrievals
    
    def __call__(self, query:list[str], image_store:list[str])->list[str]: 
        for retrieval in self.retrievals: 
            query, image_store = retrieval(query, image_store)
        return query, image_store
        