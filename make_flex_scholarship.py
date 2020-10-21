import copy
#copy.deepcopy(a)

def string_to_list( result_string ) :
    result_list = list(result_string.split('\n'))
    print(result_list)
    return result_list

def set_flex_scholarship_result( result ) :
  # 從Bubble.py導入字典Bubble_Type
  import Bubble
  A_bubble = Bubble.Bubble_Scholarship_Type

  # 創造一個contents
  contents = { "type": "carousel","contents": [] }
  # print(contents)
  # 0 名稱
  # 1 日期
  # 2 金額
  # 3 網址
  list_result = string_to_list(result)
  
  while len(list_result) != 1 :
    A_NEW_bubble = copy.deepcopy(A_bubble)
    string = list_result[0]
    list_result.pop(0)
        # 獎學金標題
    A_NEW_bubble["header"]["contents"][0]["text"] = string
        
    string = list_result[0]
    list_result.pop(0)
        # 日期
    A_NEW_bubble["body"]["contents"][0]["text"] = "📅  " + string
        
    string = list_result[0]
    list_result.pop(0)       
        # 金額
    A_NEW_bubble["body"]["contents"][1]["text"] = "💵  " + string
                  
    string = list_result[0]
    list_result.pop(0)       
        # 按鈕的網址
    A_NEW_bubble["body"]["contents"][2]["action"]["uri"] = string
                
    contents["contents"].append(A_NEW_bubble)

  print(contents)
  return contents


# result = "財團法人利晉工程社會福利慈善事業基金會"+"\n"+"http://lijin.com.tw/Extend/Foundation/application"+"\n"+"林坤池獎學金"+"\n"+"http://ttntc.cyc.org.tw/download"+"\n"
# set_flex_scholarship_result( result )
