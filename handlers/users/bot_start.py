from aiogram import types
from loader import dp

from filters import IsPrivate
from utils.db_api import quck_commands as commands
from utils.misc import rate_limit


@rate_limit(limit=3,)
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привіт {user.first_name}\n'
                                 f'Ти вже зареєстований')
        elif user.status == 'ban':
            await message.answer('Ти забанений')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
        await message.answer('Ти успішно зареєстрований')


@rate_limit(limit=3,)
@dp.message_handler(IsPrivate(), text='/ban')
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='ban')
    await message.answer('Ми тебе забанили')


@rate_limit(limit=3,)
@dp.message_handler(IsPrivate(), text='/unban')
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='active')
    await message.answer('Ти більше не забанений')

@rate_limit(limit=3,)
@dp.message_handler(IsPrivate(), text='/profile')
async def get_ban(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'Айді: {user.user_id}\n'
                         f'first_name: {user.first_name}\n'
                         f'last_name: {user.last_name}\n'
                         f'username: {user.username}\n'
                         f'status: {user.status}')
