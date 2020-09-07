# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:34:22 2020

@author: User
"""
import pymongo
import pandas as pd
import urllib.request as req #載入模組並設定別名
from urllib.request import urlopen
import urllib
import bs4 # 爬蟲分析
import re # #字串.數字的操控
import unidecode
import openpyxl

"""
?ann_type=1 行政公告
?ann_type=5 徵才公告
?ann_type=4 校內徵才
?ann_type=3 校外來文
?ann_type=10 實習就業
"""

url="https://itouch.cycu.edu.tw/active_system/active_group/cycu_30/announcement.jsp"

#選擇要查看的公告類別

# num = input("請選擇要查詢之類別: 1.行政公告 2.徵才公告 3.校內徵才 4.校外來文 5.實習就業 : ")

    
choosehref = "?ann_type=1"    
a = url + choosehref
txtname = "行政公告"
res = pd.read_html(a)
data = res[0].iloc[:,0:3]
data.to_excel( txtname + ".xlsx")

choosehref = "?ann_type=5"    
b = url + choosehref
txtname = "徵才公告"
res = pd.read_html(b)
data = res[0].iloc[:,0:3]
data.to_excel( txtname + ".xlsx")

choosehref = "?ann_type=4"    
c = url + choosehref
txtname = "校內徵才"
res = pd.read_html(c)
data = res[0].iloc[:,0:3]
data.to_excel( txtname + ".xlsx")

choosehref = "?ann_type=3"    
d = url + choosehref
txtname = "校外來文"
res = pd.read_html(d)
data = res[0].iloc[:,0:3]
data.to_excel( txtname + ".xlsx")

choosehref = "?ann_type=10"    
e = url + choosehref
txtname = "實習就業"
res = pd.read_html(e)
data = res[0].iloc[:,0:3]
data.to_excel( txtname + ".xlsx")