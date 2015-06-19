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

var PORT = process.envPort || 8080;

//The routes for out API
var router = express.Router();

router.get('/', function(req, res){
    json = { help: "helpful message on how to use api."};
    res.json(json);
})

router.route('/search')

    .get('/search/:title', function(req, res){
        //TODO: Add a check to see if this is a valid title
        var url = 'http://en.wikipedia.org/?title=' + req.params.title;

        request(url, function(err, response, data){
            if(!err){
                var $ = cheerio.load(data);

                var text;
                var json = {text : ""};

                //filter the results
                $('p:first').filter(function(){
                    var p = $(this);

                    json.text = p;
                })
            }
        })

        res.json(json);
    })

//Prefixing all the routes in the api
wc.use('/climb', router);

//Starting Server
wc.listen(PORT)

console.log('Base of the cliff is at port 8081');

exports = module.exports = wc;
