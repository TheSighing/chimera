import zerorpc
import requests
import re
import json
from bs4 import BeautifulSoup

#TODO: def climb_images() => gathers images from wiki and applies context to them
#TODO: def see_also() => makes a whole set of related thhings to the topic chosen
#TODO:
#   def chossy() => parse disambiguation pages can be called
#   when the page reached durign climb or
#   any given method in the class and it hits a "chossy page"
#   one that cannot be parsed in this custiomary
#   method ie a disambiguation page or otherwise
#TODO:
#   def flash() => grab directly a section of the overall page when supplied
#   a set of context levels and/or a bit of text that it can match
#   climb links should build based on a depth choice and and builds graph of links
#   to help determine later searches
#TODO: add comments to this
#TODO: bolts should also allow for optional images.
#TODO:
#   climb should have options (object) passed in to allow it to include images
#   in route or to include graph of links with given
#   level of depth
#TODO:
#   You are creating context and subcontexts, text, links => Bolt() object
#   and loading into an Array building structure to the wiki itself
#   (or any large text based information page) that can be accessed
#   parsed as such. Later should incorporate other checks to find titles and context that are more universal.
#TODO:
#   Should also work with any amount of headers
#   fix the h1 - ?? checks so they are extensible rather than hard coded
#   this so it matches the h# set up and loops to
#   decide on depth or just inputs the number found
#   as the hash for the entry (headers define amounts of context)
#TODO: create overall function that sanitizes the strings for printing them "pretty"
#TODO: Replace complex words with definitions you find in the underlying link or using dictionary.
#TODO: Build some test harnesses for API and Restful-API.
#TODO: Return related topics and souroundign topics using wikis dropdowns, as part of climb or as separate API function.

def chossy():
        print "This is a Disambiguation Page...\n\n"

class Bolt():
    def __init__(self, text):
        self.contexts =  {}
        self.text = text

    # Add context to bolt.
    def belay(self, context, level=None):
        if(not level):
            self.contexts = {}
            self.contexts["1"] = context
        else:
            self.contexts[str(level)] = context

    # Encodes the bolt for safe transfer through zerorpc pipeline.
    def encode(self):
        return { "Text" : self.text, "Contexts" : self.contexts }

    def __str__(self):
        temp = "Text: " + self.text
        temp += "\nContext:"
        for key in self.contexts:
            temp += "\nlvl" + key + ": " + self.contexts[key]

        return temp

class Climber(object):
    # Constructs route of entire wiki page based on text.
    #@zerorpc.stream
    def climb(self, topic, options=None):
        self.topic = topic;

        self.url = 'http://en.wikipedia.org/?title=%s' % self.topic
        self.content = requests.get(self.url)
        self.soup = BeautifulSoup(self.content.text)

        wiki_parsed = []

        check = self.soup.find_all(id="disambigbox")

        if(not len(check)):

            h = ["", "", "", ""]
            for section in self.soup.find_all(["h1", "h2", "h3", "h4", "p"]):
                try:
                    if(section.name  == "h1"):
                        text = section.get_text()
                        if(text != "Contents" and text != ""):
                            h[0] = text
                    elif(section.name  == "h2"):
                        text = section.get_text()
                        if(text != "Contents" and text != ""):
                            h[1] = text
                            h[2] = ""
                            h[3] = ""
                    elif(section.name  == "h3"):
                        text = section.get_text()
                        if(text != "Contents" and text != ""):
                            h[2] = text
                            h[3] = ""
                    elif(section.name  == "h4"):
                        text = section.get_text()
                        if(text != "Contents" and text != ""):
                            h[3] = text
                    elif(section.name == "p"):
                        # Add text to the bolt.
                        string = section.get_text()
                        if(string != ""):
                            string = re.sub(r"\[\d+\]", "", string)
                            bolt = Bolt(string)
                            bolt.belay(h[0], 1)
                            bolt.belay(h[1], 2)
                            bolt.belay(h[2], 3)
                            bolt.belay(h[3], 4)
                            wiki_parsed.append(bolt.encode())
                    else:
                        continue
                    pass
                except Exception as e:
                    print e
                    continue
        else:
            chossy()

        return json.dumps(wiki_parsed, indent=4)

    # Extracts images and their context attached/explanation.
    def climb_images(self):
        images = self.soup.find_all('img')
        print images

        return "images"

    # Builds map of links with given search depth option as parameter.
    def climb_links(self):
        links = [ a.get('href') for a in self.soup.select('div#mw-content-text a') ]

        return "links"

s = zerorpc.Server(Climber())
s.bind("tcp://0.0.0.0:5050")
s.run()
