from StateHandlers.StateHandler import StateHandler
from DB.DataBase import DataBase


class DeleteAccStateHandler(StateHandler):
    def __init__(self):
        self.id = StateHandler.State.delete_acc
        self.state_menu = ["Назад"]

    def EnterState(self, ui, stateHandlers):
        ui.user_state = self.id
        db = DataBase()
        cards = db.getAccounts(ui.chat_id)  # дичь какая-то
        if len(cards) == 0:
            ui.sender.sendMessage("У Вас еще нет счетов")
            stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers)
            return
        kb = []
        self.cards = {}
        strip = []
        i=0
        for i in range(len(cards)):
            strip.append(cards[i].NAME)
            self.cards.update({cards[i].NAME: cards[i]})
            if i % 2 == 1:
                kb.append(strip)
                strip = []
        if i%2==0:
            kb.append(strip)
        kb.append(self.state_menu)
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Выберите счёт", reply_markup=show_keyboard)

    def EvaluateState(self, ui, msg, stateHandlers):
        # print(msg['text'])
        if msg['text'] == self.state_menu[0]:
            stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers)
        elif self.cards.__contains__(msg['text']):
            #stateHandlers[StateHandler.State.balance_show].EnterState(ui, stateHandlers, self.cards[msg['text']])
            db = DataBase()
            db.removeAccount(self.cards[msg['text']].account_ID)
            stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers)
        else:
            ui.sender.sendMessage("Неверное имя счёта")
            stateHandlers[StateHandler.State.choose_acc].EnterState(ui, stateHandlers)