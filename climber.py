import zerorpc
import requests
import json
import msgpack
import gevent
from bs4 import BeautifulSoup

#TODO: List
# Parse and clean the text to remove the reference numbers
# get images from wiki and apply context to them
# def see_also() => makes a whole set of related thhings to the topic chosen
# def chossy() => parse disambiguation pages can be called when the page reached durign climb or
# any given method in the class and it hits a "chossy page" one that cannot be parsed in this custiomary
# method ie a disambiguation page or otherwise
# def flash() => grab directly a section of the overall page when supplied a set of context levels and/or
# a bit of text that it can match
# climb links should build based on a depth choice and and builds graph of links to help determine later searches
# add comments to this 

#TODO: Notes
# proven method to send object to the otherside
# wiki_parsed.append({ "Text" :  bolt.text , "Contexts: " : bolt.contexts })
# re.compile => a way to check for a specific string match


def encode(obj):
    return { "Text" : obj.text, "Contexts" : obj.contexts }

class Bolt():
    def __init__(self, text):
        self.contexts =  {}
        self.text = text

    def belay(self, context, level=None):
        if(not level):
            self.contexts = {}
            self.contexts["1"] = context
        else:
            self.contexts[str(level)] = context

    def __str__(self):
        temp = "Text: " + self.text
        temp += "\nContext:"
        for key in self.contexts:
            temp += "\nlvl" + key + ": " + self.contexts[key]

        return temp

class Climber(object):
    #@zerorpc.stream
    def climb(self, topic):
        self.topic = topic;

        self.url = 'http://en.wikipedia.org/?title=%s' % self.topic
        self.content = requests.get(self.url)
        self.soup = BeautifulSoup(self.content.text)

        wiki_parsed = []


        #TODO:
        # You are creating context, subcontext, text, links => Beta() object and loading into an Array
        # building structure to the wiki itself (or any large text based information page) that can be accessed
        # parsed and such.
        # later should incorporate other checks to find titles and context
        # this doesnt quite work how i want it to need it to have parent contexts saved
        # so that only the changing level changes but the other context remain thre same for each new bolt added on
        # a new bolt is constituted by the fact that one of the context level has chaged
        # proboably should make this become hadled by the class Bolt or something
        # Should also work with any amount of headers (headers define amounts of context)
        h = ["", "", "", ""]
        for section in self.soup.find_all(["h1", "h2", "h3", "h4", "p"]):
            try:
                if(section.name  == "h1"):
                    h[0] = section.get_text()
                elif(section.name  == "h2"):
                    h[1] = section.get_text()
                elif(section.name  == "h3"):
                    h[2] = section.get_text()
                elif(section.name  == "h4"):
                    h[3] = section.get_text()
                elif(section.name == "p"):
                    # Add text to the bolt.
                    bolt = Bolt(section.get_text())
                    bolt.belay(h[0], 1)
                    bolt.belay(h[1], 2)
                    bolt.belay(h[2], 3)
                    bolt.belay(h[3], 4)
                    wiki_parsed.append(encode(bolt))
                else:
                    continue
                pass
            except Exception as e:
                continue

        return json.dumps(wiki_parsed, indent=4)


    def climb_images(self):
        images = self.soup.find_all('img')
        print images

        return "images"

    def climb_links(self):
        links = [ a.get('href') for a in self.soup.select('div#mw-content-text a') ]

        return json.dumps(links, indent=4)

s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
