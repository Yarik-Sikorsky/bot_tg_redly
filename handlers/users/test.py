from aiogram import types
from loader import dp
from keyboards.default import kb_test

@dp.message_handler(text='текст1')
async def test(message: types.Message):
    await message.answer(f'Привіт {message.from_user.full_name}!\n'
                         f'Тут якийсь текст', reply_markup=kb_test)
