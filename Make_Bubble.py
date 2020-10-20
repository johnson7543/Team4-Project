# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:56:32 2020

@author: LIN
"""
#從Bubble.py導入字典Bubble_Type
import Bubble
A_bubble = Bubble.Bubble_Type
print(type(A_bubble)) #dict

#創造一個Total
Total = { "type": "carousel","contents": [] }
print(Total)

Get_Total() :
    
Total["contents"].append(A_bubble)
Total["contents"].append(A_bubble)
print(Total)

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