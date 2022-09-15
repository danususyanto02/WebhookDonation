from email import message
from os import abort
from urllib import response
import pyautogui
from slack_sdk.webhook import WebhookClient
from flask import Flask, request
from pywinauto.keyboard import send_keys

app = Flask(__name__)



@app.route('/', methods=['POST'])
def index():
    send_keys('{ENTER}')
    pyautogui.write("Lo semua cupu anjing, by 1 sini sama gua")
    send_keys('{ENTER}')
    return ('Ini Web Hook Brok.', 200, None)

if __name__ == '__main__':
  app.run(debug=True)


