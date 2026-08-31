"""Echo bot — reacts to commands, text and every media type Telegram sends.

Run:
    cp .env.example .env      # add BOT_TOKEN
    pip install -r requirements.txt
    python main.py
"""
import os

from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Message

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set. Copy .env.example to .env and fill it in.")

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def reaction_start(message : Message):
    chat_id = message.chat.id
    first_tname = message.from_user.first_name
    bot.send_message(chat_id, f"salom, {first_tname}")


@bot.message_handler(regexp='Salom')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'salom ubu narsa istaysizmi?')


@bot.message_handler(content_types=['text'])
def reaction_text(message:Message):
    chat_id = message.chat.id
    text = message.text
    bot.send_message(chat_id, text)

@bot.message_handler(content_types=['photo'])
def reaction_photo(message: Message):
    chat_id = message.chat.id
    file_id = message.photo[-1].file_id
    bot.send_photo(chat_id, file_id)

@bot.message_handler(content_types=['document'])
def reaction_document(message: Message):
    chat_id = message.chat.id
    document_id = message.document.file_id
    bot.send_document(chat_id, document_id)

@bot.message_handler(content_types=['voice'])
def reaction_voice(message: Message):
    chat_id = message.chat.id
    voice_id = message.voice.file_id
    bot.send_voice(chat_id, voice_id)

@bot.message_handler(content_types=['video'])
def reaction_video(message: Message):
    chat_id = message.chat.id
    video_id = message.video.file_id
    bot.send_video(chat_id, video_id)

@bot.message_handler(content_types=['audio'])
def reaction_audio(message: Message):
    chat_id = message.chat.id
    audio_id = message.audio.file_id
    bot.send_audio(chat_id, audio_id)

if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
