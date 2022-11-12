import tocen
import logging

from aiogram import Dispatcher, Bot, executor, types
from aiogram.types.message import ContentType

logging.basicConfig(level=logging.INFO)
bot = Bot(token=tocen.tok_test)
dp = Dispatcher(bot)
PRICES = types.LabeledPrice(label="Пожертва храму", amount=10 * 100)  # копейки (грн)

#start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    sto = open('C:\\Users\\FUJITSU\\Pictures\\аниме\\nnn\\новый храм\\фото.png', 'rb')  # Вступительное фото
    await bot.send_photo(message.chat.id, sto)
    clav = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tp1 = types.KeyboardButton("Помолица🙏")
    tp2 = types.KeyboardButton("Пожертвовать богине 💸")
    clav.add(tp1, tp2)
    await bot.send_message(message.chat.id,
                           "Добро пожаловать прихожанин,\n Я - <b>храм присвятой Викторий</b>, бот храм созданный для того, чтобы служить нашей богини Викторий .",
                           parse_mode='html', reply_markup=clav)


@dp.message_handler(content_types=['text'])
async def lop(message):
    cop_1 = open('C:\\Users\\FUJITSU\\Pictures\\аниме\\nnn\\новый храм\\икона1.png', 'rb')  # Фото иконы №1
    cop_2 = open('C:\\Users\\FUJITSU\\Pictures\\аниме\\nnn\\новый храм\\икона2.png', 'rb')  # Фото иконы №2
    cop_3 = open('C:\\Users\\FUJITSU\\Pictures\\аниме\\nnn\\новый храм\\stickes.webp', 'rb')  # Стикер пожертвувание
    if message.chat.type == 'private':
        if message.text == 'Помолица🙏':
            kls = types.InlineKeyboardMarkup(row_width=1)  # клавиатура номер два

            await bot.send_photo(message.chat.id, cop_1)  # Иконы для молитвы
            await bot.send_photo(message.chat.id, cop_2)  # вторая икона для молитвы

            itm = types.InlineKeyboardButton("Отпустить грех ", callback_data='good')  # Значение клавиатура номер два

            kls.add(itm)  # Клавиатура номер два
            await bot.send_message(message.chat.id, str("Царица моя Преблагая, Надежда моя, Богородица,\n"
                                                        "Приют сирот и странников Защитница, скорбящих Радость,\n"
                                                        "Обиженных Покровительница!\n"
                                                        "Видишь мою беду, видишь мою скорбь;\n"
                                                        "Помоги мне, как немощному, направь меня, как странника.\n"
                                                        "Обиду мою знаешь: разреши ее по Своей воле."),
                                   reply_markup=kls)  # Ответ на кнопку помалица Молитва
        elif message.text == 'Пожертвовать богине 💸':  # Пожертвувание
            await bot.send_sticker(message.chat.id, cop_3)  # Стикер пожертв
            # Оплата
            await bot.send_invoice(message.chat.id,
                                   title="Пожертва",
                                   description="Пожертвуй богини 🙏\n"
                                               "И она спустит на тебя удачу😇\n"
                                               "И отпустит сразу все грехи😇",
                                   provider_token=tocen.tok_col,  # Токен кошелька
                                   currency='UAH',
                                   photo_url="file:///C:/Users/FUJITSU/Pictures/%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5/nnn/%D0%B8%D0%BA%D0%BE%D0%BD%D0%B01.png",
                                   photo_size=416,
                                   photo_width=416,
                                   photo_height=216,
                                   is_flexible=False,
                                   prices=[PRICES],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload")


# Молитва
@dp.callback_query_handler(lambda query: True)
async def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                await bot.send_message(call.message.chat.id, 'Грех отпущен')  # после нажатия текст
                await bot.edit_message_text(chat_id=call.message.chat.id,
                                            message_id=call.message.message_id,
                                            text="Молитва окончена",
                                            reply_markup=None)  # замена кнопки инлайтовой клавиатуры
                await bot.answer_callback_query(callback_query_id=call.id,
                                                show_alert=False,
                                                text="Грех отпущен !!!!")  # Оповищение


    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
