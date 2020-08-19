# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:26:13 2020

@author: User
"""

import urllib.request as req #載入模組並設定別名
from urllib.request import urlopen
import urllib
import bs4 # 爬蟲分析
import re # #字串.數字的操控

url="https://itouch.cycu.edu.tw/active_system/query_data/student/ssgogo.jsp"

#!!!必須建立一個Request的物件,附加Request Headers的資訊,讓Pprogram看起來像正常的使用者
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
    

root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("a")

nameList = []
hrefList = []
targetnameList = []
targethrefList = []

for title in titles :
    nameList.append(title.string)
    hrefList.append(title.get('href')) # 放入list存起來
    
"""for i in range(len(nameList)) :
    # print(nameList[i], end = "  " )
    print(hrefList[i])"""
    

list_href = []

for i in hrefList :
  if not ( "mailto" in i or "javascript" in i ) :
    list_href.append(i)
 
print(list_href)

print(len(list_href))