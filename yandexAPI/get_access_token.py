from yandex_money.api import Wallet, ExternalPayment
from DB.DataBase import DataBase
client_id = 'BF2F8E11F0A8D2EB36CDA4171598908EEBE08ED0659E6E50766521D5C429BD77'
redirect_uri = 'http://tchat.noip.me/endpoint'
forward_uri = 'http://tchat.noip.me/redirect'
client_secret = '40349DB56E4FB3AC4AD9634F6937B248C95C264A36C060D0FA91EBDB902F96867E8BC2ADA8A29546F7AEB59E8741ED2B5F691D210D4FF6B0A35A691AF79AE3B3'

scope = ['account-info', 'operation-history', "payment.to-pattern(\"10449\")", "payment.to-pattern(\"20651\")",  "payment.to-pattern(\"phone-topup\")"]  #Здесь список разрешений, которые ты просишь у аккаунта
'''
auth_url = Wallet.build_obtain_token_url(client_id, redirect_uri, scope)
print('Вставь следующий url в браузер, пройди требуемые процедуры и потом скопируй часть нового urla после code= и введи в программу\n')
print(auth_url)

code = input()

access_token = Wallet.get_access_token(client_id, code, redirect_uri, client_secret)  # change to client_secret=None
print('Это access_token. Сохрани вторую часть в фигурных скобках себе отдельно. Пригодится, чтобы не получать каждый раз заново.\n')
print(access_token)
print("\n")
with open('token.txt','w') as tokenfile:
    tokenfile.write(access_token['access_token'])
'''

def get_auth_url(id):
    return Wallet.build_obtain_token_url(client_id, redirect_uri+"?id="+id, scope) + "&response_type=code"

def set_token(code,chat_id, db):
    access_token = Wallet.get_access_token(client_id, code, redirect_uri + "?id=" + str(chat_id), client_secret)  # change to client_secret=None
    if('error' in access_token):
        return False
    db.setToken(str(chat_id), str(access_token['access_token']))
    return True