from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
ikb_menu2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Повідомлення', callback_data='Повідомлення'),
                                        InlineKeyboardButton(text='Ccилка', callback_data='https://pythonworld.ru/'),
                                    ],
                                ])
