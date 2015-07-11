
//TODO: Make this a library of functions with same functionality
//TODO: have this node js file open anc close the server to python script then communicate to it
//      as its worker process throuugh zeromq and still work as an API that can be accessed via npm and have the alt be a restful API later
//      this file should parse the results of pythons venture and then return it in a nice usable format 
var zerorpc = require("zerorpc"),
express = require('express'),
climber = express(),
bodyParser = require('body-parser'),
async = require('async'),
events = require('events');

var PORT = 8080;
var ZMQ_PORT = 5050;

var e = new events.EventEmitter();
var client = new zerorpc.Client();
client.connect('tcp://127.0.0.1:' + ZMQ_PORT);

//Preparing to derive data from POST
climber.use(bodyParser.urlencoded({extended: true}));
climber.use(bodyParser.json());

//The routes for API.
var router = express.Router();

// Main request for content.
router.get('/climb/:topic', function(req, res){
  client.invoke("climb", req.params.topic, function(err, content, more){
    if(!more){
      console.log("Done.");
    }
    else{
      console.log(content);
      res.send(content);
    }
  });
});

//Prefixing all the routes in the api
climber.use('/api', router);

//Starting Server
climber.listen(PORT);
console.log('Base of the cliff is at port ', PORT);

exports = module.exports = climber;
