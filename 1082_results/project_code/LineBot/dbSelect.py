# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:36:43 2020

@author: LIN
"""

import os 
import psycopg2

#模仿命令提示字元去取得database的資料庫位置且去掉換行符號
DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a qwer88411').read()[:-1]

#利用前面得到的DATABASE_URL連接上 Heroku 給我們的資料庫
conn = psycopg2.connect(DATABASE_URL,sslmode='require')

#初始化一個可以執行指令的cursor()
cursor = conn.cursor()


Statement = "SELECT column_name FROM information_schema.columns WHERE table_name = 'account'"

#cursor()執行SQL指令
cursor.execute(Statement)

#指令下達後都需要使用commit做確認
conn.commit()

data =  [] 
while True:
    temp = cursor.fetchone() # 類似pop
    if temp:
      data.append(temp)
    else :
      break
print(data)

#關閉cursor
cursor.close()
#關閉連線
conn.close()