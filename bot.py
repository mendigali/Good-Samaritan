import telebot
import random

from telebot import types

TOKEN = '1422772240:AAEYWYt-heBexwfnSa_ZEYLnh9-X8huIKwA'

bot = telebot.TeleBot(TOKEN)

# First time message
@bot.message_handler(commands=['start'])
def welcome(message):
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('🗿✂️📄 Давай сыграем! 🗿✂️📄')

	markup.add(item1)

	bot.send_message(message.chat.id, 'Добро пожаловать, <b>{0.first_name}</b>!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы играть в 🗿Камень ✂️Ножницы 📄Бумага.'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

# User item picker
@bot.message_handler(content_types=['text'])
def play(message):
	if message.chat.type == 'private':
		if message.text == '🗿✂️📄 Давай сыграем! 🗿✂️📄':
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton('🗿 Камень', callback_data='rock')
			item2 = types.InlineKeyboardButton('✂️ Ножницы', callback_data='scissors')
			item3 = types.InlineKeyboardButton('📄 Бумага', callback_data='paper')

			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Хорошо, я выбрал чем буду ходить. Теперь твоя очередь:', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

# Handling and processing user input
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			possibleItems = ['rock', 'paper', 'scissors']
			eng_to_rus = {
				'rock': '🗿 камень',
				'paper': '📄 бумагу',
				'scissors': '✂️ ножницы'
			}
			bot_item = random.choice(possibleItems)
			user_item = call.data
			if user_item == bot_item:
				bot.send_message(call.message.chat.id, 'Ничья!')
			elif user_item == 'rock' and bot_item == 'paper':
				bot.send_message(call.message.chat.id, 'Ты проиграл! Я выбрал 📄 бумагу, а 📄 бумага обёртывает 🗿 камень!')
			elif user_item == 'paper' and bot_item == 'scissors':
				bot.send_message(call.message.chat.id, 'Ты проиграл! Я выбрал ✂️ ножницы, а ✂️ ножницы режут 📄 бумагу!')
			elif user_item == 'scissors' and bot_item == 'rock':
				bot.send_message(call.message.chat.id, 'Ты проиграл! Я выбрал 🗿 камень, а 🗿 камень ломает ✂️ ножницы!')
			else:
				bot.send_message(call.message.chat.id, 'Ты выиграл!')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Хорошо, я выбрал чем буду ходить. Теперь твоя очередь:', reply_markup=None)
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=(f'Ты выбрал {eng_to_rus.get(user_item)}.\n Бот выбрал {eng_to_rus.get(bot_item)}.'))

	except Exception as e:
		bot.send_message(call.message.chat.id, repr(e))

# RUN
bot.polling(none_stop=True)