from linebot import LineBotApi
from linebot.exceptions import LineBotApiError

def getProfile( userid = ''  ) :
  line_bot_api = LineBotApi('l8HIzKnuKYtgSCLb5VG2VcBPoaEM3xWnDZQcGwoGkBWnpV8aji5gPeKDP1kTy/CxmskDdaND9kuV05D1GDEcuUWkwnSmv2QewSuSdU/4lZtZI188/NS9YA5vVEEjI0Zo1YBa9y/pc77fUcZlQTx7EAdB04t89/1O/w1cDnyilFU=')

  try:
    profile = line_bot_api.get_profile( userid )
      
  except LineBotApiError as e:
    # error handle
    profile = e 

  print( profile )
  return profile