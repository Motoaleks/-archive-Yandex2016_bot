from StateHandlers.StateHandler import StateHandler
from yandexAPI import get_auth_url
from DB.AccountBot import Account, TypeOfAccount
from DB.DataBase import DataBase

class AddNameStateHandler(StateHandler):
    def __init__(self):
        self.id = StateHandler.State.add_name
        self.state_menu = ["Назад"]

    def EnterState(self, ui, stateHandlers, ac):
        self.account = ac
        ui.user_state = self.id
        kb = [[self.state_menu[0]]]
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Введите имя.", reply_markup=show_keyboard)

    def EvaluateState(self, ui, msg, stateHandlers):
        import telepot
        ui.content_type, ui.chat_type, ui.chat_id = telepot.glance(msg)
        if msg['text'] == self.state_menu[0]:  # "Назад"
            stateHandlers[StateHandler.State.add_acc].EnterState(ui, stateHandlers)
            return
        else:  # Ввели имя с клавиатуры
            try:
                self.account.setName(msg['text'], 15)
            except:
                ui.sender.sendMessage("Введено слишком длинное имя. Ограничьтесь 15 символами)")
                stateHandlers[StateHandler.State.add_acc].EnterState(ui, stateHandlers)
                return
            db = DataBase()
            if(db.isAccountNameExists(ui.chat_id, msg['text'])):
                ui.sender.sendMessage("Имя уже существует")
                self.EnterState(ui, stateHandlers, self.account)
            else:
                stateHandlers[StateHandler.State.add_numb].EnterState(ui, stateHandlers, self.account)
