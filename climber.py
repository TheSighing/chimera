import zerorpc
import requests
from bs4 import BeautifulSoup

class Climber(object):
    def climber(request):
        url = 'http://en.wikipedia.org/?title=%s' % request.topic
        r = requests.get(url)
        return BeautifulSoup(r.text)

s = zerorpc.Server(Climber)
s.bind("tcp://0.0.0.0:4242")
s.run()
