class User:
    # Singletone
    obj = None
    id = -1
    phone = None
    email = None
    token = None
    state = 0
    args = {}
    def __init__(self, id = -1, phone = None, email = None, token = None, state = 0, args = {}):
        odj = self
        self.id = id
        self.phone = phone
        self.email = email
        self.token = token
        self.state = state
        self.args = args
