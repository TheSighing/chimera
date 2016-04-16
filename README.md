# Climber "Why Crawl when you can Climb?"
Climb wiki pages with this web crawler turned API or use it as Restful-API.
Uses Zmq to pipe the parsing of a wiki page from Python into chunks of data fed back to Node.js to be utilized as an (API).

Gathers context and text and stores these in relation to each other with level identifiers.

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
