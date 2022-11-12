import tocen
import logging
import col
from aiogram import Dispatcher, Bot, executor, types
from aiogram.types.message import ContentType

a = col.start
b = col.bot
c = col.lop
v= col.callback_inline

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=tocen.tok)
dp = Dispatcher(bot)

# prices
PRICES = types.LabeledPrice(label="Пожертва храму", amount=10 * 100)  # копейки (грн)


# buy
@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    if tocen.tok_col2.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовое пожертвование !!!!")
    await bot.send_invoice(message.chat.id,
                           title="Пожертва",
                           description="Пожертвуй богини 🙏\n"
                                       "И она спустит на тебя удачу😇\n"
                                       "И отпустит сразу все грехи😇",
                           provider_token=tocen.tok_col2,
                           currency='UAH',
                           photo_url="file:///C:/Users/FUJITSU/Pictures/%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5/nnn/%D0%B8%D0%BA%D0%BE%D0%BD%D0%B01.png",
                           photo_size=416,
                           photo_width=416,
                           photo_height=216,
                           is_flexible=False,
                           prices=[PRICES],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


#  pre checkout  (must be answered in 10 seconds)
@dp.message_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f" {k} = {v} ")

    await bot.send_message(message.chat.id,
                           f"Пожертва на суму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошол успешно !!!!")


# Run

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
    executor.start_polling(main.bot, skip_updates=False)
