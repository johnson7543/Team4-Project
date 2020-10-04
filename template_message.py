from linebot.models import (
    TemplateSendMessage,FlexSendMessage,ButtonsTemplate,MessageTemplateAction
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
              "label": "顯示五筆就好",
              "text": "5"
            },
            "margin": "md",
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "我其實是原住民",
              "text": "原住民"
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
              "label": "我住離島啦",
              "text": "hello"
            },
            "margin": "md",
            "style": "secondary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "text": "天龍人",
              "label": "我住在台北市哦"
            },
            "height": "sm",
            "margin": "md",
            "position": "relative",
            "style": "primary"
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
              "label": "顯示十筆好了",
              "text": "10"
            },
            "margin": "md",
            "style": "primary",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "隨機來一筆",
              "text": "random"
            },
            "height": "sm",
            "margin": "md",
            "position": "relative",
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "text": "取消",
              "label": "我不想查獎學金了"
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
              "label": "我想改查itouch的公告",
              "text": "查詢itouch公告"
            },
            "margin": "md",
            "style": "secondary",
            "height": "sm"
          }
        ],
        "backgroundColor": "#2894FF"
      }
    }
  ]
})

iouch_template = TemplateSendMessage(
                            alt_text='請選擇公告類別',
                            template=ButtonsTemplate(
                                title='公告類別',
                                text='請選擇公告類別',
                                actions=[
                                    MessageTemplateAction(
                                        label='行政公告',
                                        text='Itouch_行政公告'
                                    ),
                                    MessageTemplateAction(
                                        label='校內/校外徵才',
                                        text='Itouch_校內/校外徵才'
                                    ),
                                    MessageTemplateAction(
                                        label='校外來文',
                                        text='Itouch_校外來文'
                                    ),
                                    MessageTemplateAction(
                                        label='實習就業',
                                        text='Itouch_實習就業'
                                    )                                    
                                ]
                            )
                        )

