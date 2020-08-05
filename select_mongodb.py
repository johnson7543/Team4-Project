


def arrange():
    return


def seldata(sel_client, response, data):

    if '獎學金' in response[2]:
        db = sel_client.blog
        collection = db.posts
        temp = data["result"]["contexts"][0]["parameters"]["ApplicationCategory"]
        score = data["result"]["contexts"][0]["parameters"]["number"]
        if '清寒類' in temp:
            return collection.find({ "Grade" : {"gte":score}, "Grade" : 'no', "Apply" : {'$regex': '清寒'} } ); # no parameter means all data in the collection
        else:
            return collection.find({ "Grade" : {"gte":score}, "Grade" : 'no', "Apply" : {'$regex': '清寒'}, {"Apply" : 0 } });
    else:
        return
    
    