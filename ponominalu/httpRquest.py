__author__ = 'Kirill'

import urllib.request, urllib.error




def url_request(parametrs):

    try:

        url = 'http://api.cultserv.ru/jtransport/partner/' + parametrs
        response = urllib.request.urlopen(url)
        result = response.read()
        print(result)
        return 1, result

    except urllib.error.URLError as e:
        print(e.reason)
        return 0, e.reason











