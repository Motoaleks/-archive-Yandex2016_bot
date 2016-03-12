class User:
    obj = None
    chat_id = None
    token = None
    def __init__(self, chat_id = None, token = None):
        odj = self
        self.chat_id = chat_id
        self.token = token
