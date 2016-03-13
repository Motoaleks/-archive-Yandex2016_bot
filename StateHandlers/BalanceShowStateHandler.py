from DB.DataBase import DataBase
from StateHandlers.StateHandler import StateHandler
from yandexAPI import get_auth_url


class BalanceStateHandler(StateHandler):
    def __init__(self):
        self.id = StateHandler.State.balance_show
        self.state_menu = ["Пополнить", "Назад"]

    def EnterState(self, ui, stateHandlers, account):
        self.account = account
        ui.user_state = self.id
        kb = [[self.state_menu[0]],[self.state_menu[1]]]
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Текущий баланс: " + account.getBalance(), reply_markup = show_keyboard)

    def EvaluateState(self, ui, msg, stateHandlers):
        if msg['text'] == self.state_menu[0]:
            stateHandlers[StateHandler.State.inpute_sum].EnterState(ui, stateHandlers, self.account)
        elif msg['text'] == self.state_menu[1]:
            stateHandlers[StateHandler.State.choose_acc].EnterState(ui, stateHandlers)
        else:
            ui.sender.sendMessage("Неверная команда")
            stateHandlers[StateHandler.State.balance_show].EnterState(ui, stateHandlers, self.acccount)
