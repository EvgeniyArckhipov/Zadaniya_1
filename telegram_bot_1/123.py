import telebot
import configure
import requests
import json

TOKEN = str(configure.config['token'])
bot = telebot.TeleBot(TOKEN)
TOKEN_API = str(configure.config['token_api'])


#val1, val2, kol = message.text.split(' ')
val1 = 'UZD'
val2 = 'CAD'
kol = '200'
r = requests.get(f'http://api.exchangeratesapi.io/v1/convert?access_key={TOKEN_API}&from={val1}&to={val2}&itog={kol}')
otvet_api = json.loads(r.content)
print(otvet_api)
#itog = f'Цена {kol} {val1} в {val2}={otvet_api}'
#bot.send_message(message.chat.id, itog)
