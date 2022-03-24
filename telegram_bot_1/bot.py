import telebot
import configure

TOKEN = str(configure.config['token'])
bot = telebot.TeleBot(TOKEN)
nal = {
    'Доллар': '',
    'Евро': '',
    'Лира': ''

}

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
    cd = ' \n'.join(nal.keys())
    bot.send_message(message.chat.id, f"Доступные валюты:\n{cd}")



@bot.message_handler(content_types = ['text']) #.message_handler - обработчик поступающих сообщщений
def function_name(message):
    if message.text.lower() in ['привет','приветик']:
        bot.send_message(message.chat.id, "Привет, "+message.chat.username+"!")
    else:
        bot.send_message(message.chat.id, "Нужно поздороваться")
    dobavlenie(message)

@bot.message_handler(content_types = ['photo'])#.message_handler - обработчик поступающих сообщщений
def function_name(message):
            bot.send_message(message.chat.id, "Это фото!)")



bot.polling(none_stop=True)  # запуск постоянной работы


