

def arrange():
    return


def seldata(userid, text):

    if '獎學金' in text:
        collection = db[str(userid)] # just testing if it wil work
        # 'db.Scholarship_Info' is the correct db collection to select from
    
    return collection.find() # no parameter means all data in the collection
    
    