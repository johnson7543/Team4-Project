# import
import os
import pymongo

# connection
def runMongo(data):    
    
    mongo_url = os.getenv('MONGOLAB_URI', 'mongodb://heroku_95jb1hvd:5mvk8kou4g9kfpl3uo2knehlmg@ds339968.mlab.com:39968/heroku_95jb1hvd?retryWrites=false')  
    # must add "retryWrites=false" at the end of the url for no reason
    
    client = pymongo.MongoClient(mongo_url)
    db = client.heroku_95jb1hvd
    collection = db.Test
    # mydict = { "name": "YuKai Wang", "Email": "johnson7543@cycu.org.tw", "brith": "1998/09/21" }
    
    if (data) :
        mydict ={"action": data["result"]["parameters"]["action"]}
        collection.insert(mydict) 
