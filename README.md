# Team4-Project

王昱凱 <johnson7543@cycu.org.tw>

張哲睿 <s10627217@cycu.org.tw>

林佑任 <qwer88411@cycu.org.tw>

<img src="https://cloud.google.com/dialogflow/docs/images/fulfillment-flow.svg" alt="呈現執行要求流程的圖表" width="100%">

1.The end-user types or speaks an expression.

2.Dialogflow matches the end-user expression to an intent and extracts parameters.

3.Dialogflow sends a webhook request message to your webhook service. This message contains information about the matched intent, 
  the action, the parameters, and the response defined for the intent.

4.Your service performs actions as needed, like database queries or external API calls.

5.Your service sends a webhook response message to Dialogflow. This message contains the response that should be sent to the end-user.

6.Dialogflow sends the response to the end-user.

7.The end-user sees or hears the response.

