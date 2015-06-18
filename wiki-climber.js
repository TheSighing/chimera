var wc = require('')(),
//replace with uri-request
request = require('request'),
//replace with the usage of zero mq to communicate to python and use beautiful soup
cheerio = require('cheerio');

wc.get('/climb:title', function(req, res){
    //add a check to see if this is a valid title
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

    res.send(json);
})

wc.listen('8081')

console.log('Base of the cliff is at port 8081');

exports = module.exports = wc;
