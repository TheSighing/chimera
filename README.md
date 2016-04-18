# Climber "Why Crawl when you can Climb?"
Climb wiki pages with this web crawler turned API or use it as Restful-API.
Uses ZMQ to pipe the parsing of a wiki page from Python into chunks of data fed back to Node.js to be utilized as an API in your application or communicate to an evolving Restful-API implementation at https://chimeraapi.herokuapp.com/.

Gathers context and text and stores these in relation to each other with level identifiers.

#Install

```javascript
$ npm install zerorpc

$ npm install climber

```

#Basic Usage
```javascript
var c = require('climber');
climber = new c(5050);

climber.climb('wolf', function(err, data){
  console.log(data);
});

climber.climb_images('wolf', function(err, data){
  console.log(data);
});

climber.climb_links('wolf', function(err, data){
  console.log(data);
});
```

#Restful-API Usage
```javascript

https://chimeraapi.herokuapp.com/wolf

https://chimeraapi.herokuapp.com/images/wolf

https://chimeraapi.herokuapp.com/links/wolf

```

### TODO

- [ ] Implement climb of images and links on both RESTFUL-API and API
- [ ] Implement options to include link and images result in standard climb
- [ ] Clean up code
- [x] Standard climb
- [ ] Report errors properly and helpfully on both RESTFUL-API and API
- [ ] Improve documentation
- [ ] Implement Naive Summary and add to resulting JSON returned for given page sections
