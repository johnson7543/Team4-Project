


def arrange():
    return


def seldata(sel_client, response, temp):

    if '獎學金' in response[2]:
        db = sel_client.blog
        collection = db.posts
    
        return collection.find({ "Apply" : {'$regex': temp[0]}}); # no parameter means all data in the collection
    else:
        return
    
    