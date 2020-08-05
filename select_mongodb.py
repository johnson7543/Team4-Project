


def arrange():
    return


def seldata(sel_client, response, data):

    if '獎學金' in response[2]:
        db = sel_client.blog
        collection = db.posts
        temp = data["result"]["contexts"][0]["parameters"]["ApplicationCategory"]
        score = int(data["result"]["contexts"][0]["parameters"]["number"])
        print(score, temp)
        print("?????????????????????????????????????????")
        if '清寒類' in temp:
            return collection.find({ "Grade" : { 'gte' : score}, "Apply" : {'$regex': '清寒'} }); # no parameter means all data in the collection
        else:
            return collection.find({ 'Grade' : { 'lte' : score}, 'Apply' : {'$regex': '.清寒'} });
    else:
        return
    
    