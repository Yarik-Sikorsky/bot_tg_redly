from aiogram.types import ContentType, Message, InputFile, MediaGroup

from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id

    photo_file_id = 'AgACAgIAAxkBAAIE8mLm4kZ6v6l1DC_a8eC5yVcBayrDAALJvjEbi644S9rviNov_AAB6AEAAwIAA20AAykE'
    photo_url = 'asa'
    photo_bytes = InputFile(path_or_bytesio='media/photo1.jpg')

    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes)
    #await dp.bot.send_video(chat_id=chat_id,video='BAACAgIAAxkBAAIE-2Lm44kinJDq1t6DpnJ_IrrGSZU5AAIfGwACi644S64t6UykQT8xKQQ')


@dp.message_handler(text='/album')
async def send_albom(message: Message):
    album = MediaGroup()
    photo_file_id = 'AgACAgIAAxkBAAIE8mLm4kZ6v6l1DC_a8eC5yVcBayrDAALJvjEbi644S9rviNov_AAB6AEAAwIAA20AAykE'
    photo_bytes = InputFile(path_or_bytesio='media/photo2.png')
    vodeo_file_id = 'BAACAgIAAxkBAAIE-2Lm44kinJDq1t6DpnJ_IrrGSZU5AAIfGwACi644S64t6UykQT8xKQQ'

    album.attach_photo(photo=photo_file_id)
    album.attach_video(video=vodeo_file_id)
    album.attach_photo(photo=photo_bytes, caption='текст22')

    await message.answer_media_group(media=album)