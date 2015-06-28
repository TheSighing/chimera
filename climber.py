import zerorpc
import requests
from bs4 import BeautifulSoup

class Climber():
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        p = soup.find_all('p')[0].get_text()

        return p

s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
