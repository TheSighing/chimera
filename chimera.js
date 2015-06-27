var zerorpc = require("zerorpc"),
express = require('express'),
wc = express(),
bodyParser = require('body-parser'),
//TODO: replace with uri-request
async = require('async'),
events = require('events');

var e = new events.EventEmitter();
var client = new zerorpc.Client();
client.connect('tcp://127.0.0.1:5050');

//Preparing to derive data from POST
wc.use(bodyParser.urlencoded({extended: true}));
wc.use(bodyParser.json());

var PORT = 8080;
var ZMQ_PORT = 5050;

//The routes for out API
var router = express.Router();

router.get('/', function(req, res){
    json = { help: "helpful message on how to use api."};
    res.json(json);
    console.log("logging the json ", json);
});

router.get('/climb/:topic', function(req, res){
  client.invoke("climb", req.params.topic, function(err, res, more){
    if(err){
        console.error(res);
    }
    else{
      if(!more){
        console.log(res);
      }
    }
  });
});

//Prefixing all the routes in the api
wc.use('/api', router);

//Starting Server
wc.listen(PORT);
console.log('Base of the cliff is at port ', PORT);

exports = module.exports = wc;
