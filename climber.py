import zerorpc
import requests
import json
from bs4 import BeautifulSoup

class Beta():
    def __init__(self, context, text):
        self.context =  context
        self.text = text

class Climber():
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        content = requests.get(url)
        soup = BeautifulSoup(content.text)

        wiki = []

        #for section_title in soup.find_all('h2'):
        #    print(section_title)

        for section_title in soup.find_all({'span' : }):
            try:
                print p
                pass
            except Exception as e:
                continue

        return "Array of Beta."

    def climb_images():
        images = soup.find_all('img')
        #wiki['related'] = links

        return "images"

    def climb_links():
        links = [ a.get('href') for a in soup.select('div#mw-content-text a') ]

        return "links"

s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
