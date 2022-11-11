import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5728481123:AAFfb63s1YqUrkfoaniRZgBc8v2fwAHQzoQ'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    bot_name = await bot.get_me()
    await message.reply(f'вас приветствует {bot_name.first_name}')
@dp.message_handler(commands=['help'])
async def help_p(message: types.Message):
    await message.answer('/my_info \n/download_photo\n/show_movies\n/send_my_info')
@dp.message_handler(commands=['download_photo'])
async def photo(message: types.Message):
    photos = await bot.get_user_profile_photos(message.from_user.id)
    await bot.get_file(photos['photos'][0][0]['file_id'])
    await bot.send_photo(message.chat.id, photo=photos['photos'][0][0]['file_id'])
@dp.message_handler(commands=['show_movies'])
async def movies1(message: types.Message):
    await message.answer("Список фильмов:\nАнчартед.Полторалогия\nhttps://www.ts.kg/show/uncharted\n"
                         "Бэтмен. Коллекция\nhttps://www.ts.kg/show/betmen_v_kino\nНе дыши. Дилогия\n"
                         "https://www.ts.kg/show/don_t_breathe")
@dp.message_handler(commands=['send_my_info'])
async def show_my_info(message: types.Message):
    arguments = message.text.split('\n')
    await bot.send_message(message.chat.id,
                           text=f'1. Вас зовут {arguments[1]} {arguments[2]}\n2. Вам {arguments[3]} лет\n3.'
                                f' Вы занимаетесь {arguments[4]}\n4. Список ваших любимых сериалов и фильмов:'
                                f' {arguments[5]}')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
