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
import os
import apiai 
import json
import test_mongodb

app = Flask(__name__)

#Dialogflow的key
ai = apiai.ApiAI('e487ae398c804714a2b714262d78a191')

# Channel Access Token
#初始化一個LineBotApi的物件
line_bot_api = LineBotApi('l8HIzKnuKYtgSCLb5VG2VcBPoaEM3xWnDZQcGwoGkBWnpV8aji5gPeKDP1kTy/CxmskDdaND9kuV05D1GDEcuUWkwnSmv2QewSuSdU/4lZtZI188/NS9YA5vVEEjI0Zo1YBa9y/pc77fUcZlQTx7EAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a86154a51569e180a823c36cb81fa05d')

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
        
    #選擇參數"text"將他丟給Dialogflow去解析其內容
    data = parse_user_text(event.message.text)
    responseJson = []
    responseJson.append(event.source.user_id)
    responseJson.append(event.message.text)
    
    if ( data["result"]["parameters"] ) :
        responseJson.append(data["result"]["parameters"]["Target"])
        action = parse_user_text(event.message.text)["result"]["parameters"]["action"]
         
        data = test_mongodb.runMongo(responseJson) # 嘗試把dialogflow回傳的存入mongodb
    # 以及從db拿取獎學金資訊、研究所資訊...etc(暫時)
    # 然而db拿出來的資料有我們不要的東西 e.g. Obj id...
        data_str = "".join(str(i.get('Target'))+'\n' for i in list(data))
    # 型別轉換 就是要打破strongly typed
    # Cursor -> list(dict) -> string
        fulfi_text = "".join(str(parse_user_text(event.message.text).get('fulfillmentText'))
    #TextSendMessage是要執行的動作，LINE還提供了其他包括：ImageSendMessage、VideoSendMessage、StickerSendMessage等等的許多許多動作
    #message也是一個json物件(或許跟event長很像)
    #把message的"text"這個項目改成此訊息經由dialogflow解析後的action
    
    #回傳訊息的製作，更改messgae裡面text的內容
        message = TextSendMessage(text = '你的Action : ' + action + '\n'
                              + '以下是我幫你找到的資料 ：\n' + data_str + '\n' + fulfi_text )
    
        line_bot_api.reply_message(event.reply_token, message )
    #LineBotApi物件的reply_message只能用在回覆訊息，且提供兩個參數:reply_token只能使用一次用完即丟
    #當其他使用者傳送信息給你的 LINE 聊天機器人，會產生一個reply_token，
    #你的聊天機器人拿著這個reply_token回覆傳信息的使用者，回覆完畢，reply_token消失
    
    else:
        responseJson.append("none")
        data = test_mongodb.runMongo(responseJson) # 嘗試把dialogflow回傳的存入mongodb
        data_str = "".join(str(i.get('Target'))+'\n' for i in list(data))
        message = TextSendMessage( text = '你在' + responseJson[1]  + '三小' ) 
        line_bot_api.reply_message(event.reply_token, message )
    
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
