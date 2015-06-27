import zerorpc
import requests
from bs4 import BeautifulSoup

class Climber(object):
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        r = requests.get(url)
        return BeautifulSoup(r.text).find_all('p')

s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
