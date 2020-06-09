# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:03:50 2020

@author: LIN

嘗試使用簡單程式發送訊息至dialogflow

"""
import apiai 
import json

#Dialogflow的key
ai = apiai.ApiAI('e487ae398c804714a2b714262d78a191')
#欲傳送過去的文字
text = "下周有考試嗎" 

def parse_user_text(text):

   request = ai.text_request()
   request.query = text #欲查詢的字串
   response = request.getresponse().read().decode('utf-8') #解讀API回傳的JSON檔案(用UTF8解碼)
   responseJson = json.loads(response)  #將json檔案轉為字典物件
   #字典結構:{'key':值}
   #印出dialogflow分析我傳過去的字串的結果的其中我所想要的項目和其內容
   print(responseJson["result"]["parameters"]["action"])
   print(type(responseJson["result"]["parameters"]["action"]))



parse_user_text(text)