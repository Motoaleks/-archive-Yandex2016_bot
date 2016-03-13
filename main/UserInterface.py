# coding=UTF-8
from enum import Enum

import telepot

import StateHandlers

class UserInterface(telepot.helper.UserHandler):
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
                              StateHandlers.StateHandler.State.add_numb : StateHandlers.AddNumStateHandler()
                              }
    def on_message(self, msg):
        flavor = telepot.flavor(msg)
        if flavor == 'normal':
            content_type, chat_type, self.chat_id = telepot.glance(msg)
            if chat_type=='private':
                if content_type=='text':
                    if( msg['text']=='/help' and not (self.user_state ==StateHandlers.StateHandler.State.main or self.user_state ==StateHandlers.StateHandler.State.start)):
                        self.stateHandlers[StateHandlers.StateHandler.State.main].EnterState(self, self.stateHandlers)
                    else:
                        self.stateHandlers[self.user_state].EvaluateState(self, msg, self.stateHandlers)
    def on_close(self,e):
        hide_keyboard = {'hide_keyboard': True}
        self.sender.sendMessage("Возвращайся... ;-)", reply_markup=hide_keyboard)
        super(UserInterface, self).on_close(e)
