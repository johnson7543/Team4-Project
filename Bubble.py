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
        ]
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
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#000000",
          "endColor": "#ffffff"
        }
      }
    }