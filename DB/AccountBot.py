from enum import Enum
from Parsing import SteelCard

balance_for_troyka = " На любой из станций метро найдите желтый круг и приложите к нему свою карту. В апреле, возможно будет вам баланс."
balance_for_phone = "Билайн - *102#.\nМегафон и МТС - *100#\n.Tele2 - *105#."


class TypeOfAccount(Enum):
    STRELKA = 0     # 11 symbols
    TROYKA = 1      # 10 symbols
    PHONE = 2       # 11 symbols
    KILLFISH = 777

# All fields are str, except 'account_ID' � 'TYPE'
class Account:
    chat_ID = "" # user id
    account_ID = -1 # unique ID, may be used for deleting
    NAME = ""
    TYPE = -1
    NUMBER = ""

    # Constructor
    def __init__(self, chat_id, account_id, type, name = "",  number = ""):
        self.account_ID = int(account_id)
        self.NUMBER = number
        self.chat_ID = chat_id
        self.TYPE = type
        self.NAME = name

    # set name
    def setName(self, name_str, limit):

        if len(name_str) > limit:
            raise Exception("Limit is exceed")

    # set type account
    def setType(self, type_of_account):
        valid_type = int(type_of_account)
        if (type_of_account > 3 or type_of_account < 0):
            raise Exception("Invalid type of account")
        TYPE = valid_type

    # set number
    def setNumber(self, number):
        if(self.TYPE < 0 or self.TYPE > 2):
            raise Exception("Invalid type of account")

        valid_num = int(number)

        if ((self.TYPE == 0 or self.TYPE == 2) and len(number) != 11):#Strelka or telephone
            raise Exception("Invalid number")

        if ((self.TYPE == 1 ) and len(number) != 10):#Troika
            raise Exception("Invalid number")

        self.NUMBER = valid_num

    # Sasha, poprav' method!
    def getBalance(self):
        if(self.TYPE < 0 or self.TYPE > 2):
            raise Exception("Invalid type of account")
        if (self.TYPE == 1):
            return balance_for_troyka
        if (self.TYPE == 2):
            return balance_for_phone

        return SteelCard.get_balance(self.NUMBER)

    # Can we add object to DB
    def isValid(self):
        return len(self.NAME) > 0 and len(self.NUMBER) > 0 and self.TYPE > 0