# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:26:06 2020

@author: User
"""

import urllib.request as req #載入模組並設定別名
import bs4 # 爬蟲分析
import pymongo

def start_func ( url_type ) :

  url_basic ="https://itouch.cycu.edu.tw/active_system/active_group/cycu_30/announcement.jsp"
  url = url_basic + url_type
    
  request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
  }) 
  
  with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
    
  root = bs4.BeautifulSoup(data, "html.parser")
  titles = root.find( name = 'table' ).find_all( name = 'a' )

  itouch_json = { "標題" : "", "網址" : "" }
  list = []
  

  for i in titles :
    i.string = str(i.string)
    i.string = " ".join(i.string.split())  
    itouch_json = { "標題" : i.string , "網址" : i.get('href') }
    list.append( itouch_json )
    
  return list

#----------------------存到db-----------------------------------------
client = pymongo.MongoClient("mongodb+srv://Jerry_Chang:jerry123@cluster0.mmp88.mongodb.net/Jerry_Chang?retryWrites=true&w=majority")
db = client.Total_Itouch
db.Itouch_實習就業.delete_many( {} )
db.Itouch_徵才公告.delete_many( {} )
db.Itouch_校內徵才.delete_many( {} )
db.Itouch_校外來文.delete_many( {} )
db.Itouch_行政公告.delete_many( {} )

choosehref = "?ann_type=1" #行政公告
temp_list = start_func( choosehref )
for temp in temp_list :
    db.Itouch_行政公告.insert_one( temp )

choosehref = "?ann_type=5" #徵才公告
temp_list = start_func( choosehref )
for temp in temp_list :
    db.Itouch_徵才公告.insert_one( temp )
    
choosehref = "?ann_type=4" #校內徵才
temp_list = start_func( choosehref )
for temp in temp_list :
    db.Itouch_校內徵才.insert_one( temp )

choosehref = "?ann_type=3" #校外來文
temp_list = start_func( choosehref )
for temp in temp_list :
    db.Itouch_校外來文.insert_one( temp )

choosehref = "?ann_type=10" #實習就業
temp_list = start_func( choosehref )
for temp in temp_list :
    db.Itouch_實習就業.insert_one( temp )

