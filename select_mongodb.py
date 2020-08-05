


def arrange():
    return


def seldata(sel_client, response):

    if '獎學金' in response[2]:
        db = sel_client.blog
        collection = db.posts
    
        return collection.find({ "Apply" : /清寒/}); # no parameter means all data in the collection
    else:
        return
    
    