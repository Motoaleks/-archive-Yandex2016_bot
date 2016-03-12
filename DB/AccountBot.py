from enum import Enum

class TypeOfAccount(Enum):
    STRELKA = 0
    TROYKA = 1
    PHONE = 2
    KILLFISH = 777

# All fields are str, except 'account_ID' � 'TYPE'
class Account:
    chat_ID = "" # user id
    account_ID = -1 # unique ID, may be used for deleting
    NAME = ""
    TYPE = -1
    NUMBER = ""

    # Constructor for user
    def __init__(self, chat_id, account_id):
        self.chat_ID = chat_id
        self.account_ID = int(account_id)

    # Constructor for BD
    def __init__(self, account_id, number, type, chat_id, name):
        self.account_ID = int(account_id)
        self.NUMBER = number
        self.chat_ID = chat_id
        self.TYPE = int(type)
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

        if (self.TYPE == TypeOfAccount.STRELKA and valid_num != 10):
            raise Exception("Invalid number")
        
        if ((self.TYPE == TypeOfAccount.TROYKA or self.TYPE == TypeOfAccount.PHONE) and valid_num != 10):
            raise Exception("Invalid number")

        self.NUMBER = valid_num

    # Can we add object to DB
    def isValid(self):
        return len(self.NAME) > 0 and len(self.NUMBER) > 0 and self.TYPE > 0

    def toString(self):
        print("Account_ID", self.account_ID, "Chat_ID", self.chat_ID, "Number", self.NUMBER, "Type", self.TYPE, "Name", self.NAME)