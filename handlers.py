from create import dp
from aiogram import types
from random import randint


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'\n\n{message.from_user.first_name}, добро пожаловать в игру с конфетами!\n\n\
    Правила игры:\n\n \
    На столе лежит заданное количество конфет.\n \
    Играют два игрока делая ход друг после друга.\n \
    Первый ход за пользователем.\n \
    За один ход можно забрать не более чем 28 конфет.\n \
    Все конфеты достаются сделавшему последний ход.\n\n \
    Для перезапуска игры снова пропишите /set и количество конфет!\n\n \
    /help - покажет все команды бота')


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Команды для игры:\n\n \
    /start - покажет правила игры\n \
    /set 100 - установит количество конфет равное 100')


@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    amount = int(message.text.split()[1])
    total = amount
    if amount >= 100:
        await message.answer(f'Количество конфет = {amount}')
    else:
        await message.answer('Можно задать число конфет только от 100')


@dp.message_handler()
async def mes_settings(message: types.Message):
    global total
    
    if message.text.isdigit():
        user_step = int(message.text.strip())
        
        if 0 < user_step <= 28 and total >= user_step:
            
            total -= user_step
            await message.answer(f'Ход игрока {message.from_user.first_name} => {user_step}')
            
            if total == 0:
                await message.answer(f'Поздравляем, {message.from_user.first_name}, ты забираешь все конфеты!')
            else:
                await message.answer(f'Количество конфет = {total}')
                bot_step = int(total % 29)
                
                if bot_step == 0:
                    bot_step += randint(1, 28)
            
                await message.answer(f'Ход БОТа - ИВАНа => {bot_step}')
                total -= bot_step    

                await message.answer(f'Количество конфет = {total}')
                if total == 0:
                    await message.answer('Сожалеем, но бот вас переиграл!')
                    
        else:
            await message.answer(f'Можно брать от 1 до 28 конфет за раз и не больше {total}')