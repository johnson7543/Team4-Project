# Team4-Project (CYCU Assistant)

### <a href="https://youtu.be/MG7tWFN1kK8">成品展示影片</a>

王昱凱 <johnson7543@cycu.org.tw>

張哲睿 <s10627217@cycu.org.tw>

林佑任 <qwer88411@cycu.org.tw>

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
