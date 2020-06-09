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

#建立表格指令
Statement = '''CREATE TABLE account(
           user_id serial PRIMARY KEY,
           username VARCHAR (50) UNIQUE NOT NULL,
           password VARCHAR (50) NOT NULL,
           email VARCHAR (355) UNIQUE NOT NULL,
           created_on TIMESTAMP NOT NULL,
           last_login TIMESTAMP
        );'''

#cursor()執行SQL指令
cursor.execute(Statement)

#指令下達後都需要使用commit做確認
conn.commit()

#關閉cursor
cursor.close()
#關閉連線
conn.close()