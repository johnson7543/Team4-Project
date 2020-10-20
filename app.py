from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
import os
import apiai 
import json
import test_mongodb
import get_confirm_message
import get_user_profile
import get_google_search
import template_message
import Make_Bubble

app = Flask(__name__)

#Dialogflow key
ai = apiai.ApiAI('e487ae398c804714a2b714262d78a191')

# Channel Access Token
# 初始化一個LineBotApi的物件
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
    msg = "呵呵呵"
    egg = '-' + '\n' + msg + '\n\n\n\n' + "會看到這句話的你... 不是碰到bug，" + '\n\n' + "就是他媽有夠閒。"
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
    print(data)
    if ( data["result"]["parameters"] ) :
        responseJson.append(data["result"]["parameters"]["Target"])  # '獎學金'
    
        if ( data["result"]["fulfillment"] ) :
            fulfi_text = data["result"]['fulfillment']["speech"]
            if "查詢獎學金2" == data["result"]["metadata"]["intentName"] :
              fulfi_text = fulfi_text + get_confirm_message.get_message(data) # add confirm message
        else :
            fulfi_text = ""
        
        message = TextSendMessage( text = fulfi_text )
        
        if 'yes' in data["result"]["metadata"]["intentName"] :
            # dialogflow return 'yes' means the conversation was end.
            data_str = test_mongodb.runMongo(responseJson, data) # 嘗試把dialogflow回傳的存入mongodb
            # 以及從db拿取獎學金資訊、研究所資訊...etc(暫時)
            # 然而db拿出來的資料有我們不要的東西 e.g. Obj id...
            wtf = ""
            for temp in data["result"]["contexts"][0]["parameters"]["ApplicationCategory"] :
              if "高中" in temp :
                wtf = egg
            
            if ( wtf ) :
              message = TextSendMessage( text = wtf ) 
            else :
              message = TextSendMessage( text = fulfi_text + '\n'+ '-' + '\n' + data_str + '\n' + '這有可能不是全部的結果，' + '\n' + '不過我們還提供了額外方法，請問要繼續分類嗎？' )
            #回傳訊息的製作，更改messgae裡面text的內容 
            #TextSendMessage是要執行的動作，LINE還提供了其他包括：ImageSendMessage、VideoSendMessage、StickerSendMessage等等的許多許多動作
            #message也是一個json物件(或許跟event長很像)
            #把message的"text"這個項目改成此訊息經由dialogflow解析後的action
            
        if 'classification' in data["result"]["metadata"]["intentName"] : #如果要繼續分類的話  
            if 'next' in data["result"]["metadata"]["intentName"]:
                data_str = test_mongodb.runMongo(responseJson, data)
                print(data_str)
                message = TextSendMessage( text = data_str )
            else :
                message = template_message.scholarship_template
                        
            
        if 'Ask Itouch 1' in data["result"]["metadata"]["intentName"] :
            message = template_message.iouch_template
            
        if 'Ask Itouch 2' in data["result"]["metadata"]["intentName"] :
            a_list = test_mongodb.runMongo(responseJson, data)
            my_contents = Make_Bubble.Get_contents(a_list)
            #message = TextSendMessage( text = data_str )
            message =  FlexSendMessage( alt_text='公告查詢結果', contents = my_contents )
            
        line_bot_api.reply_message( event.reply_token, message )
        #LineBotApi物件的reply_message只能用在回覆訊息，且提供兩個參數:reply_token只能使用一次用完即丟
        #當其他使用者傳送信息給你的 LINE 聊天機器人，會產生一個reply_token，
        #你的聊天機器人拿著這個reply_token回覆傳信息的使用者，回覆完畢，reply_token消失
    
    else :
        if ( data["result"]["fulfillment"]["speech"] ):
            fulfi_text = data["result"]['fulfillment']["speech"]        
            message = TextSendMessage( text = fulfi_text )
        else :
            my_contents = get_google_search.get_search_result(event.message.text, event.source.user_id)
            message = FlexSendMessage( alt_text='令人意外的結果', contents = my_contents )
         
        line_bot_api.reply_message(event.reply_token, message )
    
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
