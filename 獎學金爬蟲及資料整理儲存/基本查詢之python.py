# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:40:57 2020

@author: User
"""

import urllib.request as req #載入模組並設定別名
from urllib.request import urlopen
import urllib
import bs4 # 爬蟲分析
import re # #字串.數字的操控
import unidecode


"""
?ann_type=1 行政公告
?ann_type=5 徵才公告
?ann_type=4 校內徵才
?ann_type=3 校外來文
?ann_type=10 實習就業
"""

url="https://itouch.cycu.edu.tw/active_system/active_group/cycu_30/announcement.jsp"

#選擇要查看的公告類別

num = input("請選擇要查詢之類別: 1.行政公告 2.徵才公告 3.校內徵才 4.校外來文 5.實習就業 : ")

if num == '1' :
    choosehref = "?ann_type=1"
    txtname = 1
elif num == '2' :
    choosehref = "?ann_type=5"
    txtname = 2
elif num == '3' :
    choosehref = "?ann_type=4"
    txtname = 3
elif num == '4' :
    choosehref = "?ann_type=3"
    txtname = 4
else :
    choosehref = "?ann_type=10"
    txtname = 5
    
url = url + choosehref

txtname = str(txtname)

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
 
print(len(nameList))  

#for a in nameList :
 #   print(a)
  
for a in range(len(nameList)) :
  if ( isinstance( nameList[a], bs4.element.NavigableString ) ) :
    nameList[a] = str(nameList[a].string)



if num == '1' :
  f = open( 'itouch_' + "行政公告", 'w', encoding="utf-8" ) 
elif num == '2' :
  f = open( 'itouch_' + "徵才公告", 'w', encoding="utf-8" )   
elif num == '3' :
  f = open( 'itouch_' + "校內徵才", 'w', encoding="utf-8" )  
elif num == '4' :
  f = open( 'itouch_' + "校外來文", 'w', encoding="utf-8" )   
else :
  f = open( 'itouch_' + "實習就業", 'w', encoding="utf-8" )     


for i in range( 27,len(nameList)) :
  if ( isinstance( nameList[i], str ) ) :
    f.write(nameList[i]) 
f.close()

"""
    

for i in nameList :
    print(i)
    
search = input("輸入關鍵字:")

sum1 = 0 

for name in nameList :
    
    if name.find(search) != -1 :
        targethrefList.append(hrefList[sum1])
        targetnameList.append(nameList[sum1])
    sum1 = sum1 + 1
    
sum1 = 0
    
for i in range(len(targetnameList)) :
    print(targetnameList[i], end = "  " )
    print(targethrefList[i]) 
"""
        


