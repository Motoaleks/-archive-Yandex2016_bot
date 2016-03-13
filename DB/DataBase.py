import sqlite3

from DB.AccountBot import Account, TypeOfAccount


class DataBase:
    conn = None  # database
    c = None  # cursor
    dbName = 'BotArmy.db'

    # constructor
    def __init__(self):
        import os
        path = os.getcwd()
        self.conn = sqlite3.connect(path + "\\" + self.dbName)
        self.c = self.conn.cursor()
        self.createDb()

    # Create table
    def createDb(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS User
             (chat_id TEXT, token TEXT)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS Account
             (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, type TEXT, chat_id TEXT, name TEXT)''')
        self.commit()

    # insert new account to DB
    def addAccount(self, number, type, chat_id, name):
        self.c.execute('INSERT INTO Account (number, type, chat_id, name) VALUES (?,?,?,?)',
                       (number, type.value, chat_id, name))
        self.commit()

    #if account exists
    def isAccountNameExists(self, chat_id, name):
        if self.c.execute('SELECT * FROM Account WHERE chat_id = ' + chat_id + ' AND name = ' + name) is None:
            # if account not exists
            return False
        # if account was found
        return True

    # insert new user to DB
    def addUser(self, chat_id, token):
        self.c.execute('INSERT INTO User (chat_id, token) VALUES (?,?)',
                       (chat_id, token))
        self.commit()

    # get all accounts which have the chat_id
    def getAccounts(self, chat_id):
        numbers = self.c.execute('SELECT * FROM Account WHERE chat_id = ' + str(chat_id))
        res_numbers = list()
        for i in numbers:
            res_numbers.append(Account(i[3], i[0], i[2], i[4], i[1]))
        return res_numbers

    # return token which has a user with such chat_id
    def getToken(self, chat_id):
        user = self.c.execute('SELECT * FROM User WHERE chat_id = ' + chat_id)
        return user.fetchone()[1]

    # add new user or update the existing one
    def setToken(self, chat_id, token):
        if not self.checkID(chat_id):
            # user already exists
            self.c.execute('UPDATE User SET token = ? WHERE chat_id = ?', (token, chat_id))
        else:
            # add new user to DB
            self.c.execute('INSERT INTO User (chat_id, token) VALUES (?,?)', (chat_id, token))
        self.commit()

    # check if the user already exist
    def checkID(self, chat_id):
        if self.getUser(chat_id) is None:
            # if user not exists
            return True
        # if user was found - problemo
        return False

    # get the user via chat_id
    def getUser(self, chat_id):
        user = self.c.execute('SELECT * FROM User WHERE chat_id = ' + str(chat_id))
        return user.fetchone()

    # delete the
    def removeAccount(self, id):
        self.c.execute('DELETE FROM Account WHERE id = ' + id)
        self.commit()

    # destructor - close connection
    def __del__(self):
        self.conn.close()

    # commit
    def commit(self):
        self.conn.commit()

        # db = DataBase()
        # db.addAccount("345", "35", "49", "Zhenya")
        # db.addAccount("123", "1", "42", "Nastya")
        # db.removeAccount("1")
        # for i in db.getAccounts("49"):
        #    Account.toString(i)
        # db.addUser("56", "678")
        # db.setToken("56", "666")
        # print(db.getToken("56"))
