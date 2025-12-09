import os
import telebot

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['video'])
def handle_video(msg):
    bot.reply_to(msg, "ویدیو دریافت شد! در نسخه کامل ادیت می‌شود.")

bot.polling()
