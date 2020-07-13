# import
# import os
import pymongo
import select_mongodb

# connection
def runMongo(response, text):    
    
    # mongo_url = os.getenv('MONGO_CONNECTION', 'mongodb+srv://johnson7543:BfT5BEThq3deNBxJ@cluster0-84ii5.mongodb.net/Test?retryWrites=true&w=majority')  
    # must add "retryWrites=false" at the end of the url for no reason
    
    client = pymongo.MongoClient("mongodb+srv://johnson7543:BfT5BEThq3deNBxJ@cluster0-84ii5.mongodb.net/Test?retryWrites=true&w=majority")
    db = client.Test
    collection = db.testLineBot
    # mydict = { "name": "YuKai Wang", "Email": "johnson7543@cycu.org.tw", "brith": "1998/09/21" }
    
    if (response) :
        mydict ={"action": response[0],
                 "user id": response[1]}
        collection.insert(mydict) 
        
    return select_mongodb.seldata(db, text) # select from db.collection
    