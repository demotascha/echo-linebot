import os
import requests
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

CHANNEL_ACCESS_TOKEN = os.environ.get('CHANNEL_ACCESS_TOKEN', 'Specified environment variable is not set.')
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET', 'Specified environment variable is not set.')

# Channel Access Token
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(CHANNEL_SECRET)

def callback(request):
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# handle message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    message = TextSendMessage(text=u'嗨！' + text)
    line_bot_api.reply_message(event.reply_token, message)
