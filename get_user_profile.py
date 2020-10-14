from linebot import LineBotApi
from linebot.exceptions import LineBotApiError


def getProfile( userid ) :
  line_bot_api = LineBotApi('l8HIzKnuKYtgSCLb5VG2VcBPoaEM3xWnDZQcGwoGkBWnpV8aji5gPeKDP1kTy')

  try:
    profile = line_bot_api.get_profile( userid )
      
  except LineBotApiError as e:
    # error handle
    profile = e 

  print( profile )
  return profile