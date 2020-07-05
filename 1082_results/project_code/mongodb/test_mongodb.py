from pymongo import MongoClient
# from bson.objectid import ObjectId #這東西再透過ObjectID去尋找的時候會用到

# connection
def runMongo(data):
    client = MongoClient("mongodb+srv://johnson7543:BfT5BEThq3deNBxJ@cluster0-84ii5.mongodb.net/Test?retryWrites=true&w=majority")
    db = client.Test
    collection = db.test2
    
    # test if connection success
    collection.stats  # 如果沒有error，你就連線成功了。
    print (data)
    # mydict = { "name": "YuKai Wang", "Email": "johnson7543@cycu.org.tw", "brith": "1998/09/21" }

    for temp in data :
        mydict ={"title": temp["title"], "href": temp["href"], "tweet": temp["tweet"], "author": temp["author"]}
        collection.insert_one(mydict) 
