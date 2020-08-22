# Team4-Project

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

