import requests
import make_flex_search_result
# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "AIzaSyD0Jz7sfKdq_vJI21azx4Rr67_6Ew3xio4"
# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "011581237149803790891:kvvffq2br44"
# the search query you want
def get_search_result( query, userid ) :

  url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
# make the API request
  data = requests.get(url).json()
  print(data)
# get the result items
  search_items = data.get("items")
# iterate over 10 results found
  result = []
  for i, search_item in enumerate(search_items, start=1) :  
    result.append(search_item.get("title"))
    result.append(search_item.get("link"))
    if ( search_item.get("pagemap") ) :
      if ( search_item["pagemap"].get("cse_image") ) :
        result.append(search_item["pagemap"]["cse_image"][0]["src"])
      else :
        result.append(search_item["pagemap"]["metatags"][0]["image"])
    else :
      result.append("https://i.imgur.com/yPVpqWM.jpg")
    print (result[0])
    print (result[1])
    print (result[2])
    
    return make_flex_search_result(result, userid)
    
    # return result
