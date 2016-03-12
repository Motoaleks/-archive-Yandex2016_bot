__author__ = 'Kirill'



from ponominalu import httpRquest

def get_events(category):

    res = httpRquest.url_request("get_events?category=" + category + "?session=123")

    print(res(1))


get_events('Концерты')