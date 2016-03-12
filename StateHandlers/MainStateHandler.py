from StateHandlers.StateHandler import StateHandler
class MainStateHandler(StateHandler):
    def __init__(self):
        self.id=1
        self.state_menu=["Проверить и пополнить баланс","Добавить счёт"]
    def EnterState(self, ui, stateHandlers):
        ui.user_state=self.id
        kb = [self.state_menu]
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Help text",reply_markup=show_keyboard)
    def EvaluateState(self, ui, msg, stateHandlers):
        if msg['text']==self.state_menu[0]:#"Проверить и пополнить баланс"
            stateHandlers[StateHandler.State.choose_acc].EnterState(ui)
        elif msg['text']==self.state_menu[1]:#"Добавить счёт"
            pass
        else:
            self.EnterState(ui)