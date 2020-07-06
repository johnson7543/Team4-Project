

def seldata(db, event):

    if '獎學金' in event.message.text :
        collection = db.Test # just testing if it wil work
        # 'db.Scholarship_Info' is the correct db collection to select from
    
    return collection.find() # no parameter means all data in the collection
    
    