from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.shemas.user import User


async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str):           #Добавлення користувачча в БД
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status )
        await user.create()
    except UniqueViolationError:
        print('Користувач не добавлений')


async def select_all_users():           #Отримати користувачів з БД
    users = await User.query.gino.all()
    return users


async def count_users():            #Отримати кількість записів у БД табл користувач
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):            #Знайти конкретного юзера
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def update_status(user_id, status):          #змінює юзера
    user = await select_user(user_id)
    await user.update(status=status).apply()


