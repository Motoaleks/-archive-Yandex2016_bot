from StateHandlers.StateHandler import StateHandler
from yandexAPI import get_auth_url
from DB.AccountBot import Account, TypeOfAccount
class AddNumStateHandler(StateHandler):
    def __init__(self):
        self.id=StateHandler.State.add_numb
        self.state_menu=["Назад"]
    def EnterState(self, ui, stateHandlers,ac):
        self.account=ac
        ui.user_state = self.id
        kb = [[self.state_menu[0]]]
        show_keyboard = {'keyboard': kb}
        shablon_dict={TypeOfAccount.PHONE:"телефона через 7 без разделителей (напр. 79123456789).",
                 TypeOfAccount.STRELKA:"карты 'Стрелка' без разделителей (напр. 01234567890).",
                 TypeOfAccount.TROYKA:"карты 'Тройка' без разделителей (напр. 0123456789)."}
        ui.sender.sendMessage("Введите номер "+shablon_dict[self.account.TYPE], reply_markup=show_keyboard)
    def EvaluateState(self, ui, msg, stateHandlers):
        import telepot
        ui.content_type, ui.chat_type, ui.chat_id = telepot.glance(msg)
        if msg['text'] == self.state_menu[0]:  # "Назад"
            stateHandlers[StateHandler.State.add_acc].EnterState(ui, stateHandlers)
            return
        else:  # Ввели номер с клавиатуры
            try:
                self.account.setNumber(msg['text'])
            except:
                ui.sender.sendMessage("Введен неправильный номер.")
                stateHandlers[StateHandler.State.add_numb].EnterState(ui, stateHandlers)
                return
            if self.account.isValid():
                pass # todo add to BD
            else:
                pass #
            stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers,self.account)
