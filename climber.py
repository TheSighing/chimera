import zerorpc
import requests
import json
from bs4 import BeautifulSoup

class Bolt():
    def __init__(self, text):
        self.contexts =  {}
        self.text = text

    def belay(self, context, level=None):
        assert type(context) is StringType, "Not a string => no rope to belay."
        if(not level):
            self.contexts.push(context)
        else:
            self.contexts[str(level)] = context

    def __str__(self):
        return self.text

class Climber():
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        content = requests.get(url)
        soup = BeautifulSoup(content.text)

        wiki = []

        #re.compile => a way to check for a specific string match

        #TODO: You are creating context, subcontext, text, links => Beta() object and loading into an Array
        #      building structure to the wiki itself (or any large text based information page) that can be accessed
        #      parsed and such.
        bolt = Bolt()
        for section_title in soup.find_all(["h1", "h2", "h3", "h4", "p"]):
            try:
                if(section_title.name  == "h1"):
                    bolt.belay(section_title.get_text(), 1)
                elif(section_title.name  == "h2"):
                    bolt.belay(section_title.get_text(), 2)
                elif(section_title.name  == "h3"):
                    bolt.belay(section_title.get_text(), 3)
                elif(section_title.name  == "h4"):
                    bolt.belay(section_title.get_text(), 4)
                else:
                    # Add text to the bolt.
                    wiki.push(bolt)
                    bolt = Bolt()
                    continue
                pass
            except Exception as e:
                continue

        return "Array of Beta."

    #def see_also() => makes a whole set of related thhings to the topic chosen
    def climb_images():
        images = soup.find_all('img')
        #wiki['related'] = links

        return "images"

    def climb_links(): #this should build based on a depth choice and and builds graph of links to help determine later searches
        links = [ a.get('href') for a in soup.select('div#mw-content-text a') ]

        return "links"

s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
