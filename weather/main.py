import telebot
import requests
import json

bo = telebot.TeleBot('6925204328:AAF5HoQVZwRURsZTDq_mqZpT97rcASEPtpc') #api of our bot
API = '2209f28a7158c2ac726e69c5efc514fd' #go to the website - https://openweathermap.org/ =)

@bo.message_handler(commands=['start'])
def start(message):
    bo.send_message(message.chat.id, f"Hi {message.from_user.first_name}! Write the name of the city!")

@bo.message_handler(content_types=['text'])
def tt(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        dat = json.loads(res.text)
        bo.reply_to(message, f'Current weather: {dat["main"]["temp"]}')
    else:
        bo.reply_to(message, f'The city is listed incorrectly!!!')


bo.polling(none_stop=True)