import asyncio

from data import config
from utils.db_api import quck_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
#   await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'Vlad', 'net')
    await commands.add_user(143243, 'Vlad', 'Zikk')
    await commands.add_user(5, 'Vlad', '111')
    await commands.add_user(7878776, 'Vlad', '123')
    await commands.add_user(888, 'Vlad', 'ert')


    users = await commands.select_all_users()
    print(len(users))

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(888, 'ne_Vlad2')

    user = await commands.select_user(1)
    print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())

