def arrange_scholarship(sel_client, data):
    select_db = "Total_Scholarship"
    db = sel_client[select_db]
    text = "這樣資料很多哦 建議重新篩選"
    score_num = int(data["result"]["parameters"]["number"])
    temp_category = data["result"]["parameters"]["ApplicationCategory"]
    temp_score = data["result"]["parameters"]["ApplicationScore"]
    
    if '清寒類' in temp_category:
        select_col = "清寒類"
        collection = db[select_col]
        
        if '學業成績' in temp_score and 0 <= score_num <= 100 :
            data_db = collection.find( { '學業成績' : { '$lte' : score_num } } )
        else :
          data_db = collection.find() # no score filter request, get all data     
        data_str = "".join(str(i.get('名稱'))+'\n' for i in list(data_db))
        
        #----------------------------------------------------------------------#
        select_col = "不拘"
        collection = db[select_col]
        
        if '學業成績' in temp_score and 0 <= score_num <= 100 :
          data_db = collection.find( { '學業成績' : { '$lte' : score_num } } )
        else :
          data_db = collection.find() # no score filter request, get all data
        data_str_all = "".join(str(i.get('名稱'))+'\n' for i in list(data_db))
        
        return data_str + data_str_all
        
    elif '學業成績' in temp_score and 0 <= score_num <= 100 :
        select_col = "所有類" # all data
        collection = db[select_col]
        data_db = collection.find( { '學業成績' : { '$lte' : score_num } } )
        data_str_all = "".join(str(i.get('名稱'))+'\n' for i in list(data_db))
        
        return data_str + text
    
    else:
        select_col = "所有類" # all data collection
        collection = db[select_col]
        data_db = collection.find() # no parameter means all data in the collection
        data_str = "".join(str(i.get('名稱'))+'\n' for i in list(data_db))
        
        return data_str + text



def seldata(sel_client, response, data):

    if '獎學金' in response[2]:
        return arrange_scholarship(sel_client, data)
    
    elif 'itouch公告' in response[2]:
        return
    
    