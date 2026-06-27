import telebot
from dotenv import load_dotenv

from src.config.config import Config

load_dotenv()

bot = telebot.TeleBot(Config.TOKEN_TELEGRAM)


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id

    print(f"Chat ID: {chat_id}")

    bot.reply_to(message, f"Seu Chat ID é:\n<code>{chat_id}</code>", parse_mode="HTML")


print("Bot iniciado...")
bot.infinity_polling()
