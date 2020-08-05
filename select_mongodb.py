

def arrange():
    return


def seldata(collection, response):

    if '獎學金' in response[2]:
        collection = collection # just testing if it wil work
        # 'db.Scholarship_Info' is the correct db collection to select from
    
    return collection.find() # no parameter means all data in the collection
    
    