import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

@rizki.message_handler(commands=["start"])
def text(message):
    chatid = message.chat.id
    rizki.send_photo(chatid, open('1566206027.png','rb'))
def awal_bot(message):
    tahap1 = types.InlineKeyboardMarkup()
    tahap2 = types.InlineKeyboardButton(text="CHANNEL STORE",url="https://t.me/AZ_Dan_Rizki_Store636")
    tahap3 = types.InlineKeyboardButton(text="GRUP",url="https://t.me/GrupDanaGratis")
    tahap4 = types.InlineKeyboardButton(text="CHANNEL UTAMA",url="https://t.me/ChannelDanaGratis")
    tahap5 = types.InlineKeyboardButton(text="CHANNEL DAGET",url="https://t.me/DanaKagetTeam")
    tahap1.add(tahap2)
    tahap1.add(tahap3,tahap4)
    tahap1.add(tahap5)
    rizki.send_message(message.chat.id,"List Harga Yang Kami Jual\n===========\nYouTube Premium 4 Bulan = 3k\nYouTube Premium 1 Bulan = 1k\nNokos Telegram USA = 1.200\nNokos Telegram ID = 1.900\nNokos WhatsApp = 1k\n===========\nMinat Hubungi @Nokos_Rizki_Bot\n==========\nCommand yang tersedia di bot ini =\n/admin untuk melihat kontak admin",reply_markup=tahap1)
    rizki.send_message(message.chat.id,"Bot By @Rizki636 --> Github --> Heroku --> Telegram")

@rizki.message_handler(commands=["admin"])
def awal_bot(message):
    dest1 = types.InlineKeyboardMarkup()
    dest2 = types.InlineKeyboardButton(text="KONTAK ADMIN",url="https://t.me/Rizki636")
    dest1.add(dest2)
    rizki.send_message(message.chat.id,"ini adalah kontak admin",reply_markup=dest1)
print("bot berjalan")
rizki.polling()
