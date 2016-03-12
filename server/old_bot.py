# coding=UTF-8
import random
import sys
import time
import pprint
import  telepot
from telepot.delegate import per_chat_id, create_open
from get_access_token import get_auth_url, set_token, get_token
from check_balance_using_access_token import do_test_payment


url = "http://tchat.noip.me/redirect"

with open('log.csv', 'a') as outlog:
    def send_money(chat_id, to, sum):
        access_token = get_token(chat_id)
        return do_test_payment(access_token, to, sum)
    '''
    class YourBot(telepot.Bot):
        def on_chat_message(self, msg):
            content_type, chat_type, chat_id = telepot.glance(msg)
            print('Normal Message:', content_type, chat_type, chat_id)
            print(msg)
            outlog.write(
                str(content_type) + ';' + str(chat_type) + ';' + str(chat_id) + ';' + msg['from']['username'] + ';')
            if (content_type == 'sticker'):
                # print(msg)
                outlog.write(msg['sticker']['file_id'] + ';')
                if msg['sticker']['file_id'] == 'BQADAgADJQADzTs4A5GLGemkX28JAg':
                    print('shersh')
                    outlog.write('Sticker_Shersh')
                    bot.sendMessage(chat_id, 'Друзья, у вас осталось 5 минут!')
                elif msg['sticker']['file_id'] == 'BQADAgADIwADzTs4Ay-9E9T-I5TcAg':
                    print('ulianov')
                    outlog.write('Sticker_Ulianov')
                    bot.sendMessage(chat_id, 'Апплодисменты в Вашу корзиночку!')
                elif msg['sticker']['file_id'] == 'BQADAgADGQADzTs4A7IAAbp2k6LHlAI':
                    print('grin')
                    outlog.write('Sticker_Grin')
                    if random.randint(0, 1) == 0:
                        bot.sendMessage(chat_id, 'Он зе флай гарбач коллекшон')
                    else:
                        bot.sendMessage(chat_id, 'ТулЫ')
                elif msg['sticker']['file_id'] == 'BQADAgADGwADzTs4A58oPXNievrTAg':
                    print('boss')
                    outlog.write('Sticker_Boss')
                    bot.sendMessage(chat_id, 'алфАвит')
                # elif msg['sticker']['file_id']=='BQADAgADIwADzTs4Ay-9E9T-I5TcAg':
                #    bot.sendMessage(chat_id, 'Апплодисменты в Вашу корзиночку!')
                else:
                    print(msg)
                    outlog.write('Sticker_Other')
                    bot.sendMessage(chat_id, 'try another sticker')
            elif (content_type == 'text'):
                outlog.write(msg['text'])
                # else:
                #   outlog.write(msg)

            outlog.write('\n')
            outlog.flush()
            # need `/setinline`

        def on_inline_query(self, msg):
            print('Gbljh')
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            print('Inline Query:', query_id, from_id, query_string)
            print(msg)
            # Compose your own answers
            articles = [{'type': 'article',
                         'id': 'abc', 'title': 'ABC', 'message_text': 'Good morning'},
                        {'type': 'article',
                         'id': 'SE', 'title': 'SE', 'message_text': 'Autists'}
                        ]

            bot.answerInlineQuery(query_id, articles)

    '''



    class MessageCounter(telepot.helper.ChatHandler):
        def __init__(self, seed_tuple, timeout):
            super(MessageCounter, self).__init__(seed_tuple, timeout)
            self._count = 0
            self.flag = None
            self.to = None
            self.sum = 0

        def on_chat_message(self, msg):
            self._count += 1
            content_type, chat_type, chat_id = telepot.glance(msg)
            outlog.write(
                str(content_type) + ';' + str(chat_type) + ';' + str(chat_id) + ';' + msg['from']['username'] + ';')
            if (content_type == 'text') and msg['text'] == '/cancel' or msg['text'] == '/cancel@QpQ_bot':
                self.cancel()
            elif self.flag != None:
                self.flag(msg)
            elif (content_type == 'sticker'):
                self.sticker_handle(msg)
            elif (content_type == 'text'):
                self.text_handle(msg)
            elif (content_type == 'contact'):
                self.sender.sendMessage("I'll remember him")
                outlog.write(str(msg['contact']['phone_number']) + ';' + str(msg['contact']['user_id']))
            else:
                pass
                # self.sender.sendMessage(self._count)
            outlog.write('\n')
            outlog.flush()

        def sticker_handle(self, msg):
            content_type, chat_type, chat_id = telepot.glance(msg)
            outlog.write(msg['sticker']['file_id'] + ';')
            if msg['sticker']['file_id'] == 'BQADAgADJQADzTs4A5GLGemkX28JAg':
                print('shersh')
                outlog.write('Sticker_Shersh')
                self.sender.sendMessage('Друзья, у вас осталось 5 минут!')
            elif msg['sticker']['file_id'] == 'BQADAgADIwADzTs4Ay-9E9T-I5TcAg':
                print('ulianov')
                outlog.write('Sticker_Ulianov')
                self.sender.sendMessage('Апплодисменты в Вашу корзиночку!')
            elif msg['sticker']['file_id'] == 'BQADAgADGQADzTs4A7IAAbp2k6LHlAI':
                print('grin')
                outlog.write('Sticker_Grin')
                if random.randint(0, 1) == 0:
                    self.sender.sendMessage('Он зе флай гарбач коллекшон')
                else:
                    self.sender.sendMessage('ТулЫ')
            elif msg['sticker']['file_id'] == 'BQADAgADGwADzTs4A58oPXNievrTAg':
                print('boss')
                outlog.write('Sticker_Boss')
                self.sender.sendMessage('алфАвит')
            else:
                print(msg)
                outlog.write('Sticker_Other: ' + msg['sticker']['file_id'])
                self.sender.sendMessage('I don\' know such sticker yet')

        def text_handle(self, msg):
            content_type, chat_type, chat_id = telepot.glance(msg)
            outlog.write(msg['text'] + ';')
            com_dict = {"/help": self.my_help,
                        "/help@QpQ_bot": self.my_help,
                        "/start": self.start,
                        "/start@QpQ_bot": self.start,
                        "/give": self.give,
                        "/give@QpQ_bot": self.give
                        }
            if com_dict.get(msg['text']) != None:
                com_dict[msg['text']]()
            elif (msg['text'].find('/give') == 0):
                self.give(msg['text'].replace('/give ', ''))
            elif (msg['text'][0] == '/'):
                self.sender.sendMessage('I don\' know such command yet')

            else:
                self.my_help()

        def my_help(self):
            self.sender.sendMessage(
                "I'm a bot. I have commands. e.g. /start But I will not tell them to you) \nIf you wish, you can send me some sticker from HSE_SE pack.")

        def start(self):
            self.sender.sendMessage(
                "I'm a bot that help people to give money via Yandex Money. Go to this link, give permissions and return me the link, that tab will move to you. " + url + "?id=" + str(self.chat_id))
            #self.flag = self.set_code

        def set_code(self, msg):
            content_type, chat_type, chat_id = telepot.glance(msg)
            outlog.write(msg['text'] + ';')
            if (content_type == 'text') and (msg['text'].find('https://www.yandex.ru/?code=') == 0):
                if set_token(msg['text'].replace('https://www.yandex.ru/?code=', ''), chat_id):
                    self.sender.sendMessage(
                        'Thanks. Now we can continue with sending money. Send me /give and follow instrucitions.')

        def give(self):
            self.sender.sendMessage(
                'Pass me telephone/yandex wallet number or share contact of person who you want to give money')
            self.flag = self.give_contact

            # def give(self, msg):
            # pass

        def give_contact(self, msg):
            content_type, chat_type, chat_id = telepot.glance(msg)
            outlog.write('give_contact;')
            if (content_type == 'text'):
                outlog.write(msg['text'])
                self.to = msg['text']
            elif (content_type == 'contact'):
                outlog.write('contact ' + str(msg['contact']['phone_number']))
                self.to = msg['contact']['phone_number']
            else:
                self.sender.sendMessage('Something went wrong')
                return
            self.sender.sendMessage('Thanks. Now pass me the sum to give.')
            self.flag = self.give_sum

        def give_sum(self, msg):
            content_type, chat_type, chat_id = telepot.glance(msg)
            outlog.write('give_sum;')
            if (content_type == 'text'):
                outlog.write(msg['text'])
                try:
                    self.sum = int(msg['text'])
                except:
                    self.sender.sendMessage('Something went wrong')
                    return
                self.sender.sendMessage('We are sending ' + str(self.sum) + 'rub to ' + self.to)
                if send_money(chat_id, self.to, self.sum):
                    self.sender.sendMessage('Success')

        def cancel(self):
            self.flag = None
            self.sender.sendMessage('Operation cancelled')


    TOKEN = sys.argv[1]

    # bot = YourBot(TOKEN)
    bot = telepot.DelegatorBot(TOKEN, [(per_chat_id(),
                                        create_open(MessageCounter,
                                                    timeout=100)), ])
    bot.sendMessage(148567946, 'Bot started')
    # bot.sendMessage(-110574041, 'QpQ_bot started. Try to hack it)')
    # bot.sendMessage(-118682470, 'QpQ_bot started. Ну ты понял')
    print('Listening ...')
    bot.notifyOnMessage(run_forever=True)
    #startServer()