import telebot
import configure

TOKEN = configure.config['token']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types = ['text','photo']) #.message_handler - обработчик поступающих сообщщений
def function_name(message):
    if message.text == True:
        if message.text.lower() in ['привет','приветик']:
            bot.reply_to(message, "Привет, Пирожуля!)")
        else:
            bot.reply_to(message,"Нужно поздороваться")
    elif message. :
        bot.send_message(message, "Красивый голос")

bot.polling(none_stop=True) #запуск постоянной работы