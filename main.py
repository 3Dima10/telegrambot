import telebot
import tocen

from telebot import types

bot = telebot.TeleBot(tocen.tok)  # токен


@bot.message_handler(commands=['start'])  # запуск бота
def start(message):
    sto = open('C:\\Users\\FUJITSU\\Pictures\\аниме\\nnn\\фото.png', 'rb')  # преветственая клавиатура
    bot.send_photo(message.chat.id, sto)
    # клавиатура
    clav = types.ReplyKeyboardMarkup(resize_keyboard=True)
    it1 = types.KeyboardButton("Помолица🙏 ")  # кнопка 1
    it2 = types.KeyboardButton("Пожертвовать богине 💸 ")  # кнопка 2

    clav.add(it1, it2)

    # Приветствие
    bot.send_message(message.chat.id,
                     "Добро пожаловать прихожанин, {0.first_name}!\n Я - <b>{1.first_name}</b>, бот храм созданный для того, чтобы служить нашей богини Марий.".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=clav)


@bot.message_handler(content_types=['text'])  # обработчик сообщений
def lop(message):
    dop = open('C:\\Users\\FUJITSU\\Pictures\\аниме\\nnn\\икона1.png', 'rb')  # Икона
    col = open('C:\\Users\\FUJITSU\\Pictures\\аниме\\nnn\\икона2.png', 'rb')  # Икона
    cod = open('C:\\Users\\FUJITSU\\Pictures\\аниме\\nnn\\stickes.webp', 'rb')  # платеж стикер
    if message.chat.type == 'private':
        if message.text == 'Помолица🙏':  # Зачения кнопки помолица

            kls = types.InlineKeyboardMarkup(row_width=1)  # клавиатура номер два
            itm = types.InlineKeyboardButton("Отпустить грех ", callback_data='good')  # Значение клавиатура номер два

            kls.add(itm)  # Клавиатура номер два

            bot.send_photo(message.chat.id, dop)  # Иконы для молитвы
            bot.send_photo(message.chat.id, col)  # Иконы для молитвы
            bot.send_message(message.chat.id, str("Царица моя Преблагая, Надежда моя, Богородица,\n"
                                                  "Приют сирот и странников Защитница, скорбящих Радость,\n"
                                                  "Обиженных Покровительница!\n"
                                                  "Видишь мою беду, видишь мою скорбь;\n"
                                                  "Помоги мне, как немощному, направь меня, как странника.\n"
                                                  "Обиду мою знаешь: разреши ее по Своей воле."),
                             reply_markup=kls)  # Ответ на кнопку помалица Молитва
        elif message.text == 'Пожертвовать богине 💸':  # Пожертвувание
            dc = types.InlineKeyboardMarkup(row_width=1)
            ito = types.InlineKeyboardButton("Пожертвовать 💳 ", callback_data='gool')
            dc.add(ito)
            bot.send_sticker(message.chat.id, cod)  # Стикер пожертв
            bot.send_message(message.chat.id, str("Пожертвуй богини 🙏\n"
                                                  "И она спустит на тебя удачу😇\n"
                                                  "И отпустит сразу все грехи😇"),
                             reply_markup=dc)  # ответ на пожертвовать
        else:
            bot.send_message(message.chat.id, "Пишы правельно еретик")  # на случай если воспользуюце не клавиатурой


@bot.callback_query_handler(func=lambda call: True)  # обработчик инлайтоввой клавитуры
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':  # Инлайтова клавиатура помолица
                bot.send_message(call.message.chat.id, 'Грех отпущен')  # после нажатия текст
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text="Молива окончена",
                                      reply_markup=None)  # замена кнопки инлайтовой клавиатуры
                bot.answer_callback_query(callback_query_id=call.id,
                                          show_alert=False,
                                          text="Грех отпущен")
            if call.data == 'gool':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="5355280002536686")
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Да неспашлет богиння на тебя удачу ")
    except Exception as e:
        print(repr(e))  # поиск ошыбок


# RUN
bot.polling(none_stop=True)
