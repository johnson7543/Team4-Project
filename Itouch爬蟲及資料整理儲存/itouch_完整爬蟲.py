# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:26:06 2020

@author: User
"""

import urllib.request as req #載入模組並設定別名
import bs4 # 爬蟲分析
import json

# Google 搜尋 URL

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
  
  itouch_json = { "title" : "", "href" : "" }
  list = []
  
  for i in titles :
    print(i.string)
  
  for i in titles :
    itouch_json = { "title" : i.string , "href" : i.get('href') }
    list.append( itouch_json )
    
    
  return list


    
#table.tboder > tr.a02 > a.href
#titles = root.select( 'table.tboder > tr.a02 > td > div > a[href]' )
  
num = int(input("請選擇要查詢之類別: 1.行政公告 2.徵才公告 3.校內徵才 4.校外來文 5.實習就業 : "))

while num != 0 :

  if num == 1 :
      choosehref = "?ann_type=1"
  elif num == 2 :
      choosehref = "?ann_type=5"
  elif num == 3 :
      choosehref = "?ann_type=4"
  elif num == 4 :
      choosehref = "?ann_type=3"
  else :
      choosehref = "?ann_type=10"
      
  temp_list = start_func( choosehref )
  print( temp_list )
  
  num = int(input("請選擇要查詢之類別: 1.行政公告 2.徵才公告 3.校內徵才 4.校外來文 5.實習就業 : "))



