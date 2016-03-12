from yandexAPI.get_access_token import forward_uri
from yandex_money.api import Wallet
#from check_balance_using_access_token import do_test_payment

def get_auth_url(id):
    return forward_uri + "?id=" + str(id)

def pay_phone(token, phone, sum):
    api=Wallet(token)
    request_options = {
    "pattern_id": "phone-topup",
    "phone-number": phone,
    "amount": sum,
    "comment": "Payment from bot",
    "message": "Payment from bot",
    }
    request_result = api.request_payment(request_options)
    print(request_result)
    process_options={
        'request_id':request_result['request_id'],
        'money_source':'wallet'
    }
    process_result=api.process_payment(process_options)
    if process_result['status'] == "success":
        return True
    else:
        return False

def pay_troyka(token, num, sum):
    api=Wallet(token)
    request_options = {
    "pattern_id": "10449",
    "customerNumber": num,
    "amount": sum,
    "comment": "Payment from bot",
    "message": "Payment from bot",
    }
    request_result = api.request_payment(request_options)
    print(request_result)
    process_options={
        'request_id':request_result['request_id'],
        'money_source':'wallet'
    }
    process_result=api.process_payment(process_options)
    if process_result['status'] == "success":
        return True
    else:
        return False

def pay_strelka(tokem, num, sum):
    api=Wallet(token)
    request_options = {
    "pattern_id": "10449",
    "korona_transportCardId": num,
    "amount": sum,
    "comment": "Payment from bot",
    "message": "Payment from bot",
    }
    request_result = api.request_payment(request_options)
    print(request_result)
    process_options={
        'request_id':request_result['request_id'],
        'money_source':'wallet'
    }
    process_result=api.process_payment(process_options)
    if process_result['status'] == "success":
        return True
    else:
        return False
