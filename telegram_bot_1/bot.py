import telebot
import configure
import requests
import json

TOKEN = str(configure.config['token'])
bot = telebot.TeleBot(TOKEN)
TOKEN_API = str(configure.config['token_api'])
#nal = requests.get(f'http://api.exchangeratesapi.io/v1/symbols?access_key={TOKEN_API}')
#slovar_values = json.loads(nal.content)['symbols']

def dobavlenie(message):
    f = open('users.txt', 'a')
    f.write(message.chat.username+'\n'+str(message.chat.id)+'\n')
    f.close()

@bot.message_handler(commands=['start', 'help'])
def comm(message):
    a = message.chat.username
    bot.send_message(message.chat.id, f"Приветствую, {a}!\nЯ умею конвертировать валюту.\n"
                                      f"Для этого Вам необходимо ввести данные следующим образом:\n <название валюты, цену которой хотите узнать>"
                                      f"<имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.\n"
                                      f"Для того, чтобы узнать список доступных валют введите команду: /values")
    dobavlenie(message)
#    f = open('users.txt', 'a')
#    f.write(message.chat.username+'\n'+str(message.chat.id)+'\n')
#    f.close()
@bot.message_handler(commands=['values'])
def val(message):
    nal = requests.get(f'http://api.exchangeratesapi.io/v1/symbols?access_key={TOKEN_API}')
    slovar_values = json.loads(nal.content)['symbols'].items()
    otvet_1 = []
    for key,value in slovar_values:
        otvet_1.append(key+' : '+value)
    otvet = '\n'.join(otvet_1)
    bot.send_message(message.chat.id, f"Доступные валюты:\n{otvet}")

@bot.message_handler(content_types = ['text'])
def otvet(message):
    val1, val2, kol = message.text.split(' ')
    r = requests.get(f'http://api.exchangeratesapi.io/{TOKEN_API}/convert?from={val1}&to={val2}&itog={kol}')
    otvet_api = json.loads(r.content)['info']['rate']
    itog = f'Цена {kol} {val1} в {val2}={otvet_api}'
    bot.send_message(message.chat.id, itog)



#@bot.message_handler(content_types = ['text']) #.message_handler - обработчик поступающих сообщщений
#def function_name(message):
#    if message.text.lower() in ['привет','приветик']:
#        bot.send_message(message.chat.id, "Привет, "+message.chat.username+"!")
 #   else:
#        bot.send_message(message.chat.id, "Нужно поздороваться")
    #dobavlenie(message)

#@bot.message_handler(content_types = ['photo'])#.message_handler - обработчик поступающих сообщщений
#def function_name(message):
#            bot.send_message(message.chat.id, "Это фото!)")



bot.polling(none_stop=True)  # запуск постоянной работы


