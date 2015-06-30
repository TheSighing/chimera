import zerorpc
import requests
import json
from bs4 import BeautifulSoup

class Climber():
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        r = requests.get(url)
        soup = BeautifulSoup(r.text)

        paragraphs = [ p.get_text() for p in soup.find_all('p') ]
        links = [ a.get('href') for a in soup.select('div#mw-content-text a') ]
        images = soup.find_all('img')
        
        wiki = {}
        wiki['topic'] = paragraphs
        wiki['related'] = links

        return wiki


s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
