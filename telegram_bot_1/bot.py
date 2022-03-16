import telebot
import configure

TOKEN = str(configure.config['token'])
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def comm(message):
    bot.send_message(message.chat.id, 'Приветствие от /start')
    f = open('users.txt', 'a')
    f.write(message.chat.username+'\n'+str(message.chat.id)+'\n')
    f.close()

@bot.message_handler(content_types = ['text'])#.message_handler - обработчик поступающих сообщщений
def function_name(message):
    if message.text.lower() in ['привет','приветик']:
        bot.send_message(message.chat.id, "Привет, Пирожуля!)")
    else:
            bot.send_message(message.chat.id, "Нужно поздороваться")

@bot.message_handler(content_types = ['photo'])#.message_handler - обработчик поступающих сообщщений
def function_name(message):
            bot.send_message(message.chat.id, "Это фото!)")

#@DECOR()
#def dobavlenie():
#    f = open('users.txt', 'a')
#    f.write(message.chat.username+'\n'+str(message.chat.id)+'\n')
#    f.close()



bot.polling(none_stop=True)  # запуск постоянной работы

#    elif message:
#       bot.send_message(message, "Красивый голос")

