from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Повідомлення', callback_data='Повідомлення'),
                                        InlineKeyboardButton(text='Ccилка', callback_data='https://pythonworld.ru/'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='alert', callback_data='alert')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Замінити кнопки меню', callback_data='Кнопки2')
                                    ]
                                ])
