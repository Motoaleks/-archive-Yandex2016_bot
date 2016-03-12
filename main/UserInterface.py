# coding=UTF-8
import telepot

'''
Заглушка для получения состояния пользователя
'''
def get_user_state(chat_id):
    return "default"
'''
Заглушка для "показать рекомендации"
'''
def get_recomendations():

    return []

'''
Заглушка для получения списка категорий
'''
def get_categories():
    return ['Sample category','Sample category2']


class UserInterface(telepot.helper.UserHandler):
    main_menu_list=('Показать рекомендации', 'Хочу дёшево', 'Рядом со мной', 'Скоро', 'По категориям')
    def __init__(self, seed_tuple, timeout):
        super(UserInterface, self).__init__(seed_tuple, timeout)
        self.user_state='undefined'
    def on_message(self, msg):
        flavor = telepot.flavor(msg)
        content_type, chat_type, chat_id = telepot.glance(msg)
        # self.sender.sendMessage("Hello")
        if content_type!='text':
            self.sender.sendMessage("I'll remember that. Send /help to get commands list.")
            return
        if (self.user_state=='undefined'):
            self.user_state=get_user_state(chat_id)
        if (chat_type != 'private'):
            return
        if (self.user_state=='default'):
            if msg['text'] == '/start' or msg['text'] == '/start@ticket_buy_bot':
                self.action_on_start(msg)
            if msg['text'] == '/help' or msg['text'] == '/help@ticket_buy_bot':
                self.action_on_help(msg)
        elif (self.user_state=='first' and msg['text'] in UserInterface.main_menu_list):
            if msg['text']==UserInterface.main_menu_list[4]: #'По категориям'
                kb =[]
                for cat in get_categories():
                    kb.append([cat])
                show_keyboard = {'keyboard': kb}
                self.sender.sendMessage("Теперь выбери категорию.",reply_markup=show_keyboard)
                self.user_state='choose_category'
            else:
                hide_keyboard = {'hide_keyboard': True}
                message=msg['text']
                self.sender.sendMessage(message, reply_markup=hide_keyboard)
        

    def action_on_start(self, msg):
        self.sender.sendMessage(
            "Привет! Я ticket-buy bot! Я помогу быстро и удобно купить билет на интересующее тебя мероприятие. Жми /help чтобы узнать подробности.")

    def action_on_help(self, msg):
        kb = [[UserInterface.main_menu_list[0]],[UserInterface.main_menu_list[1],UserInterface.main_menu_list[2]],[UserInterface.main_menu_list[3],UserInterface.main_menu_list[4]]]
        show_keyboard = {'keyboard': kb}
        self.sender.sendMessage(
            "Билетер (ticket_buy_bot) - это бот для Telegram, который выдаёт информацию о лучших мероприятиях в ближайшее время и помогает купить билет. Чтобы ты не пропустил долгожданное событие, наш бот обязательно напомнит о нем. \n\n"
            + "Нажми на кнопку – получишь результат))",
            reply_markup=show_keyboard)
        self.user_state='first'


    def on_close(self,e):
        hide_keyboard = {'hide_keyboard': True}
        self.sender.sendMessage("Возвращайся за новой движухой ;-)", reply_markup=hide_keyboard)
        super(UserInterface, self).on_close(e)