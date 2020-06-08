from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import apiai 
import json

app = Flask(__name__)

#Dialogflow的key
ai = apiai.ApiAI('e487ae398c804714a2b714262d78a191')

# Channel Access Token
#初始化一個LineBotApi的物件
line_bot_api = LineBotApi('XUfZsWefxi6HDwDu4AKo4Ro42rje7b/bN3qesRA5oapqJ4WDhm3oO2qZZxOY3w1YyF2v7KRZDcrm7jix7ZaLMCDslwBGDi/4Si6BTi0LhHeK8x1MSp3auGhLCWEKlLhZVf1z/efhUjvv4m1kOC0hCwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7074f0de8312b55f594705c8de705e1b')


def parse_user_text(text): #傳訊息給dialogflow並得到解析後的答案

   request = ai.text_request()
   request.query = text #欲查詢的字串
   response = request.getresponse().read().decode('utf-8') #解讀API回傳的JSON檔案(用UTF8解碼)
   responseJson = json.loads(response)  #將json檔案轉為字典物件
   #字典結構:{'key':值}
   #印出dialogflow分析我傳過去的字串的結果的其中我所想要的項目和其內容
   #print(responseJson["result"]["parameters"]["action"])
   #print(type(responseJson["result"]["parameters"]["action"]))
   return responseJson


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)#每當收到LINE的訊息事件MessageEvent，且是一則文字訊息時 ，就執行下列程式碼。
def handle_message(event):#此函數接收LINE傳過來的資訊並貼上"event"標籤。
    
    # event長這樣是一個json物件
    #    event = {"reply_token":"就是代表reply_token的一串亂碼", 
    #         "type":"message",
    #         "timestamp":"1462629479859", 程式語言中標準的時間計算方式
    #         "source":{"type":"user",
    #                   "user_id":"就是代表user的一串亂碼"}, 
    #         "message":{"id":"就是代表這次message的一串代碼", 
    #                    "type":"text", 
    #                    "text":"使用者傳來的文字信息內容"}}
        
    #選擇參數text將他丟給dialogflow去解析
    responseJson = parse_user_text(event.message.text)
    
    #TextSendMessage是要執行的動作，LINE還提供了其他包括：ImageSendMessage、VideoSendMessage、StickerSendMessage等等的許多許多動作
    #message 也是一個json物件(或許跟event長很像)
    #把message的"text"這個項目改成此訊息經由dialogflow解析後的action
    message = TextSendMessage(text = responseJson["result"]["parameters"]["action"]) 

    line_bot_api.reply_message(event.reply_token, message )
    #LineBotApi物件的reply_message只能用在回覆訊息，且提供兩個參數:reply_token只能使用一次用完即丟
    #當其他使用者傳送信息給你的 LINE 聊天機器人，會產生一個reply_token，
    #你的聊天機器人拿著這個reply_token回覆傳信息的使用者，回覆完畢，reply_token消失
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
