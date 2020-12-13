import telebot
import random
import time
import string
from telebot import types

TOKEN = '1313844607:AAETgl4Lx33MVRNY68b-VKGvNwx3zzFifkU'

bot = telebot.TeleBot(TOKEN)

PASSWORD_LENGTH = 8
PASSWORD_LOWERCASE_ALLOWED = True
PASSWORD_UPPERCASE_ALLOWED = False
PASSWORD_DIGITS_ALLOWED = True
PASSWORD_SYMBOLS_ALLOWED = False

def correctSettings():
    global PASSWORD_LOWERCASE_ALLOWED
    global PASSWORD_UPPERCASE_ALLOWED
    global PASSWORD_DIGITS_ALLOWED
    global PASSWORD_SYMBOLS_ALLOWED
    if PASSWORD_LOWERCASE_ALLOWED:
        return True
    if PASSWORD_UPPERCASE_ALLOWED:
        return True
    if PASSWORD_DIGITS_ALLOWED:
        return True
    if PASSWORD_SYMBOLS_ALLOWED:
        return True
    return False

def generate_password():
    global PASSWORD_LENGTH
    global PASSWORD_LOWERCASE_ALLOWED
    global PASSWORD_UPPERCASE_ALLOWED
    global PASSWORD_DIGITS_ALLOWED
    global PASSWORD_SYMBOLS_ALLOWED
    characters = ''
    if PASSWORD_LOWERCASE_ALLOWED:
        characters += string.ascii_lowercase
    if PASSWORD_UPPERCASE_ALLOWED:
        characters += string.ascii_uppercase
    if PASSWORD_DIGITS_ALLOWED:
        characters += string.digits
    if PASSWORD_SYMBOLS_ALLOWED:
        characters += string.punctuation
    password = ''.join([random.choice(characters) for n in range(PASSWORD_LENGTH)])
    return password

@bot.message_handler(commands=['start'])
def welcome_msg(message):
    msg_text = 'Добро пожаловать!\n'
    msg_text += 'Данный бот создан для того, чтобы генерировать пароли.\n'
    msg_text += 'Для того чтобы сгенерировать пароль введите команду\n'
    msg_text += '/generate'
    bot.send_message(message.chat.id, msg_text)

@bot.message_handler(commands=['generate'])
def menu(message):
    yes = '✅Да'
    no = '❌Нет'
    msg_text = 'Пароль будет сгенерирован используя настройки ниже:\n\n\n'
    msg_text += f'Длина пароля: {PASSWORD_LENGTH}\n\n'
    msg_text += f'🔡 Использовать маленькие буквы: {yes if PASSWORD_LOWERCASE_ALLOWED else no}\n\n'
    msg_text += f'🔠 Использовать большие буквы: {yes if PASSWORD_UPPERCASE_ALLOWED else no}\n\n'
    msg_text += f'🔢 Использовать цифры: {yes if PASSWORD_DIGITS_ALLOWED else no}\n\n'
    msg_text += f'🔣 Использовать другие символы и знаки препинания: {yes if PASSWORD_SYMBOLS_ALLOWED else no}\n\n\n'
    msg_text += 'Для того, чтобы сгенерировать пароль, нажмите кнопку "Сгенерировать пароль"\n'
    msg_text += 'Также при желании, вы можете изменить настройки.'

    allow = '✅Разрешить'
    not_allow = '❌Запретить'
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('🔑Сгенерировать пароль🔐', callback_data='generate_password')
    button2 = types.InlineKeyboardButton('Изменить длину пароля', callback_data='edit_password_length')
    button3 = types.InlineKeyboardButton(f'{not_allow if PASSWORD_LOWERCASE_ALLOWED else allow} использовать маленькие буквы', callback_data='toggle_lowercase')
    button4 = types.InlineKeyboardButton(f'{not_allow if PASSWORD_UPPERCASE_ALLOWED else allow} использовать большие буквы', callback_data='toggle_uppercase')
    button5 = types.InlineKeyboardButton(f'{not_allow if PASSWORD_DIGITS_ALLOWED else allow} использовать цифры', callback_data='toggle_digits')
    button6 = types.InlineKeyboardButton(f'{not_allow if PASSWORD_SYMBOLS_ALLOWED else allow} использовать символы и знаки препинания', callback_data='toggle_symbols')

    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, msg_text, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def password_length(message):
    global PASSWORD_LENGTH
    if message.text.isdigit() == True:
        pass_length = int(message.text)
        if pass_length < 4 or pass_length > 32:
            bot.send_message(message.chat.id, 'Извините, но данная длина не подходит. Выберите значение от 4 до 32 символов.')
        else:
            PASSWORD_LENGTH = pass_length
            menu(message)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, введите число заново.')

@bot.callback_query_handler(func=lambda call: True)
def generator_settings(call):
    global PASSWORD_LOWERCASE_ALLOWED
    global PASSWORD_UPPERCASE_ALLOWED
    global PASSWORD_DIGITS_ALLOWED
    global PASSWORD_SYMBOLS_ALLOWED
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'generate_password':
        if not correctSettings():
            bot.send_message(call.message.chat.id, 'Ошибка! Вам нужно включить хотя бы 1 пункт из меню, чтобы сгенерировать пароль!')
        else:
            password = generate_password()
            bot.send_message(call.message.chat.id, f'Вот ваш пароль:\n{password}')
    elif call.data == 'edit_password_length':
        bot.send_message(call.message.chat.id, 'Выберите длину пароля (допустимые значения от 4 до 32).')
    elif call.data == 'toggle_lowercase':
        PASSWORD_LOWERCASE_ALLOWED = not PASSWORD_LOWERCASE_ALLOWED
        menu(call.message)
    elif call.data == 'toggle_uppercase':
        PASSWORD_UPPERCASE_ALLOWED = not PASSWORD_UPPERCASE_ALLOWED
        menu(call.message)
    elif call.data == 'toggle_digits':
        PASSWORD_DIGITS_ALLOWED = not PASSWORD_DIGITS_ALLOWED
        menu(call.message)
    elif call.data == 'toggle_symbols':
        PASSWORD_SYMBOLS_ALLOWED = not PASSWORD_SYMBOLS_ALLOWED
        menu(call.message)

bot.polling(none_stop=True)