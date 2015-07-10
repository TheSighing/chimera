import zerorpc
import requests
import json
from bs4 import BeautifulSoup

class Bolt():
    def __init__(self, text):
        self.contexts =  {}
        self.text = text
        self.len = 0

    def belay(self, context, level=None):
        assert type(context) is StringType, "Not a string => no rope to belay."
        if(not level):
            self.contexts = {}
            self.contexts["1"] = context
            self.len = 1
        else:
            location = self.contexts[str(level)]
            print location
            #Check if location has an entry before incrementing total counter for amount of context levels
            if(not location):
                self.len += 1

            self.contexts[str(level)] = context

    def __str__(self):
        temp = "Text: " + self.text
        if(self.len >= 1):
            temp += "\nContext:"
        for i in range(self.len):
            temp += "\nlvl" + str(i) + ": " + self.contexts[str(i)]

        return temp

class Climber():
    def climb(self, topic):
        url = 'http://en.wikipedia.org/?title=%s' % topic
        content = requests.get(url)
        soup = BeautifulSoup(content.text)

        wiki = []

        b = Bolt("hey")

        print b
        wiki.append(b)

        #re.compile => a way to check for a specific string match

        #TODO: You are creating context, subcontext, text, links => Beta() object and loading into an Array
        #      building structure to the wiki itself (or any large text based information page) that can be accessed
        #      parsed and such.
        # for section in soup.find_all(["h1", "h2", "h3", "h4", "p"]):
        #     bolt = Bolt("")
        #
        #     try:
        #         if(section.name  == "h1"):
        #             bolt.belay(section.get_text(), 1)
        #         elif(section.name  == "h2"):
        #             bolt.belay(section.get_text(), 2)
        #         elif(section.name  == "h3"):
        #             bolt.belay(section.get_text(), 3)
        #         elif(section.name  == "h4"):
        #             bolt.belay(section.get_text(), 4)
        #         else:
        #             # Add text to the bolt.
        #             bolt = Bolt(section.get_text())
        #             wiki.append(bolt)
        #         pass
        #     except Exception as e:
        #         continue
        #
        # for entry in wiki:
        #     print entry
        #
        # return wiki
        return wiki

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
