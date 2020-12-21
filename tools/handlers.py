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
import tools.resources as resources
import requests
from tools.database import (post_sql_query, create_userdata_table,
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
                                text=resources.answer7[1])
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '8':
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up1))
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up2))
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
        line_bot_api.push_message(current_user, template_message)
        time.sleep(15)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up3))
        time.sleep(5)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up4))
        time.sleep(1)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up4))
        time.sleep(1)
        line_bot_api.push_message(current_user, TextSendMessage(
                                        text=resources.follow_up5))
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
    if stage == '9':
        time.sleep(2)
        save_reply_to_db(stage_num=stage, answer=text, user=current_user)
        all_data = grab_all_data(user=current_user)[0]
        print(all_data)
        phone = all_data[10]
        name = all_data[2]
        sex = all_data[5]
        comment = f'อายุ: {all_data[4]}; '\
                    f'น้ำหนัก: {all_data[6]}; '\
                    f'ส่วนสูง: {all_data[7]}; '\
                    f'พลังงานที่เหลือในช่วงท้ายของวัน: {all_data[8]}; '\
                    f'อาหาร: {all_data[9]}; '
        reply = {
            'name': 'สม8จิจจต',
            'phone': phone,
            'internal_phone': '0629692931',
            'sex': sex,
            'comment': comment,
            'country_code': 'TH',
            'campaign_id':'967987',
            'sid1':'5901',
            'redirect_url':'https://line.me/en/'
        }
        x = requests.post(URL, data = reply)
        data = json.loads(x.text)
        print(x)
        print(data)
        print(reply)
