# import
# import os
import pymongo
import select_mongodb
import get_user_profile

import pytz
from datetime import datetime

# connection
def runMongo(response, data):    
    
    # mongo_url = os.getenv('MONGO_CONNECTION', 'mongodb+srv://johnson7543:BfT5BEThq3deNBxJ@cluster0-84ii5.mongodb.net/Test?retryWrites=true&w=majority')  
    # must add "retryWrites=false" at the end of the url for no reason
    # NOTICEE!!!!
    # Since the mlab-MongoDB will be removed from heroku app on November 10, we are now using MongoDB Atlas directly
    # Btw, there is a new app on heroku which support accessing  mongodb with no free plan, fuck you.
    
    userid = response[0]
    client = pymongo.MongoClient("mongodb+srv://johnson7543:BfT5BEThq3deNBxJ@cluster0-84ii5.mongodb.net/Test?retryWrites=true&w=majority")
    sel_client = pymongo.MongoClient("mongodb+srv://Jerry_Chang:jerry123@cluster0.mmp88.mongodb.net/Jerry_Chang?retryWrites=true&w=majority")
    db = client['User-data']
    collection = db[userid]
    # mydict = { "name": "YuKai Wang", "Email": "johnson7543@cycu.org.tw", "brith": "1998/09/21" }
    
    if (response):
        profile = get_user_profile.getProfile(userid)
        print(profile)
        print(type(profile))
        print()
        
        profile_photo = str(profile.picture_url)
        profile_name = str(profile['display_name'])

        
        if ( data["result"]["contexts"][0]["parameters"]["ApplicationCategory.original"] ) :
          info = str(data["result"]["contexts"][0]["parameters"]["ApplicationCategory.original"])
        else :
          info = str(data["result"]["contexts"][0]["parameters"]["ApplicationCategory"])
          
        mydict = { "time": datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S'),
                   "user id" : userid,
                   "user frofile" : str(profile),
                   "user name" : profile_name,
                   "user photo" : profile_photo,
                   "user text" : response[1],
                   "target": response[2],
                   "info" : info
                  }
        
        collection.insert(mydict) 
        
        return select_mongodb.seldata(sel_client, response, data) # select from db.collection
    
    
    
   
    