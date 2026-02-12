import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import Config, load_config
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.chat_action import ChatActionSender


config: Config = load_config()

bot = Bot(token=config.bot.token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():

    logging.basicConfig(
        level=config.log.log_level,
        format=config.log.log_format
    )

    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

HEARTS_EFFECT = "5159385139981059251"

class ValentineFSM(StatesGroup):
    question = State()

@dp.message(CommandStart())
async def valentine_suprise(message: Message, state: FSMContext):
    await message.answer(f"Привет! {message.from_user.first_name} (AKA Мехрубончик) , введи кое какое чиловое слово😏")
    await message.answer("Подсказка: это наше любимое слово. (4 буквы)")
    await state.set_state(ValentineFSM.question)

@dp.message(ValentineFSM.question)
async def congratulations(message: Message, state: FSMContext, bot: Bot):
    if message.text.lower().strip() == "хайп":
        await state.clear() 
        
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(2)
            await message.answer("Ай лев! ХАЙП присутствует!!!📈")
            
        await asyncio.sleep(2)
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(3)
            await message.answer("Раз уж сегодня 14 февраля, я решил, что обычных слов будет мало...")

        await asyncio.sleep(2)
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(3)
            await message.answer_photo(
                photo="AgACAgIAAxkBAANRaY3qD6ATnSHxYz-NaXz2W6j-trEAAoYVaxueC3FIGZFq6m1uakQBAAMCAANtAAM6BA",
                caption="Но для начала держи твой любимый мертвый кустик)))"
            )            

        await asyncio.sleep(2)
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(3)
            await message.answer_photo(
                photo="AgACAgIAAxkBAAMTaYi6mUycRB-7Y--Z4VSwYJdC6nwAAqUTaxvMA0lIaw5Omh1l2PcBAAMCAAN4AAM6BA",
                caption="С каждым днем все труднее и труднее оставаться человеком..."
            )
        
        await asyncio.sleep(2)
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(3)
            await message.answer_animation(
                animation="CgACAgIAAxkBAAMYaYi7a4b26feLg__exAw-PSep2wIAAquUAALMA0lIbOsTU2XvAAH2OgQ",
                caption="Но зачем притворятся кем то, чтобы сохранять свой рассудок, если можно быть самим собой с нужным человеком?"
            )
        
        await asyncio.sleep(2)
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(3)
            await message.answer("Мне действительно приятно проводить с тобой время, мне нравится твой юмор, твои увлечения, вкус в музыке...")


        await asyncio.sleep(2)
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(3)
            await message.answer("Для меня ты не просто подруга. Я ценю тебя больше, чем просто друга... Мне нужно признатся...")

        await asyncio.sleep(2)
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(1)
            await message.answer("Настя... Я...")


        await asyncio.sleep(2)
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(5)
            await message.answer("Головка от хуя")

            
        await asyncio.sleep(6)
        await bot.send_photo(
            chat_id=message.chat.id,
            photo="AgACAgIAAxkBAAMaaYi-e19lj2mqbrIgqi_Bob79OpEAAsoTaxvMA0lIKCScu9AqqHUBAAMCAAN5AAM6BA",
            caption="С Днем святого Валентина! ЕЕЕЕЕЕЕЕЕЕ ХАААААААААААААААЙП✌️✌️✌️✌️🤙🤙🤙🔥🔥🔥🔥🔥",
            message_effect_id=HEARTS_EFFECT
        )

        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(2)
            await message.answer("Анастасия, а ты хайповая!!! Мне нравится)))")

    else:
        await message.answer("Не-а, попробуй еще раз!")

# # Этот хендлер поймает ЛЮБУЮ гифку или фото и выдаст тебе file_id
# @dp.message(F.animation)
# async def get_animation_id(message: Message):
#     await message.answer(f"ID твоей гифки:\n<code>{message.animation.file_id}</code>", parse_mode="HTML")

# @dp.message(F.photo)
# async def get_photo_id(message: Message):
#     # У фото берем последний элемент списка (самое высокое качество)
#     await message.answer(f"ID твоего фото:\n<code>{message.photo[-1].file_id}</code>", parse_mode="HTML")


@dp.message()
async def echo(message: Message):
    await message.answer(text="Нажми на /start")




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot was stopped")


