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
        content = requests.get(url)
        soup = BeautifulSoup(content.text)

        paragraphs = [ p.get_text() for p in soup.find_all('p') ]
        main_contexts = [ h2.get_text() for h2 in soup.find_all('h2') if(h2.get_text().lower() != 'contents') ]
        contexts = [ c.get_text() for c in soup.find_all('span', { "class" : "mw-headline" }) ]

        wiki = []

        for s in sub_contexts:
            if(s in main_contexts):
                c = s;
            else:
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
