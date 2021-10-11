
import os
import telebot # Importamos las librería
#import pyscreenshot
#import pyautogui
from time import sleep
import subprocess

TOKEN = '1994301852:AAFtdPBsXDrhtOFtB0m9CBYCKmYJrvksFvA' # Ponemos nuestro Token generado con el @BotFather

import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['pools'])
def send_welcome(message):
#    im = pyscreenshot.grab()   
 #   sleep(2)
  #  im.show()
   # im.save("screenshot.jpg")
    #screenshot = pyautogui.screenshot()
    #screenshot.save("screenshot.png")
    #os.system("echo Hello from the other side!")
    subprocess.call('start /wait py screen.py', shell=True)
    sleep(20)
    bot.reply_to(message, "Te comparto los pools, NO ES CONSEJO DE INVERSIÓN")
    photo = open('screenshot.png', 'rb')
    bot.send_photo(-1001308174545,photo)




@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

#captura de pantalla


#mandar la wallet para donaciones

