var zerorpc = require("zerorpc"),
express = require('express'),
climber = express(),
bodyParser = require('body-parser'),
async = require('async'),
events = require('events');

//Ports
var PORT = 8080;
var ZMQ_PORT = 5050;

var e = new events.EventEmitter();
var client = new zerorpc.Client();
client.connect('tcp://127.0.0.1:', ZMQ_PORT);

//Preparing to derive data from POST
climber.use(bodyParser.urlencoded({extended: true}));
climber.use(bodyParser.json());

//The routes for out API
var router = express.Router();

//Main route
router.get('/climb/:topic', function(req, res){
  console.log("Excelsior...");
  client.invoke("climb", req.params.topic, function(err, content, more){
    if(err){
      console.error(content);
    }
    else{
      res.send(content);
    }
    if (!more) {
      console.log("Done.");
    }
  });
});

//Prefixing all the routes in the api
climber.use('/api', router);

//Starting Server
climber.listen(PORT);
console.log('Base of the cliff is at port ', PORT);

exports = module.exports = climber;
