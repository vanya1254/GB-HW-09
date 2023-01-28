from aiogram import executor
from handlers import dp


async def on_start(_):
    print('Bot activated')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)