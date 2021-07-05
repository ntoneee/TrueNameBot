from os import getenv
from asyncio import sleep
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

bot = Bot(getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def handle_start(message: types.Message):
    await message.reply('👋')
    await sleep(0.2)
    await message.reply(
        'Hello! Forward me one\'s message and I\'ll send you back his name!\n'
        'Привет! Перешли мне сообщения и я верну имя автора!'
    )


@dp.message_handler(lambda message: message.is_forward()
                    and message.chat.type == types.ChatType.PRIVATE,
                    content_types=types.ContentTypes.ANY)
async def handle_forwards(message: types.Message):
    if message.forward_from_chat:
        name = message.forward_from_chat.title
    elif message.forward_from:
        name = message.forward_from.full_name
    else:
        name = message.forward_sender_name
    await message.reply(name)


if __name__ == '__main__':
    executor.start_polling(dp)
