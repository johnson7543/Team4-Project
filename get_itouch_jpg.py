# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:49:56 2020

@author: jerry.chang
"""

import urllib.request as req #載入模組並設定別名
import bs4 # 爬蟲分析
import random

def get_jpg( url_type ) :

  url = url_type
    
  request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
  }) 
  
  with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
    
  root = bs4.BeautifulSoup(data, "html.parser")
  titles = root.find_all( name = 'img' )
  titles.remove(titles[0])
  
  target = []
  temp_count = 0
  random_picture = ["https://i.imgur.com/yPVpqWM.jpg", "https://i.imgur.com/lgATe0t.jpg",
                    "https://i.imgur.com/vbqktrv.jpg", "https://i.imgur.com/pd5leLb.jpg",
                    "https://i.imgur.com/uje85ic.jpg", "https://i.imgur.com/QnTJfmt.jpg",
                    "https://i.imgur.com/0mzIs1N.jpg", "https://i.imgur.com/Vt5Q1d4.jpg",
                    "https://i.imgur.com/ZB1e21i.jpg","https://i.imgur.com/5pYIfw7.jpg"]
  
  for i in titles :
    if ( ".JPG" in i.get("src") ) or ( ".png" in i.get("src") ) or ( ".jpg" in i.get("src") ) or ( ".PNG" in i.get("src") ) :
      temp_count = temp_count + 1
      target.append(i.get("src"))

  if temp_count < 1 :
    temp_num = random.randint(0,9)
    return random_picture[temp_num]
  else : 
    for i in target :    
      # print("https://ann.cycu.edu.tw" + i )
      if "https:" in i :  
        return i 
      return "https://ann.cycu.edu.tw" + i
        
# str_test = get_jpg( "https://ann.cycu.edu.tw/aa/frontend/AnnItem.jsp?sn=47735" )
# print(str_test)
      
  