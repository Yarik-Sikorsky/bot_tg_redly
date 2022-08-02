
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default import kb_test
from keyboards.inline import ikb_menu, ikb_menu2
from loader import dp

@dp.message_handler(text='інлайн-меню')
async def show_inlain_menu(message: types.Message):
    await message.answer('Інлайн меню нижче', reply_markup=ikb_menu)


@dp.callback_query_handler(text='Повідомлення')
async def sen_massage(call: CallbackQuery):
    await call.message.answer('Кнопки замінені', reply_markup=kb_test)


@dp.callback_query_handler(text='alert')
async def sen_massage(call: CallbackQuery):
    await call.answer('Кнопки замінені', show_alert=True)


@dp.callback_query_handler(text='Кнопки2')
async def sen_massage(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)