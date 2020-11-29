from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, SourceUser, ImageCarouselTemplate,
    ImageCarouselColumn, ButtonsTemplate, BubbleContainer, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ImageComponent, ButtonComponent,
    SeparatorComponent, TemplateSendMessage, MessageAction, PostbackAction, ConfirmTemplate,
    FlexSendMessage, ImageMessage)
from linebot import LineBotApi, WebhookHandler
import time
import json
import os
import sys
import resources
import requests
from database import (post_sql_query, create_userdata_table,
                        user_in_db, save_reply_to_db, grab_all_data)


channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None or channel_access_token is None:
    print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
URL = 'https://tracker.everad.com/conversion/new'


def message_handler(event, stage, current_user, text):
    if stage == '3':
        time.sleep(2)
        buttons_template = ButtonsTemplate(text=resources.sentence3,
            actions=[
                MessageAction(label=resources.answer3[0],
                                text=resources.answer3_1[0]),
                MessageAction(label=resources.answer3[1],
                                text=resources.answer3_1[1])
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '4':
        time.sleep(2)
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=resources.sentence4))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '5':
        time.sleep(2)
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=resources.sentence5))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '6':
        time.sleep(2)
        buttons_template = ButtonsTemplate(text=resources.sentence6, actions=[
                MessageAction(label=resources.answer6[0],
                                text=resources.answer6[0]),
                MessageAction(label=resources.answer6[1],
                                text=resources.answer6[1])
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '7':
        time.sleep(2)
        buttons_template = ButtonsTemplate(text=resources.sentence7, actions=[
                MessageAction(label=resources.answer7[0],
                                text=resources.answer7[0]),
                MessageAction(label=resources.answer7[1],
                                text=resources.answer7[1]),
                MessageAction(label=resources.answer7[2],
                                text=resources.answer7[2]),
                MessageAction(label=resources.answer7[3],
                                text=resources.answer7[3])
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '8':
        time.sleep(2)
        buttons_template = ButtonsTemplate(text=resources.sentence8, actions=[
                MessageAction(label=resources.answer8[0],
                                text=resources.answer8[0]),
                MessageAction(label=resources.answer8[1],
                                text=resources.answer8[1]),
                MessageAction(label=resources.answer8[2],
                                text=resources.answer8[2])
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '9':
        time.sleep(2)
        buttons_template = ButtonsTemplate(text=resources.sentence9, actions=[
                MessageAction(label=resources.answer9[0],
                                text=resources.answer9[0]),
                MessageAction(label=resources.answer9[1],
                                text=resources.answer9[1])
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '10':
        time.sleep(2)
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=resources.sentence10))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '11':
        time.sleep(2)
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=resources.sentence11))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '12':
        time.sleep(2)
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=resources.sentence12))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '13':
        time.sleep(2)
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=resources.sentence13))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '14':
        time.sleep(2)
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=resources.sentence14))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '15':
        time.sleep(2)
        buttons_template = ButtonsTemplate(text=resources.sentence15, actions=[
                MessageAction(label=resources.answer15[0],
                                text=resources.answer15[0]),
                MessageAction(label=resources.answer15[1],
                                text=resources.answer15[1])
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '16':
        time.sleep(2)
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    TextComponent(text=resources.sentence16,
                                    wrap=True),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer16[0],
                                            text=resources.answer16[0]),
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer16[1],
                                            text=resources.answer16[1])
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer16[2],
                                            text=resources.answer16[2])
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer16[3],
                                            text=resources.answer16[3])
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer16[4],
                                            text=resources.answer16[4])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '17':
        time.sleep(2)
        buttons_template = ButtonsTemplate(text=resources.sentence17, actions=[
                MessageAction(label=resources.answer17[0],
                                text=resources.answer17[0]),
                MessageAction(label=resources.answer17[1],
                                text=resources.answer17[1]),
                MessageAction(label=resources.answer17[2],
                                text=resources.answer17[2]),
                MessageAction(label=resources.answer17[3],
                                text=resources.answer17[3])
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '18':
        time.sleep(2)
        line_bot_api.push_message(
            current_user, TextSendMessage(text=resources.sentence18))
        time.sleep(2)
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    TextComponent(text=resources.sentence18_1,
                                    wrap=True),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer18[0],
                                            text=resources.answer18[0]),
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer18[1],
                                            text=resources.answer18[1])
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer18[2],
                                            text=resources.answer18[2])
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer18[3],
                                            text=resources.answer18[3])
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer18[4],
                                            text=resources.answer18[4])
                    ),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer18[5],
                                            text=resources.answer18[5])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '19':
        time.sleep(2)
        if text == resources.answer18[0]:
            bubble = BubbleContainer(
                size='kilo',
                direction='ltr',
                hero=ImageComponent(
                    url='https://www.5gkb.by/images/bolezn/ostrye-boli-v-zhivote.jpg',
                    size='full'
                ),
                body=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        TextComponent(text=resources.sentence19_1,
                                        wrap=True),
                        ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer19[0],
                                            text=resources.answer19[0])
                        )
                    ]
                ),
            )
            message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
            line_bot_api.reply_message(event.reply_token,message)
        if text == resources.answer18[1]:
            bubble = BubbleContainer(
                size='kilo',
                direction='ltr',
                hero=ImageComponent(
                    url='https://www.5gkb.by/images/bolezn/ostrye-boli-v-zhivote.jpg',
                    size='full'
                ),
                body=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        TextComponent(text=resources.sentence19_2,
                                        wrap=True),
                        ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer19[0],
                                            text=resources.answer19[0])
                        )
                    ]
                ),
            )
            message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
            line_bot_api.reply_message(event.reply_token,message)
        if text == resources.answer18[2]:
            bubble = BubbleContainer(
                size='kilo',
                direction='ltr',
                hero=ImageComponent(
                    url='https://www.5gkb.by/images/bolezn/ostrye-boli-v-zhivote.jpg',
                    size='full'
                ),
                body=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        TextComponent(text=resources.sentence19_3,
                                        wrap=True),
                        ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer19[0],
                                            text=resources.answer19[0])
                        )
                    ]
                ),
            )
            message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
            line_bot_api.reply_message(event.reply_token,message)
        if text == resources.answer18[3]:
            bubble = BubbleContainer(
                size='kilo',
                direction='ltr',
                hero=ImageComponent(
                    url='https://www.5gkb.by/images/bolezn/ostrye-boli-v-zhivote.jpg',
                    size='full'
                ),
                body=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        TextComponent(text=resources.sentence19_4,
                                        wrap=True),
                        ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer19[0],
                                            text=resources.answer19[0])
                        )
                    ]
                ),
            )
            message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
            line_bot_api.reply_message(event.reply_token,message)
        if text == resources.answer18[4]:
            bubble = BubbleContainer(
                size='kilo',
                direction='ltr',
                hero=ImageComponent(
                    url='https://www.5gkb.by/images/bolezn/ostrye-boli-v-zhivote.jpg',
                    size='full'
                ),
                body=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        TextComponent(text=resources.sentence19_5,
                                        wrap=True),
                        ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer19[0],
                                            text=resources.answer19[0])
                        )
                    ]
                ),
            )
            message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
            line_bot_api.reply_message(event.reply_token,message)
        if text == resources.answer18[5]:
            bubble = BubbleContainer(
                size='kilo',
                direction='ltr',
                hero=ImageComponent(
                    url='https://www.5gkb.by/images/bolezn/ostrye-boli-v-zhivote.jpg',
                    size='full'
                ),
                body=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        TextComponent(text=resources.sentence19_6,
                                        wrap=True),
                        ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label=resources.answer19[0],
                                            text=resources.answer19[0])
                        )
                    ]
                ),
            )
            message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
            line_bot_api.reply_message(event.reply_token,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '20':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up1))
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up2))
        time.sleep(2)
        line_bot_api.push_message(current_user,TextSendMessage(
                                        text=resources.follow_up3))
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                spacing='xs',
                contents=[
                    ButtonComponent(
                    style='link',
                    height='sm',
                    action=MessageAction(label=resources.answer20[0],
                                        text=resources.answer20[0])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.push_message(current_user,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '21':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up4))
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up5))
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    ButtonComponent(
                    style='link',
                    height='sm',
                    action=MessageAction(label=resources.answer21[0],
                                        text=resources.answer21[0])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.push_message(current_user,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '22':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up6))
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up7))
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    ButtonComponent(
                    style='link',
                    height='sm',
                    action=MessageAction(label=resources.answer22[0],
                                        text=resources.answer22[0])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.push_message(current_user,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '23':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up8))
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up9))
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    ButtonComponent(
                    style='link',
                    height='sm',
                    action=MessageAction(label=resources.answer23[0],
                                        text=resources.answer23[0])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.push_message(current_user,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '24':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up10))

        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url='https://i.ibb.co/cJchm40/1.jpg',
                                action=PostbackAction(data='example1')),
            ImageCarouselColumn(image_url='https://i.ibb.co/F0pjf87/2.jpg',
                                action=PostbackAction(data='example2')),
            ImageCarouselColumn(image_url='https://i.ibb.co/mD6GfYR/3.jpg',
                                action=PostbackAction(data='example3')),
            ImageCarouselColumn(image_url='https://i.ibb.co/fNkWmSw/4.jpg',
                                action=PostbackAction(data='example4')),
            ImageCarouselColumn(image_url='https://i.ibb.co/nn9wzcZ/5.jpg',
                                action=PostbackAction(data='example5')),
        ])
        template_message = TemplateSendMessage(
            alt_text='ImageCarousel alt text', template=image_carousel_template)
        time.sleep(2)
        line_bot_api.push_message(current_user, template_message)
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    ButtonComponent(
                    style='link',
                    height='sm',
                    action=MessageAction(label=resources.answer24[0],
                                        text=resources.answer24[0])
                    )
                ]
            )
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.push_message(current_user,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '25':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up11))
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    ButtonComponent(
                    style='link',
                    height='sm',
                    action=MessageAction(label=resources.answer25[0],
                                        text=resources.answer25[0])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.push_message(current_user,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '26':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up12))
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    ButtonComponent(
                    style='link',
                    height='sm',
                    action=MessageAction(label=resources.answer26[0],
                                        text=resources.answer26[0])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.push_message(current_user,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '27':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up13))
        bubble = BubbleContainer(
            size='kilo',
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    ButtonComponent(
                    style='link',
                    height='sm',
                    action=MessageAction(label=resources.answer27[0],
                                        text=resources.answer27[0])
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Buttons alt text", contents=bubble)
        line_bot_api.push_message(current_user,message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '28':
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up14))
        time.sleep(2)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up15))
        time.sleep(2)
        bubble_string = """
        {
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://nature-tricks.com/wp-content/uploads/2020/05/keto-eat-fit-capsules-review.jpg",
                "position": "relative",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "1:1",
                "gravity": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Keto Eat & Fit",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#ffffff"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "$200",
                        "color": "#a9a9a9",
                        "decoration": "line-through",
                        "align": "end"
                      },
                      {
                        "type": "text",
                        "text": "$100",
                        "color": "#ebebeb",
                        "size": "xl",
                        "align": "end"
                      }
                    ]
                  }
                ],
                "position": "absolute",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px",
                "backgroundColor": "#00000099",
                "paddingAll": "20px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "SALE",
                    "color": "#ffffff"
                  }
                ],
                "position": "absolute",
                "backgroundColor": "#ff2600",
                "cornerRadius": "20px",
                "paddingAll": "5px",
                "offsetTop": "10px",
                "offsetEnd": "10px",
                "paddingStart": "10px",
                "paddingEnd": "10px"
              }
            ],
            "paddingAll": "0px"
          }
        }
        """
        message = FlexSendMessage(alt_text="hello", contents=json.loads(bubble_string))
        line_bot_api.push_message(
            current_user,
            message
        )
        time.sleep(2)
        line_bot_api.push_message(
            current_user,TextSendMessage(text=resources.sentence20))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '29':
        time.sleep(2)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=resources.sentence21))
        all_data = grab_all_data(user=current_user)[0]
        # result = ''
        # for column in all_data:
        #     try:
        #         result.join(str(column)+'\n')
        #     except TypeError:
        #         continue
        phone = all_data[-1]
        name = all_data[2]
        # zodiac_sign = f'Возраст: {all_data[4]}; '\
        #             f'Пол: {all_data[5]}; '\
        #             f'Вес: {all_data[6]}; '\
        #             f'Рост: {all_data[7]}; '\
        #             f'Занимается спортом: {all_data[8]}; '\
        #             f'Времени спит: {all_data[9]}; '\
        #             f'Легко просыпается: {all_data[10]}; '\
        #             f'Энергии под конец дня: {all_data[11]}; '\
        #             f'Приемов пищи: {all_data[12]}; '\
        #             f'Рацион: {all_data[13]}; '\
        #             f'Алкоголь: {all_data[14]}; '\
        #             f'Диеты: {all_data[15]}; '\
        #             f'Аллергии: {all_data[16]};'\
        #             f'Регулярный стул: {all_data[17]}; '\
        #             f'Области тела исправить: {all_data[18]}; '\
        #             f'Самочувствие: {all_data[19]};'
        zodiac_sign = f'Возраст: {all_data[4]}; '\
                    f'Вес: {all_data[6]}; '\
                    f'Рост: {all_data[7]}; '
                    # f'Занимается спортом: {all_data[8]}; '\
                    # f'Времени спит: {all_data[9]}; '\
                    # f'Легко просыпается: {all_data[10]}; '\
                    # f'Энергии под конец дня: {all_data[11]}; '\
                    # f'Приемов пищи: {all_data[12]}; '\
                    # f'Рацион: {all_data[13]}; '\
                    # f'Алкоголь: {all_data[14]}; '\
                    # f'Диеты: {all_data[15]}; '\
                    # f'Аллергии: {all_data[16]};'\
                    # f'Регулярный стул: {all_data[17]}; '\
                    # f'Области тела исправить: {all_data[18]}; '\
                    # f'Самочувствие: {all_data[19]};'

        reply = {
            'name': name,
            'phone': phone,
            'sex': 'Мужчина',
            'zodiac_sign': zodiac_sign,
            'campaign_id':'964667',
            'sid1':'5901',
            'redirect_url':'https://line.me/en/'
        }
        x = requests.post(URL, data = reply)
        print(x)