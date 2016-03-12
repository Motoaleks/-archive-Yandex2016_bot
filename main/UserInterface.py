# coding=UTF-8
from enum import Enum

import telepot

import StateHandlers


class State(Enum):
    start=0
    main=1
    choose_acc=2
    balance_show=3
    inpute_sum=4
    add_acc=5
    add_name=6
    add_numb=7
class UserInterface(telepot.helper.UserHandler):
    '''
    states_menus={}
    states_menus.update((State.main,["Проверить и пополнить баланс","Добавить счёт"]))
    states_menus.update((State.choose_acc,["Назад"]))
    states_menus.update((State.balance_show,["Пополнить","Назад"]))
    states_menus.update((State.inpute_sum,[]))
    states_menus.update((State.add_acc,["Мобильный","Тройка","Стрелка"]))
    states_menus.update((State.add_name,[]))
    states_menus.update((State.add_numb,[]))
    '''
    def __init__(self, seed_tuple, timeout):
        super(UserInterface, self).__init__(seed_tuple, timeout)
        self.user_state=StateHandlers.StateHandler.State.start
        self.cards={}
        self.stateHandlers = {StateHandlers.StateHandler.State.start : StateHandlers.StartStateHandler(),
                 StateHandlers.StateHandler.State.main : StateHandlers.MainStateHandler(),
                 StateHandlers.StateHandler.State.choose_acc : StateHandlers.ChooseAccStateHandler(),
                              StateHandlers.StateHandler.State.balance_show : StateHandlers.BalanceStateHandler(),
                              StateHandlers.StateHandler.State.inpute_sum : StateHandlers.InputSumStateHandler(),
                              StateHandlers.StateHandler.State.add_acc : StateHandlers.AddAccStateHandler(),
                              StateHandlers.StateHandler.State.add_name : StateHandlers.AddNameStateHandler(),
                              StateHandlers.StateHandler.State.add_numb : StateHandlers.AddNameStateHandler()
                              }
    def on_message(self, msg):
        flavor = telepot.flavor(msg)
        if flavor == 'normal':
            content_type, chat_type, chat_id = telepot.glance(msg)
            if chat_type=='private':
                if content_type=='text':
                    if( msg['text']=='/help' and not self.user_state ==StateHandlers.StateHandler.State.main):
                        self.stateHandlers[StateHandlers.StateHandler.State.main].EnterState(self, self.stateHandlers)
                    else:
                        self.stateHandlers[self.user_state].EvaluateState(self, msg, self.stateHandlers)
    def action_on_start(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        from yandexAPI import get_auth_url
        self.sender.sendMessage("Привет! Я ticket-buy bot! Я помогу быстро и удобно проверить и пополнить баланс карт Тройка и Стрелка или счёт телефона. Перейди по ссылке и разреши нам доступ)\n"+get_auth_url(chat_id))

    def action_on_help(self):
        self.user_state=State.main
        kb = UserInterface.states_menus[self.user_state]
        show_keyboard = {'keyboard': kb}
        self.sender.sendMessage("Help text",reply_markup=show_keyboard)

    def action_on_check(self,msg):
        self.user_state=State.choose_acc
        cards=get_cards()
        if len(cards==0):
            kb=[UserInterface.states_menus[self.user_state]]
            show_keyboard = {'keyboard': kb}
            self.sender.sendMessage("У Вас еще нет счетов",reply_markup=show_keyboard)
            return
        kb=[]
        self.cards={}
        strip=[]
        for i in range( len(cards)):
            strip.append(cards[i].tostring())
            self.cards.update((cards[i].tostring(),cards[i]))
            if i%2==1:
                kb.append[strip]
                strip=[]
        kb.append(UserInterface.states_menus[self.user_state])
        show_keyboard = {'keyboard': kb}
        self.sender.sendMessage("Выберите счёт",reply_markup=show_keyboard)
        self.user_state=State.choose_acc
    def on_close(self,e):
        hide_keyboard = {'hide_keyboard': True}
        self.sender.sendMessage("Возвращайся... ;-)", reply_markup=hide_keyboard)
        super(UserInterface, self).on_close(e)
