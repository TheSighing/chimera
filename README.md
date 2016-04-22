# Climber - "Why crawl when you can climb?!"
Climb wiki pages with this web crawler turned API or use it as Restful-API, information returned as JSON.
Uses ZMQ to pipe the parsing of a wiki page from Python into chunks of data fed back to Node.js to be utilized as an API in your application or communicate to an evolving Restful-API implementation at https://chimeraapi.herokuapp.com/.

Gathers context and text and stores these in relation to each other with level identifiers.

##Coming Soon
Implementation of Automatic Summary attached to the returned JSON.

##Install

```javascript
$ npm install zerorpc

$ npm install climber

```

##Basic API Usage
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

##Restful-API Usage
```javascript

https://chimeraapi.herokuapp.com/wolf

https://chimeraapi.herokuapp.com/images/wolf

https://chimeraapi.herokuapp.com/links/wolf

```

### TODO

- [ ] Implement climb of images and links on both RESTFUL-API and API
- [ ] Implement options to include link and images result in standard climb
- [ ] Clean up code
- [ ] Improve result set accuracy to ensure handling of various types of wiki pages and to handle disambiguation pages by returning useful information for the developer using the API as to how to construct a follow up query to the API.
- [x] Standard climb
- [ ] Report errors properly and helpfully on both RESTFUL-API and API
- [ ] Improve documentation
- [ ] Implement Naive Summary and add to resulting JSON returned for given page sections
