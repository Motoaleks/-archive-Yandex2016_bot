from StateHandlers.StateHandler import StateHandler
from yandexAPI import get_auth_url
class StartStateHandler(StateHandler):
    def __init__(self):
        id=StateHandler.State.start
        state_menu=[]
    def EnterState(self, ui, stateHandlers):
        pass
    def EvaluateState(self, ui, msg, stateHandlers):
        import telepot
        ui.content_type, ui.chat_type, ui.chat_id = telepot.glance(msg)
        from DB.DataBase import DataBase
        db = DataBase()
        if(db.checkID(ui.chat_id)):
            ui.sender.sendMessage("Привет! Я ticket-buy bot! Я помогу быстро и удобно проверить и пополнить баланс карт Тройка и Стрелка или счёт телефона. Перейди по ссылке и разреши нам доступ)\n"+get_auth_url(ui.chat_id))
        else:
             stateHandlers[StateHandler.State.main].EnterState(ui, stateHandlers)