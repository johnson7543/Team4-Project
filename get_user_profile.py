from linebot import LineBotApi
from linebot.exceptions import LineBotApiError

def getProfile( userid ) :
  #原本的 
  line_bot_api = LineBotApi('l8HIzKnuKYtgSCLb5VG2VcBPoaEM3xWnDZQcGwoGkBWnpV8aji5gPeKDP1kTy/CxmskDdaND9kuV05D1GDEcuUWkwnSmv2QewSuSdU/4lZtZI188/NS9YA5vVEEjI0Zo1YBa9y/pc77fUcZlQTx7EAdB04t89/1O/w1cDnyilFU=')
  #測試的 line_bot_api = LineBotApi('Um2jzO1uJTdSoP53n1w3fQzklfU3cX2Hik2dKMkLOLUQUfJUyW/Lwn19IEL3YnEKdlQubAAtOABkvFJ3VRIskzj39RVr/s7xvY9jaGhiLIMBoXZQgrQ8Asp4MINqLqLAI5SJw/U276iiUPB9cO/7SQdB04t89/1O/w1cDnyilFU=')
  
  try:
    profile = line_bot_api.get_profile( userid )
      
  except LineBotApiError as e:
    # error handle
    profile = e 

  return profile