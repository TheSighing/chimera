__version__ = '0.1.4'

import requests
import re
import json
from bs4 import BeautifulSoup

# TODO: def see_also() => makes a whole set of related thhings to the topic
# chosen
# TODO:
#   def chossy() => parse disambiguation pages can be called
#   when the page reached durign climb or
#   any given method in the class and it hits a "chossy page"
#   one that cannot be parsed in this custiomary
#   method ie a disambiguation page or otherwise
# TODO:
#   def flash() => grab directly a section of the overall page when supplied
#   a set of context levels and/or a bit of text that it can match
#   climb links should build based on a depth choice and and builds graph of
#   links to help determine later searches
# TODO: add comments to this
# TODO: bolts should also allow for optional images.
# TODO:
#   climb should have options (object) passed in to allow it to include images
#   in route or to include graph of links with given
#   level of depth
# TODO:
#   You are creating context and subcontexts, text, links => Bolt() object
#   and loading into an Array building structure to the wiki itself
#   (or any large text based information page) that can be accessed
#   parsed as such. Later should incorporate other checks to find titles and
#   context that are more universal.
# TODO:
#   Should also work with any amount of headers
#   fix the h1 - ?? checks so they are extensible rather than hard coded
#   this so it matches the h# set up and loops to
#   decide on depth or just inputs the number found
#   as the hash for the entry (headers define amounts of context)
# TODO: create overall function that sanitizes the strings for printing them
#       "pretty"
# TODO: Replace complex words with definitions you find in the underlying link
#       or using dictionary.
# TODO: Build some test harnesses for API and Restful-API.
# TODO: Return related topics and souroundign topics using wikis dropdowns,
#       as part of climb or as separate API function.


def check_text(text):
    if(text != "Contents" and text != ""):
        return text


def chossy():
    return {"error": "This is a Disambiguation Page...\n\n"}


class Bolt():
    def __init__(self, text):
        self.contexts = {}
        self.text = text
        self.images = None

    # Add context to bolt.
    def belay(self, context, level=None):
        if(not level):
            self.contexts = {}
            self.contexts["one"] = context
        else:
            self.contexts[level] = context

    # Encodes bolt for json formatting.
    def encode(self):
        return {"text": self.text, "contexts": self.contexts}

    def __str__(self):
        temp = "Text: " + self.text
        temp += "\nContext:"
        for key in self.contexts:
            temp += "\nlvl" + key + ": " + self.contexts[key]

        return temp


class Climber():
    # Constructs route of entire wiki page based on topic chosen.
    def __init__(self, options=None):
        self.options = {} if not options else options


    def climb(self, topic):
        self.depth = self.options["depth"] if "depth" in self.options.keys() else None
        self.summary = self.options["summary"] if "summary" in self.options.keys() else None
        if(topic is None):
            return None
        else:
            url = 'http://en.wikipedia.org/?title=%s' % topic
            content = requests.get(url)
            self.soup = BeautifulSoup(content.text, "html.parser")

            check = self.soup.find_all(id="disambigbox")

            return self.get_scaffold(check)


    # Extracts images given a topic.
    def climb_images(self, topic=None):
        images = []

        if(topic is None):
            check = self.soup.find_all(id="disambigbox")

            for image in self.soup.findAll("img"):
                images.append("https://" + image["src"])
        else:
            url = 'http://en.wikipedia.org/?title=%s' % topic
            content = requests.get(url)
            self.soup = BeautifulSoup(content.text, "html.parser")

            check = self.soup.find_all(id="disambigbox")

            if(check):
                for image in self.soup.findAll("img"):
                    images.append("https://" + image["src"])
            else:
                return chossy()

        return json.dumps(images)


    def get_scaffold(self, check):
        # TODO: WIll cause a toggle based on passed type in which case the
        # include summary scaffold will be used but no matter what the depth
        # will be passed to scaffold defaulting to 0
        if(not len(check)):
            images_list = None
            wiki_parsed = self.scaffold_basic(self.summary, self.depth)

            if("images" in self.options.keys()):
                images_list = self.climb_images()

            if(images_list is None):
                return json.dumps({"data": wiki_parsed})
            else:
                return json.dumps({"data": wiki_parsed,
                                   "images": images_list})
        else:
            # TODO: WIll return all the other options to search from
            #       disambiguation page
            return chossy()


    def scaffold_basic(self, summary, depth):

        selected = []
        h = ["", "", "", ""]

        for section in self.soup.find_all(["h1", "h2", "h3", "h4", "p"]):
            try:
                if(section.name == "h1"):
                    text = section.get_text()
                    if(check_text(text)):
                        h[0] = text
                elif(section.name == "h2"):
                    text = section.get_text()
                    if(check_text(text)):
                        h[1] = text
                        h[2] = ""
                        h[3] = ""
                elif(section.name == "h3"):
                    text = section.get_text()
                    if(check_text(text)):
                        h[2] = text
                        h[3] = ""
                elif(section.name == "h4"):
                    text = section.get_text()
                    if(check_text(text)):
                        h[3] = text
                elif(section.name == "p"):
                    # Add text to the bolt.
                    string = section.get_text()
                    if(string != ""):
                        string = re.sub(r"\[\d+\]", "", string)
                        bolt = Bolt(string)
                        bolt.belay(h[0], "one")
                        bolt.belay(h[1], "two")
                        bolt.belay(h[2], "three")
                        bolt.belay(h[3], "four")
                        selected.append(bolt.encode())
                else:
                    continue
                pass
            except Exception as e:
                print e
                continue

        return selected

    # Builds map of links with given search depth option as parameter.
    # def climb_links(self, topic, options):
    #     if(not len(check)):
    #         link_query = 'div#mw-content-text a'
    #         links = [a.get('href') for a in self.soup.select(link_query)]

    #         return json.dumps(links)
    #     else:
    #         return chossy()
