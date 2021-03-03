# Team4-Project (CYCU Assistant)

王昱凱 <johnson7543@cycu.org.tw>

張哲睿 <s10627217@cycu.org.tw>

林佑任 <qwer88411@cycu.org.tw>


### <a href="https://youtu.be/MG7tWFN1kK8">成品展示影片</a>
### <a href="https://drive.google.com/file/d/1WFMS3W1G-w0a8fYuuvo8WssFH4dEnpT0/view?usp=sharing">專題書面報告</a>

[![](https://i.imgur.com/BqzQ6Gh.png)](https://i.imgur.com/BqzQ6Gh.png "運作結果")
[![](https://i.imgur.com/Vg0GtuB.jpg)](https://i.imgur.com/Vg0GtuB.jpg "架構圖")
## Dialogflow運作流程
<ol>
  <li>The end-user types or speaks an expression.</li>
  <li>Dialogflow matches the end-user expression to an intent and extracts parameters.</li>
  <li>
    Dialogflow sends a
    <a href="https://cloud.google.com/dialogflow/docs/fulfillment-how#webhook_request">webhook request</a>
    message to your webhook service.
    This message contains information about the matched intent, the action, the parameters,
    and the response defined for the intent.
  </li>
  <li>Your service performs actions as needed, like database queries or external API calls.</li>
  <li>
    Your service sends a
    <a href="https://cloud.google.com/dialogflow/docs/fulfillment-how#webhook_response">webhook response</a>
    message to Dialogflow.
    This message contains the response that should be sent to the end-user.
  </li>
  <li>Dialogflow sends the response to the end-user.</li>
  <li>The end-user sees or hears the response.</li>
</ol>

## 系統安裝指南
1. 請到 Line 官方的 Line Developers 申請 Line Message API 的功能,取得一個自己的聊天機器人 channel
(channel的詳細內容有包含Channel secret、Channel access token 此兩項數據為重要資料,將會影響整個機器人是否可使用)。

2. 複製我們的倉庫能取得所有相關的程式碼(主程、其他功能的程式)

3. 申請 Heroku 帳號建立一個新的 web(app)，並且來與自己的 GitHub 帳號做連接,方便未來的部署更加快速,減少在 CMD 指令的操作,相關操作方法可以上網搜尋。
其中必須將要被執行的檔案在 Heroku 中做設定app.py 以及 keep_awake.py (如果你不想Heroku睡著的話)

4. 更改程式碼 app.py、get_user_profile.py 這兩個檔案內分別有可以更改 Channel secret、Channel access token 的地方(參照註解)，改成自己所申請的Line帳號之金鑰(上述兩項)。資料庫的金鑰也需要做更改，在test_mongodb.py、兩個爬蟲程式，改成自己申請的( MongoDB)。當然不改的話也能運作就是了，因為是獨立出來的部分。

5. Line Developers的頁面會有一項Webhook URL,這項資料可以在Heroku找到,且也必須更改,讓你的機器人能夠接收並回傳訊息。

  格式為：https://{heroku_app名稱}.herokuapp.com/callback

  例如 : https://linemongo.herokuapp.com/callback


## 需要設定讓heroku執行的檔案
#### app.py                      
>主程式
#### keep_awake.py               
>讓heorku不要睡著

## 被呼叫的檔案
#### get_confirm_message.py      
>製作篩選確認訊息
#### get_google_search.py        
>google search API
#### get_itouch_jpg.py           
>輸入網址就會抓取該網址之ioutch公告圖片
#### get_user_profile.py         
>抓取使用者的(Line)資訊
#### Bubble.py                   
>查詢結果的flex_message模板
#### Make_Bubble.py              
>製作itouch公告的flex_message
#### make_flex_scholarship.py    
>製作獎學金結果的flex_message
#### make_flex_search_result.py  
>製作google_search結果的flex_message
#### template_message.py         
>獎學金額外篩選的按鈕模板
#### test_mongodb.py             
>將使用者紀錄存入資料庫以及連接要抓取結果的資料庫
#### select_mongodb.py           
>從資料庫抓取資料

## 使用heroku排程執行的檔案
#### crawler program內兩個.py     
>資料爬蟲程式(公告、獎學金)

## 設定檔
#### Procfile                    
>Heroku執行設定檔
#### requirements.txt             
>Heroku需要安裝的import檔
