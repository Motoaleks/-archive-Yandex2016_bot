from enum import Enum

class TypeOfAccount(Enum):
    STRELKA = 0
    TROYKA = 1
    PHONE = 2
    KILLFISH = 777

# ВСЕ ПОЛЯ ТИПА STRING, КРОМЕ 'account_ID' и 'TYPE'
class Account:
    chat_ID = "" # юзер, которому принадлежит счет
    account_ID = -1 # уникальное ID для счета, используем для удаления
    NAME = ""
    TYPE = -1
    NUMBER = ""

    # Конструктор для Андрея : по мере инициализации полей
    def __init__(self, chat_id, account_id):
        self.chat_ID = chat_id
        self.account_ID = account_id

    # Конструктор для Насти: для загрузки из БД
    def __init__(self, account_id, number, type, chat_id, name):
        self.account_ID = int(account_id)
        self.NUMBER = number
        self.chat_ID = chat_id
        self.TYPE = int(type)
        self.NAME = name


    # Установка имени
    def setName(self, name_str, limit):
        
        if len(name_str) > limit:
            raise Exception("Limit is exceed")

    # Установка типа счёта
    def setType(self, type_of_account):
        valid_type = int(type_of_account)
        if (type_of_account > 3 or type_of_account < 0):
            raise Exception("Invalid type of account")
        TYPE = valid_type

    # Установка номера (карты или телефона)
    def setNumber(self, number):
        if(self.TYPE < 0 or self.TYPE > 2):
            raise Exception("Invalid type of account")

        valid_num = int(number)

        if (self.TYPE == TypeOfAccount.STRELKA and valid_num != 10):
            raise Exception("Invalid number")
        
        if ((self.TYPE == TypeOfAccount.TROYKA or self.TYPE == TypeOfAccount.PHONE) and valid_num != 10):
            raise Exception("Invalid number")

        self.NUMBER = valid_num

    # Можно ли добавлять объект в БД
    def isValid(self):
        return len(name) > 0 and len(number) > 0 and TYPE > 0