from StateHandlers.StateHandler import StateHandler
from DB.DataBase import DataBase

class MainStateHandler(StateHandler):
    MAX_NUMBERS = 6

    def __init__(self):
        self.id = StateHandler.State.main
        self.state_menu = ["Проверить и пополнить баланс", "Добавить счёт", "Удалить счёт"]

    def EnterState(self, ui, stateHandlers):
        ui.user_state = self.id
        db = DataBase()
        num_ac = db.getNumAccounts(ui.chat_id)
        #kb = [[self.state_menu[0]], [self.state_menu[1]], [self.state_menu[2]]]
        kb = [[self.state_menu[0]]]
        if(num_ac < MainStateHandler.MAX_NUMBERS):
            kb.append([self.state_menu[1]])
        if(num_ac>0):
            kb.append([self.state_menu[2]])
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Выберете команду.", reply_markup=show_keyboard)

    def EvaluateState(self, ui, msg, stateHandlers):
        if msg['text'] == self.state_menu[0]:  # "Проверить и пополнить баланс"
            stateHandlers[StateHandler.State.choose_acc].EnterState(ui, stateHandlers)
        elif msg['text'] == self.state_menu[1]:  # "Добавить счёт"
            db = DataBase()
            if(db.getNumAccounts(ui.chat_id)==MainStateHandler.MAX_NUMBERS):
                ui.sender.sendMessage("Достигнуто максимальное количество возможных привязанных счетов.")
                self.EnterState(ui, stateHandlers)
            else:
                stateHandlers[StateHandler.State.add_acc].EnterState(ui,stateHandlers)
        elif(msg['text'] == self.state_menu[2]): # "Удалить счёт"
            db = DataBase()
            if(db.getNumAccounts(ui.chat_id)==MainStateHandler.MAX_NUMBERS):
                ui.sender.sendMessage("Не привязано ни одного счета.")
                self.EnterState(ui, stateHandlers)
            else:
                stateHandlers[StateHandler.State.delete_acc].EnterState(ui, stateHandlers)
        else:
            self.EnterState(ui, stateHandlers)
