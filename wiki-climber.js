var express = require('express'),
wc = express(),
bodyParser = require('body-parser'),
//TODO: replace with uri-request
request = require('request'),
cheerio = require('cheerio'),
async = require('async'),
events = require('events');

var e = new events.EventEmitter();

//Preparing to derive data from POST
wc.use(bodyParser.urlencoded({extended: true}));
wc.use(bodyParser.json());

var PORT = 8080;

//The routes for out API
var router = express.Router();

router.get('/', function(req, res){
    json = { help: "helpful message on how to use api."};
    res.json(json);
    console.log("logging the json ", json);
});

router.get('/climb/:topic', function(req, res){
    //TODO: Add a check to see if this is a valid title
    var url = 'http://en.wikipedia.org/?title=' + req.params.topic;
    var text = [], json = {text : ""};

    request(url, function(err, response, data){
        if(!err){
            var $ = cheerio.load(data);
            e.on('parse_complete', function(){
                res.json(json);
            });


            async.waterfall([
                function(callback){
                    //filter the results
                    //later have all of these accessible and ready to be parsed
                    $('#mw-content-text p').each(function(i, elem){
                        var p = $(this);
                        text[i] = p.text();
                    });

                    callback(null, text);
                },
                function(arr, callback){
                    //later this wont be hard coded it wil happen after sendign a message to user of api to designate choices
                    //or somethign like that
                    json.text = arr[0];

                    callback();
                }
            ], function(err){
                    if(err){
                        console.log("FAILED.");
                    }
                    else{
                        console.log("SUCCESS.");
                        e.emit('parse_complete');
                    }
            });
        }
    });
});

//Prefixing all the routes in the api
wc.use('/api', router);

//Starting Server
wc.listen(PORT);
console.log('Base of the cliff is at port ', PORT);

exports = module.exports = wc;
