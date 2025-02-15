import requests
import random
import make_flex_search_result
# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "AIzaSyD0Jz7sfKdq_vJI21azx4Rr67_6Ew3xio4"
# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "011581237149803790891:kvvffq2br44"
# the search query you want

random_picture = ["https://i.imgur.com/yPVpqWM.jpg", "https://i.imgur.com/lgATe0t.jpg",
                  "https://i.imgur.com/vbqktrv.jpg", "https://i.imgur.com/pd5leLb.jpg",
                  "https://i.imgur.com/uje85ic.jpg", "https://i.imgur.com/QnTJfmt.jpg",
                  "https://i.imgur.com/0mzIs1N.jpg", "https://i.imgur.com/Vt5Q1d4.jpg",
                  "https://i.imgur.com/ZB1e21i.jpg","https://i.imgur.com/5pYIfw7.jpg"]

def get_search_result( query, userid ) :
  if '台' in query :
    query = query.replace('台', '臺')
    print(query)
      
  https = False
  temp_num = random.randint(0,9)
  flag = True
  defult_photo = random_picture[temp_num]
  useful_photo = ""
  url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
  # make the API request
  data = requests.get(url).json()
  print(data)
  # get the result items
  search_items = data.get("items")
  i = 0
  for i, search_item in enumerate(search_items, start=0) :  
    result = []
    if query[0] in search_item.get("title") :
      # 為了提升精準度 避免搜尋張光正卻跑出醫美診所
      result.append(search_item.get("title"))
      result.append(search_item.get("link"))
      if ( search_item.get("pagemap") ) :
        if ( search_item["pagemap"].get("cse_image") ) :
          temp = search_item["pagemap"]["cse_image"][0]["src"]
        elif ( search_item["pagemap"].get("metatags") and search_item["pagemap"]["metatags"][0].get("image") ) :
          temp = search_item["pagemap"]["metatags"][0]["image"]
        elif ( search_item["pagemap"].get("metatags") and search_item["pagemap"]["metatags"][0].get("og:image") ) :
          temp = search_item["pagemap"]["metatags"][0]["og:image"]
        else: temp = ""
          
        if ( ".jpg" in temp  or ".png" in temp or ".JPG" in temp or ".PNG"  in temp ) and not ".jpg?" in temp :
          result.append(temp)
        else : 
          result.append(defult_photo)
          
      else :
        result.append(defult_photo)
        
      if ( result[2][4] == 's' and result[2] != defult_photo and flag ) : 
          flag = False
          useful_photo = result[2]
      else :
          if (useful_photo) : result[2] = useful_photo
          else : result[2] = defult_photo          
      if search_item.get("link")[4] != 's' : break
   
      print ("end at first stage")
      print (result[0])
      print (result[1])
      print (result[2])
    
      return make_flex_search_result.set_flex_search_result(result, userid)
    
  for i, search_item in enumerate(search_items, start=0) :  # 為了怕完全找不到有一樣字串存在的標題...
    result = []
    result.append(search_item.get("title"))
    result.append(search_item.get("link"))
    if search_item.get("link")[4] == 's' :
      https = True
      if ( search_item.get("pagemap") ) :
        if ( search_item["pagemap"].get("cse_image") ) :
          temp = search_item["pagemap"]["cse_image"][0]["src"]
        elif ( search_item["pagemap"].get("metatags") and search_item["pagemap"]["metatags"][0].get("image") ) :
          temp = search_item["pagemap"]["metatags"][0]["image"]
        elif ( search_item["pagemap"].get("metatags") and search_item["pagemap"]["metatags"][0].get("og:image") ) :
          temp = search_item["pagemap"]["metatags"][0]["og:image"]
        else: temp = ""
          
        if ( ".jpg" in temp  or ".png" in temp or ".JPG" in temp or ".PNG"  in temp ) and not ".jpg?" in temp :
          result.append(temp)
        else : 
          result.append(defult_photo)
          
      else :
        result.append(defult_photo)
        
      if ( result[2][4] == 's' and result[2] != defult_photo and flag ) : 
          flag = False
          useful_photo = result[2]
      else :
          if (useful_photo) : result[2] = useful_photo
          else : result[2] = defult_photo
          
      print ("end at second stage")       
      print (result[0])
      print (result[1])
      print (result[2])
    
    
      return make_flex_search_result.set_flex_search_result(result, userid)
  
  if ( not https ) :
    print("no https website, redo again with extending search")
    return get_search_result( query + " youtube", userid )
