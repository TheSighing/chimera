# Climber "Why Crawl when you can Climb?"
Climb wiki pages with this web crawler turned API or use it as Restful-API.
Uses Zmq, Python, Node.js to pipe the parsing of a wiki page into "Bolts" (Python) to Node.js (API)

Why crawl when you can climb?

Gathers context and text and stores these in relation to each other with level identifiers.

#TODO:

***Replace complex words with definitions you find in the underlying link or using dictionary.

***Add option to allow for summary of returned data.

Need to make a way to install using npm, update the capabilities of the "climber" to gather more info from wiki.

***Get images from wiki and apply context to them.

def see_also() => makes a whole set of related thhings to the topic chosen.

***def chossy() => parse disambiguation pages can be called when the page reached during climb or
any given method in the class and it hits a "chossy page" one that cannot be parsed in this customary
method ie a disambiguation page or otherwise.

?? def flash() => directly grab a section of the overall page when supplied a set of context levels and/or
a bit of text that it can match. ??

Climb links should build based on a depth choice and and builds graph of "links" to help determine later searches.

***Add comments to this code and organize code (avoid spagetti).

***Also improve documentation and explain the API usage.

Build some test harnesses for API.

Web Crawler as Restful Service
#Install

npm install zerorpc
npm install climber


```javascript
var c = require('climber');
climber = new c(5050);

climber.climb('wolf', function(err, data){
  console.log(data);
});

climber.climb_images(function(err, data){
  console.log(data);
});

climber.climb_links(function(err, data){
  console.log(data);
});
```
