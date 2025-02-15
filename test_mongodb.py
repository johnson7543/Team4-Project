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
        
        profile_photo = profile.picture_url
        profile_name = profile.display_name
        
        mydict_search = { "time": datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S'),
                          "user id" : userid,
                          "user name" : profile_name,
                          "user photo" : profile_photo,
                          "user text" : response[1],
                          "intent": response[2]  # 'Search'
                        }
            
        if ( response[2] == 'Search' ) :
          collection.insert(mydict_search) 
          return
        
        mydict_1 = { "time": datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S'),
                     "user id" : userid,
                     "user name" : profile_name,
                     "user photo" : profile_photo,
                     "user text" : response[1],
                     "target": response[2],
                     "intent": response[3]
                   }
            
        if ( response[3] == '查詢獎學金1' or response[3] == 'Ask Itouch 1' ) :
          collection.insert(mydict_1) 
          return
        
        info = ""
        if ( response[2] != "公告" and data["result"]["contexts"][0]["parameters"].get("ApplicationCategory.original") ) :
          info = str(data["result"]["contexts"][0]["parameters"]["ApplicationCategory.original"])
        elif( response[2] != "公告" and data["result"]["contexts"][0]["parameters"].get("ApplicationCategory") ) :
          info = str(data["result"]["contexts"][0]["parameters"]["ApplicationCategory"])
               
        mydict_2 = { "time": datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S'),
                     "user id" : userid,
                     "user name" : profile_name,
                     "user photo" : profile_photo,
                     "user text" : response[1],
                     "target": response[2],
                     "info" : info
                   }
        
        if ( response[3] == '查詢獎學金2' ) :
          collection.insert(mydict_2) 
          return
        
        if ( response[3] == '查詢獎學金2 - yes' or response[3] == 'Ask Itouch 2' or response[3] == '查詢獎學金2 - classification - next' ) :
          return select_mongodb.seldata(sel_client, response, data) # select from db.collection
    
