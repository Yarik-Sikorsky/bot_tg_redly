from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from keyboards.default import kb_menu
from loader import dp

from states import register

@dp.message_handler(IsPrivate(), Command('register'))
async def register_(messag: types.Message):
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

    kb_name = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f'{messag.from_user.full_name}')
            ],
        ],
        resize_keyboard=True
    )

    await messag.answer('Привіт, ти почав реєстрацію, \nВведи своє імя', reply_markup= kb_name)
    await register.test1.set()


@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer(f'{answer} Скільки вам років?')
    await register.test2.set()


@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await state.get_data()
    name = data.get('test1')
    years = data.get('test2')
    await  message.answer(f'Реєстрація завершена\n'
                          f'Твоє імя {name}\n'
                          f'Тобі {years} років', reply_markup=kb_menu)
    await state.finish()