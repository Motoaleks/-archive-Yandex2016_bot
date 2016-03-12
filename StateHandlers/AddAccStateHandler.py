from StateHandlers.StateHandler import StateHandler
from yandexAPI import get_auth_url
class AddAccStateHandler(StateHandler):
    def __init__(self):
        id=0
        state_menu=[]
    def EnterState(self, ui, stateHandlers):
        pass
    def EvaluateState(self, ui, msg, stateHandlers):
        import telepot
        ui.content_type, ui.chat_type, ui.chat_id = telepot.glance(msg)
        ui.sender.sendMessage("Привет! Я ticket-buy bot! Я помогу быстро и удобно проверить и пополнить баланс карт Тройка и Стрелка или счёт телефона. Перейди по ссылке и разреши нам доступ)\n"+get_auth_url(ui.chat_id))
        #TODO:check token