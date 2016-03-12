"""
URL redirection example.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import time
import sys
from get_access_token import get_auth_url, set_token
from botwrapper import  bot

HOST_NAME = '' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8080 # Maybe set this to 9000.
LAST_RESORT = "http://google.com/"

class RedirectHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(302)
        ps = parse_qs(self.path[10:])
        self.send_header("Location", get_auth_url(ps['id'][0]))
        self.end_headers()
    def do_GET(self):
        if(self.path[:9] == '/redirect'):
            self.do_HEAD()
        elif(self.path[:9] == '/endpoint'):
            print(self.path)
            ps = parse_qs(self.path[10:])
            #bot.sendMessage(148567946, ps['code'][0])
            set_token(ps['code'][0], ps['id'][0])
            bot.sendMessage(ps['id'][0], 'Thanks. Now we can continue with sending money. Send me /give and follow instrucitions.')
            #self.do_HEAD()
            self.send_response(200)
            self.end_headers()

httpd = HTTPServer((HOST_NAME, PORT_NUMBER), RedirectHandler)
print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
httpd.serve_forever()
httpd.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
#initBot()