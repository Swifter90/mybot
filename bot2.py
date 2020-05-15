#!/usr/bin/env python

import requests
import telebot
from telebot import types


bot = telebot.TeleBot("632863901:AAHVy_wW42DKrz4XAKwK1asZZWWxLFhIdc4")


@bot.message_handler(commands=['start', 'choose'])
def send_welcome(message):
	bot.reply_to(message, "What do you want")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "@i_k_o_m is my Owner")

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('privet'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('privet'))
        bot.answer_inline_query(inline_query.id, ['kak dela', 'bratan'])
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling(timeout=60)

