from StateHandlers.StateHandler import StateHandler
from yandexAPI import get_auth_url


class AddAccStateHandler(StateHandler):
    def __init__(self):
        id = StateHandler.State.add_acc
        state_menu = ["Мобильный телефон", "Карта 'Стрелка'", "Карта 'Тройка'", "Назад"]

    def EnterState(self, ui, stateHandlers):
        ui.user_state = self.id
        kb = [[self.state_menu[0]], [self.state_menu[1]], [self.state_menu[2]], [self.state_menu[3]]]
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Выберите тип счета.", reply_markup=show_keyboard)

    def EvaluateState(self, ui, msg, stateHandlers):
        import telepot
        from DB.AccountBot import Account, TypeOfAccount
        ui.content_type, ui.chat_type, ui.chat_id = telepot.glance(msg)
        type = -1
        if msg['text'] == self.state_menu[0]:  # "Мобильный телефон"
            type = TypeOfAccount.PHONE
        elif msg['text'] == self.state_menu[1]:  # "Карта 'Стрелка'"
            type = TypeOfAccount.STRELKA
        elif msg['text'] == self.state_menu[2]:  # "Карта 'Тройка'"
            type = TypeOfAccount.TROYKA
        elif msg['text'] == self.state_menu[3]:  # "Назад"
            stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers)
            return
        else:
            stateHandlers[StateHandler.State.add_acc].EnterState(ui, stateHandlers)
            return
        ac = Account(ui.chat_id, "", type)
        stateHandlers[StateHandler.State.add_name].EnterState(ui, stateHandlers, ac)
