import zerorpc
import requests
import json
from bs4 import BeautifulSoup

class Bolt():
    def __init__(self, text):
        self.contexts =  {}
        self.text = text
        self.height = 0

    def belay(self, context, level=None):
        if(not level):
            self.contexts = {}
            self.contexts["1"] = context
            self.height = 1
        else:
            try:
                location = self.contexts[str(level)]
                #Check if location has an entry before incrementing total counter for amount of context levels
                self.height += 1
                self.contexts[str(level)] = context
            except:
                self.contexts[str(level)] = context

    def __str__(self):
        temp = "Text: " + self.text
        if(self.height >= 1):
            temp += "\nContext:"
        for i in range(self.height):
            temp += "\nlvl" + str(i) + ": " + self.contexts[str(i)]

        return temp

class Climber():
    @zerorpc.stream
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        content = requests.get(url)
        soup = BeautifulSoup(content.text)

        wiki_parsed = []
        #re.compile => a way to check for a specific string match

        #TODO: You are creating context, subcontext, text, links => Beta() object and loading into an Array
        #      building structure to the wiki itself (or any large text based information page) that can be accessed
        #      parsed and such.
        for section in soup.find_all(["h1", "h2", "h3", "h4", "p"]):
            bolt = Bolt("")

            #this doesnt quite work how i want it to need it to have parent contexts saved
            #so that only the changing level changes but the other context remain thre same for each new bolt added on
            # a new bolt is constituted by the fact that one of the context level has chaged
            # proboably should make this become hadled by the class Bolt or something
            try:
                if(section.name  == "h1"):
                    bolt.belay(section.get_text(), 1)
                elif(section.name  == "h2"):
                    bolt.belay(section.get_text(), 2)
                elif(section.name  == "h3"):
                    bolt.belay(section.get_text(), 3)
                elif(section.name  == "h4"):
                    bolt.belay(section.get_text(), 4)
                else:
                    # Add text to the bolt.
                    bolt = Bolt(section.get_text())
                pass
            except Exception as e:
                continue

        b = Bolt("Test.")
        b.belay("Context 1")
        b.belay("Context 2", 2)
        b.belay("Context 2 alt", 2)
        print b.height
        wiki_parsed.append({ "Text" :  b.text , "Contexts: " : b.contexts })
        return wiki_parsed

    #def see_also() => makes a whole set of related thhings to the topic chosen
    def climb_images():
        #images = soup.find_all('img')

        return "images"

    #this should build based on a depth choice and and builds graph of links to help determine later searches
    def climb_links():
        #links = [ a.get('href') for a in soup.select('div#mw-content-text a') ]

        return "links"

s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
