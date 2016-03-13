# coding=UTF-8
import sys
import telepot
from telepot.delegate import per_from_id, create_open
from main.UserInterface import UserInterface

TOKEN = sys.argv[1]
bot = telepot.DelegatorBot(TOKEN, [(per_from_id(),
                                    create_open(UserInterface,
                                                timeout=3600)), ])
#bot.sendMessage(54016973, 'Bileter bot started')
print('Listening ...')
bot.notifyOnMessage(run_forever=True)

