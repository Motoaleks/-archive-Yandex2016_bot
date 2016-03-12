from urllib.request import urlopen
import json

def getJSON(url):
    response = urlopen(url)
    string = response.read().decode('utf-8')
    return json.loads(string)


# Example
# url = 'http://api.cultserv.ru/jtransport/partner/get_categories?session=123'
# js = getJSON(url)
# print(js["message"][0]["title"])




