import sqlite3
from DB.User import User


class DataBase:
    conn = None  # database
    c = None  # cursor
    dbName = 'BotArmy.db'

    #constructor
    def __init__(self):
        self.conn = sqlite3.connect(self.dbName)
        self.c = self.conn.cursor()
        self.createDb()

    # Create table
    def createDb(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS BotArmy
             (id TEXT, phone TEXT, email TEXT, token TEXT, state TEXT, args TEXT)''')
        self.commit()

    # insert user
    def insertUser(self, user):
        if not self.checkID(user.id):
            raise NameError("ID already exists")
        self.c.execute("INSERT INTO BotArmy (id,phone,email,token,state,args) VALUES (?,?,?,?,?,?)",
                       (user.id, user.phone, user.email, user.token, user.state, str(user.args)))
        self.commit()

    # delete user
    def deleteUser(self, id):
        if not self.checkID(id):
            self.c.execute('DELETE FROM BotArmy WHERE id = ' + id)
        else:
            raise NameError('User not exist')

    # check if ID is not exist
    def checkID(self, id):
        if self.getUser(id) is None:
            # if user not exists
            return True
        # if user was found - problemo
        return False

    # =============SETTERS=============
    # change phone
    def updatePhone(self, id, phone):
        self.c.execute('UPDATE BotArmy SET phone  = ? WHERE id=?', (phone, id))
        self.commit()

    # change email
    def updateEmail(self, id, email):
        self.c.execute('UPDATE BotArmy SET email  = ? WHERE id=?', (email, id))
        self.commit()

    # change token
    def updateToken(self, id, token):
        self.c.execute('UPDATE BotArmy SET token  = ? WHERE id=?', (token, id))
        self.commit()

    # change state
    def updateState(self, id, state):
        self.c.execute('UPDATE BotArmy SET state  = ? WHERE id=?', (state, id))
        self.commit()

    # change Args
    def updateArgs(self, id, args):
        temp = str(args)
        self.c.execute('UPDATE BotArmy SET args  = ? WHERE id= ?', (temp, id))
        self.commit()

        # =============SETTERS END=============

    # =============GETTERS=============

    def getPhone(self, id):
        user = self.c.execute('SELECT * FROM BotArmy WHERE id = ' + id)
        return user.fetchone()[1]

    def getEmail(self, id):
        user = self.c.execute('SELECT * FROM BotArmy WHERE id = ' + id)
        return user.fetchone()[2]

    def getToken(self, id):
        user = self.c.execute('SELECT * FROM BotArmy WHERE id = ' + id)
        return user.fetchone()[3]

    def getState(self, id):
        user = self.c.execute('SELECT * FROM BotArmy WHERE id = ' + id)
        return user.fetchone()[4]

    def getUser(self, id):
        # try:
        user = self.c.execute('SELECT * FROM BotArmy WHERE id = ' + str(id))
        return user.fetchone()

    def getArgs(self, id):
        user = self.c.execute('SELECT * FROM BotArmy WHERE id = ' + id)
        temp = user.fetchone()[5]
        return eval(temp)

    # =============GETTERS END=============

    # print database
    def printAll(self):
        for row in self.c.execute('SELECT * FROM BotArmy'):
            print(row)

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
