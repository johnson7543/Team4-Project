def get_confirm_message(data) :
    temp_category = ""
    temp_score = ""
    
    if ( data["result"]["contexts"][0]["parameters"]["ApplicationCategory"] ) :
        temp_category = data["result"]["contexts"][0]["parameters"]["ApplicationCategory"]
        
    if ( data["result"]["contexts"][0]["parameters"]["ApplicationScore"] ) :
        temp_score = data["result"]["contexts"][0]["parameters"]["ApplicationScore"]
        if ( data["result"]["contexts"][0]["parameters"]["number"]):
          temp_score = temp_score + data["result"]["contexts"][0]["parameters"]["number"]
    
    temp_all = temp_category + temp_score
    if ( temp_all ) :      
      return temp_category + temp_score
    else :
      text = "您沒有篩選任何條件哦？ 確定嗎？"
      return text
        