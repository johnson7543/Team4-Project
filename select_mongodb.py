def arrange_scholarship(sel_client, response, data):
    select_db = "Total_Scholarship"
    db = sel_client[select_db]
    score = int(data["result"]["contexts"][0]["parameters"]["number"])
         
    temp = data["result"]["contexts"][0]["parameters"]["ApplicationCategory"]
    if '清寒類' in temp:
        select_col = "清寒類"
        collection = db[select_col]
    
        data_db = collection.find( { '學業成績' : { '$lte' : score } } )
        data_str = "".join(str(i.get('名稱'))+'\n' for i in list(data_db))
        
        select_col = "不拘"
        collection = db[select_col]
        data_db = collection.find( { '學業成績' : { '$lte' : score } } )
        data_str_all = "".join(str(i.get('名稱'))+'\n' for i in list(data_db))
        
        return data_str + data_str_all
        
    # return collection.find({"Apply" : {'$regex': '清寒'} }); # no parameter means all data in the collection
    else:
        select_col = "不拘"
        collection = db[select_col]
        data_db = collection.find( { '學業成績' : { '$lte' : score } } )
        data_str = "".join(str(i.get('名稱'))+'\n' for i in list(data_db))
            
        return data_str



def seldata(sel_client, response, data):

    if '獎學金' in response[2]:
        return arrange_scholarship(sel_client, response, data)
    
    else:
        return
    
    