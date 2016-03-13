from StateHandlers.StateHandler import StateHandler
from yandexAPI import get_auth_url


class InputSumStateHandler(StateHandler):
    def __init__(self):
        self.id = StateHandler.State.balance_show
        self.state_menu = ["Назад"]

    def EnterState(self, ui, stateHandlers, account):
        self.account = account
        ui.user_state = self.id
        kb = [self.state_menu[0]]
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Введите сумму пополнения", reply_markup=show_keyboard)

    def EvaluateState(self, ui, msg, stateHandlers):
        if msg['text'] == self.state_menu[0]:
            stateHandlers[StateHandler.State.balance_show].EnterState(ui, stateHandlers, self.account)
        elif msg['text'].isdigit():
            # todo: fuck Magic, do Yandex Money here
            # stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers)
            pass
        else:
            ui.sender.sendMessage("Неверная команда")
            stateHandlers[StateHandler.State.inpute_sum].EnterState(ui, stateHandlers, self.acccount)
