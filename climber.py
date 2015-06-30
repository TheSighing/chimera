import zerorpc
import requests
import json
from bs4 import BeautifulSoup

class Bubble():
    def __init__(self, context, sub_context, text):
        self.context =  context
        self.sub_context = sub_context
        self.text = text

class Climber():
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        r = requests.get(url)
        soup = BeautifulSoup(r.text)

        paragraphs = [ p.get_text() for p in soup.find_all('p') ]
        contexts = soup.find_all('h2#mw-headline')
        sub_contexts = soup.find_all('h3#mw-headline')

        wiki = []

        for s in sub_contexts:
            print(s.previous_sibling)
            bubble = Bubble(c, s)
            wiki.append(bubble)

        return wiki

    def climb_images():
        images = soup.find_all('img')
        #wiki['related'] = links

        return "images"

    def climb_links():
        links = [ a.get('href') for a in soup.select('div#mw-content-text a') ]

        return links

s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
