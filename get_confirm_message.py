def get_message(data) :
  temp_category = ""
  temp_score = ""

  if ( data["result"]["parameters"]["ApplicationCategory"] ) :
    for temp in data["result"]["contexts"][0]["parameters"]["ApplicationCategory.original"] :
      if "大肆" in temp :
          temp = "大四生"
      if "大醫生" in temp :
          temp = "大一生"      
      temp_category = temp_category + temp + '\n' 
        
  if ( data["result"]["parameters"]["ApplicationScore"] ) :
        temp_score = data["result"]["parameters"]["ApplicationScore"]
  if ( data["result"]["parameters"]["number"]):
          temp_score = " ".join(temp_score) + str(data["result"]["parameters"]["number"])
    
  temp_all = temp_category + temp_score

  if ( temp_all ) :   
    text = "請問是想要篩選以下條件嗎？" + "\n"
    return text + temp_category + temp_score
  else :
    text = "您沒有篩選任何條件哦？ 確定嗎？"
    return text
        