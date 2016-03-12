import sqlite3
from DB.User import User


class DataBase:
    conn = None  # database
    c = None  # cursor
    dbName = 'BotArmy.db'

    # constructor
    def __init__(self):
        self.conn = sqlite3.connect(self.dbName)
        self.c = self.conn.cursor()
        self.createDb()

    # Create table
    def createDb(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS User
             (chat_id TEXT, token TEXT)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS Numbers
             (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, type TEXT, chat_id TEXT, name TEXT)''')
        self.commit()

    # insert user
    def addNumber(self, number, type, chat_id, name):
        self.c.execute("INSERT INTO Numbers (number, type, chat_id, name) VALUES (?,?,?,?)",
                       (number, type, chat_id, name))
        self.commit()

    def getNumbers(self, chat_id):
        numbers = self.c.execute('SELECT * FROM Numbers WHERE chat_id = ' + chat_id)
        return numbers

    def getToken(self, chat_id):
        user = self.c.execute('SELECT * FROM User WHERE chat_id = ' + chat_id)
        return user.fetchone()[1]

    def setToken(self, chat_id, token):
        if not self.checkID(chat_id):
            #raise NameError("ID already exists")
            self.c.execute('UPDATE User SET token = ? WHERE chat_id = ?', (token, chat_id))
        else:
            self.c.execute("INSERT INTO User (chat_id, token) VALUES (?,?)",
                       (chat_id, token))
        self.commit()

    def checkID(self, chat_id):
        if self.getUser(chat_id) is None:
            # if user not exists
            return True
        # if user was found - problemo
        return False

    def getUser(self, chat_id):
        user = self.c.execute('SELECT * FROM User WHERE chat_id = ' + str(chat_id))
        return user.fetchone()

    def removeNumber(self, id):
        self.c.execute('DELETE FROM Numbers WHERE id = ' + id)
        self.commit()

    # destructor - close connection
    def __del__(self):
        self.conn.close()

    # commit
    def commit(self):
        self.conn.commit()

# db = DataBase()
# db.printAll()
# user = User("1123", '8-800-555-35-35', 'sashaTzar@yandex.ru', '123', '0', {'key': 'hi', 'ID': '123'})
# try:
#     db.insertUser(user)
# except:
#     print("User already exists! Test complete!")
# print('Phone:' + db.getPhone('1123'))
# print('Email:' + db.getEmail('1123'))
# print('Token:' + db.getToken('1123'))
# print('State:' + db.getState('1123'))
# print('Args:' + str(db.getArgs('1123')))
#
# db.updatePhone('1123', '8-800')
# db.updateEmail('1123', 'LOH')
# db.updateToken('1123', '666')
# db.updateState('1123', 'Complete')
# db.updateArgs('1123', {'123': 23})
#
# print('Phone:' + db.getPhone('1123'))
# print('Email:' + db.getEmail('1123'))
# print('Token:' + db.getToken('1123'))
# print('State:' + db.getState('1123'))
# print('Args:' + str(db.getArgs('1123')))
#
# db.printAll()
#
# db.deleteUser('1123')
#
# db.printAll()
