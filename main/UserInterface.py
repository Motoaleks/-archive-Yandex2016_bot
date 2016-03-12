# coding=UTF-8
import telepot

class UserInterface(telepot.helper.UserHandler):
    
    def __init__(self, seed_tuple, timeout):
        super(UserInterface, self).__init__(seed_tuple, timeout)
        self.user_state='undefined'
    def on_message(self, msg):
        flavor = telepot.flavor(msg)
        content_type, chat_type, chat_id = telepot.glance(msg)

    def on_close(self,e):
        hide_keyboard = {'hide_keyboard': True}
        self.sender.sendMessage("Возвращайся... ;-)", reply_markup=hide_keyboard)
        super(UserInterface, self).on_close(e)
