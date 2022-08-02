from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустити бота'),
        types.BotCommand('help', 'Допомога'),
        types.BotCommand('menu', 'Меню'),
        types.BotCommand('profile', 'Отимати дані з БД'),
        types.BotCommand('register', 'Реєстрація'),
        types.BotCommand('photo', 'Фото'),
        types.BotCommand('album', 'Альбом')
    ])