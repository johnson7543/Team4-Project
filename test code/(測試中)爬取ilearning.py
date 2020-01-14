# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:33:07 2019

@author: LIN
登入ilearning
"""
import requests
from bs4 import BeautifulSoup

import hashlib
import base64
import binascii
from pyDes import *




username ='10627211'
passward ='YJLin880410'


login_url = "https://i-learning.cycu.edu.tw/login.php" #登入的部分

session_requests = requests.Session() #使所有請求發生在同一個session裡面
respones = session_requests.get(login_url)
respones.encoding = "utf8" # 以utf-8編碼
soup = BeautifulSoup(respones.text, "lxml") #將網頁分析BeautifulSoup物件
passwordDiv =soup.find("div" ,class_ = 'passwordDiv') #找到我要的Div
login_key = passwordDiv.find(attrs={"name":'login_key',"type":"hidden"})["value"] #取得我要的值
print(login_key,type(login_key))

headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': '_ga=GA1.3.1572832747.1551869778; school_hash=2a628f5618d57bc0c100018c62e0331f; PHPSESSID=2desgai834vd5rjoln0qv6poh4; sIdx=; wm_lang=Big5; _gid=GA1.3.625471333.1577627719',
'Host': 'i-learning.cycu.edu.tw',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}



def DesEncrypt(Des_Key,str):
    k = des(Des_Key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    EncryptStr = k.encrypt(str)
    return base64.b64encode(EncryptStr) #轉base64編碼返回


m = hashlib.md5() #md5加密的物件
m.update(passward.encode("utf-8"))
md5key = m.hexdigest()

#script語法:cypkey = md5key.substr(0,4) + login_key(0,4);
cypkey = md5key[0:4] + login_key[0:4]
pwdvalue = passward

encrypt_pwd = DesEncrypt( cypkey,passward ) #des加密


#encodedBytes = base64.b64encode(data.encode("utf-8"))
#encodedStr = str(encodedBytes, "utf-8")
#print(encodedStr)



data={'username':username ,'password':passward ,'x':0,'y':0,'login_key': login_key ,'encrypt_pwd':cypkey ,'pwd':pwdvalue}

result = session_requests.post(login_url,headers = headers ,data = data ) #post資訊
frontpage = session_requests.get("https://i-learning.cycu.edu.tw/learn/index.php",headers = headers) #再次連向主頁面
soup = BeautifulSoup(frontpage.text, "lxml")
print(soup)
print("--------------------")


#因為我發現ilearning的登入需要某個login_key但是在是無法抓到那個密碼
#一開始我認為我在登入畫面抓到的login_key值是正確的後，我自己上網登入發現login_key卻又改變了

