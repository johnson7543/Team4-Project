from line-bot-sdk import LineBotApi
from linebot.exceptions import LineBotApiError


def getProfile( userid = 'U4e235d023391dd4866a3032722640e62'  ) :
  line_bot_api = LineBotApi('l8HIzKnuKYtgSCLb5VG2VcBPoaEM3xWnDZQcGwoGkBWnpV8aji5gPeKDP1kTy')

  try:
    profile = line_bot_api.get_profile( userid )
      
  except LineBotApiError as e:
    # error handle
    profile = e 

  print( profile )
  #return profile