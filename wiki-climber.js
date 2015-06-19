var express = require('express'),
wc = express(),
bodyParser = require('body-parser'),
//TODO: replace with uri-request
request = require('request'),
//TODO: replace with the usage of zero mq to communicate to python and use beautiful soup
cheerio = require('cheerio');

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

router.get('/climb/:title', function(req, res){
    console.log("climbing");
    //TODO: Add a check to see if this is a valid title
    var url = 'http://en.wikipedia.org/?title=' + req.params.title;
    var text;
    var json = {text : ""};

    request(url, function(err, response, data){
        if(!err){
            var $ = cheerio.load(data);


            //filter the results
            $('p:first').filter(function(){
                var p = $(this);

                json.text = p;
            })
        }
    })

    res.json(json);
});

//Prefixing all the routes in the api
wc.use('/api', router);

//Starting Server
wc.listen(PORT)

console.log('Base of the cliff is at port ', PORT);

exports = module.exports = wc;
