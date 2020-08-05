


def arrange():
    return


def seldata(sel_client, response, temp):

    if '獎學金' in response[2]:
        db = sel_client.blog
        collection = db.posts
        temp = data["result"]["parameters"]["ApplicationCategory"]
        score = data["result"]["parameters"]["number"]
        if '清寒' in temp:
            temp = '清寒'
            return collection.find({ "Apply" : {'$regex': temp} } ); # no parameter means all data in the collection
        else:
            return collection.find( { "Grade" : {'$regex': score} } );
    else:
        return
    
    