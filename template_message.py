from linebot.models import (
    FlexSendMessage
)

scholarship_template = FlexSendMessage( alt_text='更多篩選...',
contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "更多篩選條件...",
            "size": "xxl",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "我想看錢最多的",
              "text": "No money no life."
            },
            "margin": "md",
            "style": "primary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "text": "Close soon...",
              "label": "我想看即將截止的"
            },
            "height": "sm",
            "margin": "md",
            "position": "relative",
            "style": "secondary",
            "color": "#84C1FF"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "text": "Are you SURE？",
              "label": "我想看\"全部\"的資料"
            },
            "height": "sm",
            "margin": "md",
            "position": "relative",
            "style": "secondary",
            "color": "#FF79BC"
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "我想看資料來源",
              "uri": "https://itouch.cycu.edu.tw/active_system/query_data/student/ssgogo.jsp"
            },
            "style": "secondary",
            "height": "sm",
            "margin": "lg",
            "color": "#FFB5B5"
          }
        ],
        "backgroundColor": "#9393FF"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "多！還要更多！",
            "color": "#000000",
            "size": "xxl"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "我想重新篩選",
              "text": "Conversation reset."
            },
            "margin": "md",
            "style": "primary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "text": "Goodbye.",
              "label": "我不想查獎學金了"
            },
            "style": "secondary",
            "position": "relative",
            "margin": "md",
            "height": "sm",
            "color": "#84C1FF"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "我想改查itouch的公告",
              "text": "查詢itouch公告"
            },
            "margin": "md",
            "style": "secondary",
            "height": "sm",
            "color": "#FF79BC"
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "聯絡我們",
              "uri": "mailto:johnson7543@cycu.org.tw"
            },
            "style": "secondary",
            "height": "sm",
            "margin": "lg",
            "color": "#FFB5B5"
          }
        ],
        "backgroundColor": "#2894FF"
      }
    }
  ]
})

iouch_template =  FlexSendMessage( alt_text='公告類別...',
contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "請選擇公告類別",
            "size": "xxl",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "行政公告",
              "text": "Itouch_行政公告"
            },
            "margin": "md",
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "校內或校外徵才",
              "text": "Itouch_校內/校外徵才"
            },
            "style": "primary",
            "position": "relative",
            "margin": "md",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "校外來文",
              "text": "Itouch_校外來文"
            },
            "margin": "md",
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "text": "Itouch_實習就業",
              "label": "實習就業"
            },
            "height": "sm",
            "margin": "md",
            "position": "relative",
            "style": "primary"
          }
        ],
        "backgroundColor": "#9393FF"
      }
    }
  ]
})

