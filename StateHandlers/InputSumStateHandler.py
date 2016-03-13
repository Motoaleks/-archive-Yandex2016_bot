from StateHandlers.StateHandler import StateHandler
from yandexAPI import get_auth_url
import yandexAPI
from DB.AccountBot import TypeOfAccount
from DB.DataBase import DataBase

class InputSumStateHandler(StateHandler):
    def __init__(self):
        self.id = StateHandler.State.inpute_sum
        self.state_menu = ["Назад"]

    def EnterState(self, ui, stateHandlers, account):
        self.account = account
        ui.user_state = self.id
        kb = [self.state_menu]
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Введите сумму пополнения", reply_markup=show_keyboard)

    def EvaluateState(self, ui, msg, stateHandlers):
        if msg['text'] == self.state_menu[0]:
            stateHandlers[StateHandler.State.balance_show].EnterState(ui, stateHandlers, self.account)
        elif msg['text'].isdigit():
            db = DataBase()
            token = db.getToken(ui.chat_id)
            # todo: fuck Magic, do Yandex Money here
            result = False
            try:
                if(self.account.TYPE == TypeOfAccount.PHONE):
                    result = yandexAPI.pay_phone(token, self.account.NUMBER, msg['text'])
                elif(self.account.TYPE == TypeOfAccount.TROYKA):
                    result = yandexAPI.pay_troyka(token, self.account.NUMBER, msg['text'])
                elif(self.account.TYPE == TypeOfAccount.STRELKA):
                    result = yandexAPI.pay_strelka(token, self.account.NUMBER, msg['text'])
            except:
                ui.sender.sendMessage("Пополнить баланс не удалось.");
            if(result):
                ui.sender.sendMessage("Пополнение успешно.");
            stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers)
        else:
            ui.sender.sendMessage("Неверная команда")
            stateHandlers[StateHandler.State.inpute_sum].EnterState(ui, stateHandlers, self.acccount)
