from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):
    
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:36808/?authMechanism=DEFAULT&authSource=AAC'%(username,password))
        self.database = self.client['AAC']
   
    #create method
    def create(self, data):
        if data is not None:            
            result = self.database.animals.insert_one(data) # data should be dictionary     
            return result.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
       
    #read one method            
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            raise Exception("nothing to read because data parameter is empty")
    
    #read all method
    def readAll(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("nothing to read because data parameter is empty")

    #update method
    def update(self, query, newData):
        if not query:
            raise Exception("No search criteria")
        elif not newData:
            raise Exception("No update value given")
        else:
            query = self.database.animals.update_many(query, {"$set": newData})
            return query.raw_result
            
    #delete method
    def delete(self, query):
        if not query:
            raise Exception ("No search criteria") 
        else:
            query = self.database.animals.delete_many(query)
            return query.raw_result
            
