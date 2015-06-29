import zerorpc
import requests
from bs4 import BeautifulSoup

class Climber():
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        paragraphs = soup.find_all('p')

        return [p.get_text() for p in paragraphs]    


s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
