import re
import random
import get_itouch_jpg

def arrange_scholarship(sel_client, data):
    select_db = "Total_Scholarship"
    db = sel_client[select_db]
    temp_category, temp_score, data_str, others_str = "", "", "", ""
    begin, last = 0, 8  # used to control how many data should print
    score_num = 0
    
    if ( data["result"]["contexts"][0]["parameters"]["ApplicationCategory"] ) :
      for temp in data["result"]["contexts"][0]["parameters"]["ApplicationCategory"] :
        temp_category = temp_category + temp + '\n'
        
    if ( data["result"]["contexts"][0]["parameters"]["ApplicationScore"] ) :
        temp_score = data["result"]["contexts"][0]["parameters"]["ApplicationScore"]
    if ( data["result"]["contexts"][0]["parameters"]["number"] ):
        score_num = int(data["result"]["contexts"][0]["parameters"]["number"])
    if ( 'next' in data["result"]["metadata"]["intentName"] and data["result"]["contexts"][0]["parameters"]["others"]):
        others_str = data["result"]["contexts"][0]["parameters"]["others"]

    if '清寒類' in temp_category :
        select_col = "清寒類"
        collection = db[select_col]
        
        if '學業成績' in temp_score and 0 <= score_num <= 100 :
            if '大學部' or '研究所' in temp_category :
              data_db = collection.find( {'$and': [ { '學業成績' : {'$lte' : score_num}, "申請身分" : { '$not' : {'$regex': '大一'} } } ] } )
            else :
              data_db = collection.find( { '學業成績' : { '$lte' : score_num } } )
        else :
          if '大學部' or '研究所' in temp_category :
            data_db = collection.find( {'$and': [ {"申請身分" : { '$not' : {'$regex': '大一'} } } ] } )
          else :
            data_db = collection.find() # no score filter request, get all data   
            
        data_list = list(data_db)        
        #----------------------------------------------------------------------#
        select_col = "不拘"
        collection = db[select_col]
        
        if '學業成績' in temp_score and 0 <= score_num <= 100 :
          if '大學部' or '研究所' in temp_category :
            data_db = collection.find( {'$and': [ { '學業成績' : {'$lte' : score_num}, "申請身分" : { '$not' : {'$regex': '大一'} } } ] } )
          else :
            data_db = collection.find( { '學業成績' : { '$lte' : score_num } } )
        else :
          if '大學部' or '研究所' in temp_category :
            data_db = collection.find( {'$and': [ {"申請身分" : { '$not' : {'$regex': '大一'} } } ] } )
          else :
            data_db = collection.find() # no score filter request, get all data  
          
        data_list_final = data_list + list(data_db)    
        #data_list_final = shuffle(data_list_final)   
        
        if "money" in others_str :
          print("sorted by money")
          data_list_final = sorted(data_list_final, key = lambda s:s["金額"], reverse = True)
          data_str = "".join(str(i.get('名稱')) + '\n'+ str(i.get('金額')) + '\n' + str(i.get('網址')) + '\n\n' for i in data_list_final[begin:last])
                   
        elif "close" in others_str :
          print("sorted by date")
          data_list_final = sorted(data_list_final, key = lambda s:s["截止日期"])
          data_str = "".join(str(i.get('名稱')) + '\n'+ str(i.get('截止日期')) + '\n' + str(i.get('網址')) + '\n\n' for i in data_list_final[begin:last])
          
        elif "all_data" in others_str :
          print("print all data")
          random.shuffle(data_list_final)
          data_str = "".join(str(i.get('名稱')) + '\n' + str(i.get('網址')) + '\n\n' for i in data_list_final )
         
        else :
            data_str = "".join(str(i.get('名稱')) +'\n'+ str(i.get('網址')) + '\n\n' for i in data_list_final[begin:last])
        
        return data_str
        
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
        data_list_final = list(data_db)
        
        if "money" in others_str :
          print("sorted by money")
          data_list_final = sorted(data_list_final, key = lambda s:s["金額"], reverse = True)        
                   
        elif "close" in others_str :
          print("sorted by date")
          data_list_final = sorted(data_list_final, key = lambda s:s["截止日期"])
        
        data_str = "".join(str(i.get('名稱')) + '\n'+ str(i.get('截止日期')) + '\n'+ str(i.get('金額')) + '\n' + str(i.get('網址')) + '\n' for i in data_list_final[begin:last])
 
        if "all_data" in others_str :
          print("print all data")
          random.shuffle(data_list_final)
          data_str = "".join(str(i.get('名稱')) + '\n' + str(i.get('網址')) + '\n' for i in data_list_final )
          
        return data_str
    
    else :  # 當沒有說是清寒和報告成績
        select_col = "所有類" # all data collection
        collection = db[select_col]
        if '大學部' or '研究所' in temp_category :  # 沒有說是清寒和報告成績的非大一生 (大二~四、研究生)
          data_db = collection.find( {'$and': [ { '申請身分' : { '$not' : {'$regex': '大一'} },
                                                    '申請資格' : {'$nin': [ re.compile(u'清寒'),re.compile(u'低收'),re.compile(u'弱勢'),re.compile(u'急難') ] } } ] } )
        else :  # 這邊預計要有"完全不篩選"的路線(對話尚未設計)
          # if 不篩選
          # 拿出所有資料 並隨機排序
          
          # else
          data_db = collection.find( {'$and': [ { '申請資格' : {'$nin': [ re.compile(u'清寒'),re.compile(u'低收'),re.compile(u'弱勢'),re.compile(u'急難') ] } } ] } )
          # 沒有說是清寒和報告成績的大一生
          
        data_list_final = list(data_db)
        
        if "money" in others_str :
          print("sorted by money")
          data_list_final = sorted(data_list_final, key = lambda s:s["金額"], reverse = True)        
                   
        elif "close" in others_str :
          print("sorted by date")
          data_list_final = sorted(data_list_final, key = lambda s:s["截止日期"])
        
        data_str = "".join(str(i.get('名稱')) + '\n'+ str(i.get('截止日期')) + '\n'+ str(i.get('金額')) + '\n' + str(i.get('網址')) + '\n' for i in data_list_final[begin:last])
 
        if "all_data" in others_str :
          print("print all data")
          random.shuffle(data_list_final)
          data_str = "".join(str(i.get('名稱')) + '\n' + str(i.get('網址')) + '\n' for i in data_list_final )
             
        return data_str
    
def get_itouch( sel_client, data ):
    select_db = "Total_Itouch"
    db = sel_client[select_db]
    temp_type = data["result"]["contexts"][0]["parameters"]["announcementtype"]
    select_col = temp_type # 選擇分類
    
    a_list = [] #一個空的list
    if 'Itouch_校內/校外徵才' in select_col :
        select_col = 'Itouch_校內徵才'
        collection = db[select_col]
        data_db = collection.find()
        
        for i in list(data_db)[0:2] :
            a_list.append(str(i.get('標題')))
            a_list.append(str(i.get('網址')))
            a_list.append(str(get_itouch_jpg.get_jpg(str(i.get('網址')))))
        
        select_col = 'Itouch_徵才公告'
        collection = db[select_col]
        data_db = collection.find()
        for i in list(data_db)[0:2]  :
            a_list.append(str(i.get('標題')))
            a_list.append(str(i.get('網址')))
            a_list.append(str(get_itouch_jpg.get_jpg(str(i.get('網址')))))
        
    else :
        collection = db[select_col]
        data_db = collection.find()
        #data_str = "".join(str(i.get('標題'))+'\n'+ str(i.get('網址'))+'\n\n' for i in list(data_db)[0:4])
        for i in list(data_db)[0:4]  :
            a_list.append(str(i.get('標題')))
            a_list.append(str(i.get('網址')))
            a_list.append(str(get_itouch_jpg.get_jpg(str(i.get('網址')))))

    return a_list

def seldata(sel_client, response, data):
    
    if '獎學金' in response[2]:
        return arrange_scholarship(sel_client, data)
    
    elif '公告' in response[2]:
        return get_itouch( sel_client, data )
    
    