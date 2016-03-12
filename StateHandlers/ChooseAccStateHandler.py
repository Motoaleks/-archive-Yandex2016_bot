from StateHandlers.StateHandler import StateHandler
from DB.DataBase import DataBase
class ChooseAccStateHandler(StateHandler):
    def __init__(self):
        self.id=2
        self.state_menu=["Назад"]
    def EnterState(self, ui, stateHandlers):
        ui.user_state=self.id
        db = DataBase()
        cards=db.getAccounts(ui.chat_id)#дичь какая-то
        if len(cards) == 0:
            ui.sender.sendMessage("У Вас еще нет счетов")
            stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers)
            return
        kb=[]
        ui.cards={}
        strip=[]
        for i in range( len(cards)):
            strip.append(cards[i].tostring())
            ui.cards.update((cards[i].tostring(),cards[i]))
            if i%2==1:
                kb.append[strip]
                strip=[]
        kb.append(self.state_menu)
        show_keyboard = {'keyboard': kb}
        ui.sender.sendMessage("Выберите счёт",reply_markup=show_keyboard)
        ui.user_state=id
    def EvaluateState(self, ui, msg, stateHandlers):
        if msg['text']==self.state_menu[0]:#"Проверить и пополнить баланс"
            self.action_on_check(msg)
        elif msg['text']==self.state_menu[1]:#"Добавить счёт"
            pass
        else:
            self.action_on_help()