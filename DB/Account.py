class Account:
    id = -1
    number = None
    type = None
    chat_id = None
    name = None
    def __init__(self, id = -1, number = None, type = None, chat_id = None, name = None):
        self.id = id
        self.number = number
        self.type = type
        self.chat_id = chat_id
        self.name = name

    def toString(self):
        print(self.id, self.number, self.type, self.chat_id, self.name)
