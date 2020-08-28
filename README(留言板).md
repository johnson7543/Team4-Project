# Team4-Project

王昱凱 <johnson7543@cycu.org.tw>

張哲睿 <s10627217@cycu.org.tw>

林佑任 <qwer88411@cycu.org.tw>

## 暑假行程表
https://docs.google.com/spreadsheets/d/e/2PACX-1vRX4sVlzRfR41GNDoFtq8DroDbjd4ZcbVb0L2T5MgsJnuxDMkMYTQCIbOG_4rPpHULFgFuG04Kjc5bP/pubhtml?gid=0&single=true

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

### **2020/8/6** 本週三到學校和同學討論，因此未參與線上討論，下週期望見到獎學金資訊的*資料庫綱要*及*連續對話串*的第一版，加油！:muscle:	

### 第六週 2020/8/26 note
1. 暑期接近尾聲，請設法在**9月10日**以前完成第一版，並請組長來信預約一個60分鐘的時段展示整個雛型系統，開學之後就太遲了。
2. 開學之後將安排三組的成果簡報和展示，在那之前還有時間調整修正，因此，目前先以完成主要模組功能及整體系統架構為重點。
