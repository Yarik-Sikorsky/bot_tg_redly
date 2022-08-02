# Тут імпортуємо всі хендлери для переписки з користувачами
from .bot_start import dp
#from .start import dp
from .help import dp
from .hellow import dp
from .menu import dp
from .buttons import dp
from .test import dp
from .inline_menu import dp
from .register import dp
from .media import dp



from .error import dp # Ловимо всі остальні текстові повідомлення ВІН ОСТАНІЙ


__all__ = ['dp'] # Список параметрів які можна імпортувати з папки users
