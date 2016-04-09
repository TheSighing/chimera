# Climber "Why Crawl when you can Climb?"
Climb wiki pages with this web crawler turned API or use it as Restful-API.
Uses Zmq, Python, Node.js to pipe the parsing of a wiki page into "Bolts" (Python) to Node.js (API)

Gathers context and text and stores these in relation to each other with level identifiers.

Web Crawler as Restful-API Service (Coming SOON as easy to use option and extension to package but for now)

# Clone repo and use Web Crawler as API Service
```javascript
$ node wiki-climber.js
```
#Install

```javascript
$ npm install zerorpc

$ npm install climber

```
# Note installing climber starts the python services script in a background.

#Basic Usage
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
