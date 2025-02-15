# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:56:32 2020

@author: LIN
"""
import copy
#copy.deepcopy(a)

def Get_contents(a_list) :
    
    #從Bubble.py導入字典Bubble_Type
    import Bubble
    A_bubble = Bubble.Bubble_Type
    print(type(A_bubble)) #dict

    #創造一個contents
    contents = { "type": "carousel","contents": [] }
    print(contents)
    while len(a_list) != 0 :
        A_NEW_bubble = copy.deepcopy(A_bubble)
        string = a_list[0]
        a_list.pop(0)
        #bubble裡面的地一個Box的標題
        A_NEW_bubble["body"]["contents"][0]["text"] = string
        
        string = a_list[0]
        a_list.pop(0)
        #bubble裡面的地一個Box的標提裡面暗藏的網址
        A_NEW_bubble["body"]["contents"][0]["action"]["uri"] = string
        
        string = a_list[0]
        a_list.pop(0)       
        #bubble裡面的地一個Box的照片網址
        A_NEW_bubble["header"]["contents"][0]["url"] = string
        

      
        contents["contents"].append(A_NEW_bubble)

    print(contents)
    return contents

"""
#改bubble用appned放入total
Total = {"type": "carousel","contents": []}
BUBBLE =     {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "搜尋結果",
            "size": "4xl",
            "weight": "bold",
            "position": "relative",
            "align": "center"
          }
        ]
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "hello, world",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "http://linecorp.com/"
                    }
                  }
                ]
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "hello, world"
                  },
                  {
                    "type": "text",
                    "text": "hello, world"
                  }
                ]
              }
            ]
          }
        ]
      }
    }
"""