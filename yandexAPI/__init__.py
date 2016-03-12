from yandexAPI.get_access_token import redirect_uri
#from check_balance_using_access_token import do_test_payment

def get_auth_url(id):
    return redirect_uri + "?id=" + str(id)

def pay_phone(token, phone, sum):
    pass
def pay_troyka(token, num, sum):
    pass
def pay_strelka(tokem, num, sum):
    pass
