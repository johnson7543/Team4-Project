import re
def arrange_scholarship(sel_client, data):
    select_db = "Total_Scholarship"
    db = sel_client[select_db]
    temp_category = ""
    temp_score = ""
    data_str = ""
    data_str_all = ""
    if ( data["result"]["contexts"][0]["parameters"]["ApplicationCategory"] ) :
      for temp in data["result"]["contexts"][0]["parameters"]["ApplicationCategory"] :
        temp_category = temp_category + temp + '\n'
        
    if ( data["result"]["contexts"][0]["parameters"]["ApplicationScore"] ) :
        temp_score = data["result"]["contexts"][0]["parameters"]["ApplicationScore"]
    if ( data["result"]["contexts"][0]["parameters"]["number"]):
        score_num = int(data["result"]["contexts"][0]["parameters"]["number"])
    
    if '清寒類' in temp_category:
        select_col = "清寒類"
        collection = db[select_col]
        
        if '學業成績' in temp_score and 0 <= score_num <= 100 :
            if '大學部' or '研究所' in temp_category :
              data_db = collection.find( {'$and': [ { '學業成績' : {'$lte' : score_num}, "申請身分" : { '$not' : {'$regex': '大一'} } } ] } )
            else :
              data_db = collection.find( { '學業成績' : { '$lte' : score_num } } )
        else :
          data_db = collection.find() # no score filter request, get all data     
        data_str = "".join(str(i.get('名稱'))+'\n'+ str(i.get('網址'))+'\n\n' for i in list(data_db))
        
        #----------------------------------------------------------------------#
        select_col = "不拘"
        collection = db[select_col]
        
        if '學業成績' in temp_score and 0 <= score_num <= 100 :
          if '大學部' or '研究所' in temp_category :
            data_db = collection.find( {'$and': [ { '學業成績' : {'$lte' : score_num}, "申請身分" : { '$not' : {'$regex': '大一'} } } ] } )
          else :
            data_db = collection.find( { '學業成績' : { '$lte' : score_num } } )
        else :
          data_db = collection.find() # no score filter request, get all data
        data_str_all = "".join(str(i.get('名稱'))+'\n'+ str(i.get('網址'))+'\n\n' for i in list(data_db))
        return data_str + data_str_all
        
    elif '學業成績' in temp_score and 0 <= score_num <= 100 :
        select_col = "所有類" # all data
        collection = db[select_col]
        
        if '學業成績' in temp_score and 0 <= score_num <= 100 :
          if '大學部' or '研究所' in temp_category :
            data_db = collection.find( {'$and': [ { '學業成績' : {'$lte' : score_num}, 
                                                    '申請身分' : { '$not' : {'$regex': '大一'} },
                                                    '申請資格' : {'$nin': [ re.compile(u'清寒'),re.compile(u'低收'),re.compile(u'弱勢'),re.compile(u'急難') ] } } ] } )
          else :
            data_db = collection.find( {'$and': [ { '學業成績' : {'$lte' : score_num}, 
                                                    '申請資格' : {'$nin': [ re.compile(u'清寒'),re.compile(u'低收'),re.compile(u'弱勢'),re.compile(u'急難') ] } } ] } )                    
        data_str_all = "".join(str(i.get('名稱'))+'\n'+ str(i.get('網址'))+'\n\n' for i in list(data_db))
        return data_str_all
    
    else:
        select_col = "所有類" # all data collection
        collection = db[select_col]
        if '大學部' or '研究所' in temp_category :
          data_db = collection.find( {'$and': [ { '申請身分' : { '$not' : {'$regex': '大一'} },
                                                    '申請資格' : {'$nin': [ re.compile(u'清寒'),re.compile(u'低收'),re.compile(u'弱勢'),re.compile(u'急難') ] } } ] } )
        else :
          data_db = collection.find( {'$and': [ { '申請資格' : {'$nin': [ re.compile(u'清寒'),re.compile(u'低收'),re.compile(u'弱勢'),re.compile(u'急難') ] } } ] } )
        data_str_all = "".join(str(i.get('名稱'))+'\n'+ str(i.get('網址'))+'\n\n' for i in list(data_db))
        return data_str_all
    
def get_itouch( sel_client, data ):
    select_db = "Total_Itouch"
    db = sel_client[select_db]
    temp_type = data["result"]["contexts"][0]["parameters"]["announcementtype"]
    
    select_col = temp_type # 選擇分類
    
    if 'Itouch_校內/校外徵才' in select_col :
        select_col = 'Itouch_校內徵才'
        collection = db[select_col]
        data_db = collection.find()
        data_str1 = "".join(str(i.get('標題'))+'\n'+ str(i.get('網址'))+'\n\n' for i in list(data_db)[0:1])
        
        select_col = 'Itouch_徵才公告'
        collection = db[select_col]
        data_db = collection.find()
        data_str2 = "".join(str(i.get('標題'))+'\n'+ str(i.get('網址'))+'\n\n' for i in list(data_db)[0:1])
        data_str = data_str1 + data_str2 
        
    else :
        collection = db[select_col]
        data_db = collection.find()
        data_str = "".join(str(i.get('標題'))+'\n'+ str(i.get('網址'))+'\n\n' for i in list(data_db)[0:1])
    print(data_str)
    return data_str
def seldata(sel_client, response, data):
    
    print(response[2])
    if '獎學金' in response[2]:
        return arrange_scholarship(sel_client, data)
    
    elif '公告' in response[2]:
        print("100000000000000000000000000000000000000000")
        return get_itouch( sel_client, data )
    
    