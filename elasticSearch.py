from elasticsearch import Elasticsearch
from datetime import datetime

class Index:
    def __init__(self):
        #initiate an ElasticSearch instance, upon object creation
        self.es = Elasticsearch()
        print("Object Initiated")
    
    def update_index(self, dataObj, id):
        # if dataObj in an Obj than index with id, else print an error.
        if isinstance(dataObj, dict):
            doc = dataObj
            self.es.index(index="python-system-logger", id=id, body=doc)
            self.es.indices.refresh(index="python-logger")
        else:
            print("Data not an Map Type")
