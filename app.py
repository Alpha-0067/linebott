from flask import Flask, request, abort
from linebot import (
LineBotApi, WebhookHandler
)
from linebot.exceptions import (
InvalidSignatureError
)
from linebot.models import (
MessageEvent, TextMessage, TextSendMessage
)

app = Flask(__name__)

ACCESS_TOKEN = "kdiwhVZxJE8j7TEmZ7fC9cIVBmlPEvaobqEYbe1JmDt8tiGoJP8LZtWMVPwtSHCjP9B9q5x7L2uYTETvFeHaxJEm4ktWqpEiwo6d/7lZN6xuHA7ML1zWFaAsYxTRGm0enyMPPJM1DqKrJGauPaCzNkDQdB04t89="
SECRET = "c6640bb49b596db0b5d2930c7b5cac64"

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
   signature = request.headers['X-Line-Signature'] 
   body = request.get_data(as_text=True)
   app.logger.info("Request body: " + body)

   try:
      handler.handle(body, signature)
   except InvalidSignatureError:
      abort(400)

   return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
   line_bot_api.reply_message(
   event.reply_token,
   TextSendMessage(text=event.message.text))

if __name__ == "__main__":
   app.run()