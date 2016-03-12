from yandex_money.api import Wallet, ExternalPayment
#print("Введи здесь access_token, полученный в предыдущей проге.\n")
'''
with open('token.txt','r') as tokenfile:

    access_token=tokenfile.readline()
api=Wallet(access_token)
account_info = api.account_info()
balance = account_info['balance']  # and so on
print(balance)
request_options = {
    "pattern_id": "p2p",
    "to": "410013999801357",
    "amount_due": "0.02",
    "comment": "test payment comment from yandex-money-python",
    "message": "test payment message from yandex-money-python",
    "label": "testPayment",
    "test_payment": True,
    "test_result": "success"
};
request_result = api.request_payment(request_options)
print(request_result)

process_options={
    'request_id':request_result['request_id'],
    'money_source':'wallet',
    'test_payment':True,
    "test_result": "success"

};
process_result=api.process_payment(process_options)
print(process_result)
'''
def do_test_payment(access_token,to,sum):
    api=Wallet(access_token)
    request_options = {
    "pattern_id": "p2p",
    "to": to,
    "amount_due": sum,
    "comment": "test payment comment from yandex-money-python",
    "message": "test payment message from yandex-money-python",
    "label": "testPayment",
    "test_payment": True,
    "test_result": "success"
    };
    request_result = api.request_payment(request_options)
    print(request_result)

    process_options={
        'request_id':request_result['request_id'],
        'money_source':'wallet',
        'test_payment':True,
        "test_result": "success"

    };
    process_result=api.process_payment(process_options)

    if process_result['status'] == "success":
        return True
    else:
        return False
