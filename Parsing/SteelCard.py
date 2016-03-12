import requests

CARD_TYPE_ID = '3ae427a1-0f17-4524-acb1-a3f50090a8f3'
card_number = '03320103878'

def get_status(card_number):
    payload = {'cardnum': card_number, 'cardtypeid': CARD_TYPE_ID}
    r = requests.get('http://strelkacard.ru/api/cards/status/', params=payload)
    if r.status_code == requests.codes.ok:
        return r.json()
    raise ValueError("Can't get info about card with number %s" % card_number)


def get_balance(card_number):
    r = get_status(card_number)
    return r['balance'] / 100.

print(get_balance(card_number))