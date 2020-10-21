# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:47:09 2020

@author: LIN
"""
#一個BUBBLE的字典
#用來製作Flex Message
Bubble_Type =     {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "margin": "none",
            "size": "full",
            "aspectMode": "cover",
            "animated": True
          }
        ],
        "backgroundColor": "#D0D0D0"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "搜尋結果",
            "size": "xl",
            "weight": "bold",
            "position": "relative",
            "align": "center",
            "wrap": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          }
        ],
        "paddingTop": "none",
        "backgroundColor": "#D0D0D0"
      }
    }


Bubble_Scholarship_Type =    {
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "這是獎學金標題",
        "size": "xl",
        "position": "relative",
        "weight": "bold",
        "wrap": True,
        "align": "center"
      }
    ],
    "backgroundColor": "#D0D0D0"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "截止日期",
        "size": "lg",
        "margin": "none"
      },
      {
        "type": "text",
        "text": "金額",
        "size": "lg",
        "margin": "md"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "uri": "http://linecorp.com/",
          "label": "點我領錢"
        },
        "style": "primary",
        "position": "relative",
        "margin": "xxl",
        "height": "md",
        "offsetTop": "xs"
      }
    ],
    "backgroundColor": "#F0F0F0"
  }
}