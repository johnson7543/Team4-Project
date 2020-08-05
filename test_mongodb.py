# import
# import os
import pymongo
import select_mongodb

# connection
def runMongo(response, data = ""):    
    
    # mongo_url = os.getenv('MONGO_CONNECTION', 'mongodb+srv://johnson7543:BfT5BEThq3deNBxJ@cluster0-84ii5.mongodb.net/Test?retryWrites=true&w=majority')  
    # must add "retryWrites=false" at the end of the url for no reason
    # NOTICEE!!!!
    # Since the mlab-MongoDB will be removed from heroku app on November 10, we are now using MongoDB Atlas directly
    # Btw, there is a new app on heroku which support accessing  mongodb with no free plan, fuck you.
    
    userid = response[0]
    client = pymongo.MongoClient("mongodb+srv://johnson7543:BfT5BEThq3deNBxJ@cluster0-84ii5.mongodb.net/Test?retryWrites=true&w=majority")
    sel_client = pymongo.MongoClient("mongodb+srv://Jerry_Chang:jerry123@cluster0.mmp88.mongodb.net/Jerry_Chang?retryWrites=true&w=majority")
    db = client.Test
    collection = db[str(userid)]
    # mydict = { "name": "YuKai Wang", "Email": "johnson7543@cycu.org.tw", "brith": "1998/09/21" }
    
    if (response):
        mydict ={"user id": response[0],
                 "user text": response[1],
                 "target": response[2]}
        collection.insert(mydict) 
        
        return select_mongodb.seldata(sel_client, response, data) # select from db.collection
    
    
    
   
    