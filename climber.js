//TODO: List
var zerorpc = require("zerorpc"),
async = require('async'),
events = require('events');

//exec('nodemon --exec \"python -v\" ./climber.py', function(err, stdout, stderr){
//exec('\"python -v\" ./climber.py', function(err, stdout, stderr){
//    //Handle errors??
//    //Start communication and such???
//    //ensure this closes when done using it nad other debugging
//    if(err){
//        return callback(err);
//    }
//});

function Climber(port){
    this.port = port;
}

Climber.prototype = {
    climb : function(topic, callback){
        var e = new events.EventEmitter();
        // Start python server from this file as a child process to query against.
            console.log("your terring me apart lisa.");
        var child_process = require('child_process');
        child_process.execFile('python', ["./climber.py"], function(err, stdout, stderr){
            if(err){
                throw err;
            }

            console.log("Shut up.");
            var client = new zerorpc.Client();
            client.connect('tcp://127.0.0.1:' + this.port);

            client.invoke("climb", topic, function(err, content, more){
                if(err){
                    return callback(err, null);
                }

                if(!more){
                    client.close();
                    return callback(null, content);
                }
                else{
                    content += content + " ";
                }
            });
        });

    },

    climb_images : function(callback){
        var e = new events.EventEmitter();
        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        client.invoke("climb_images", function(err, content, more){
            if(err){
                callback(err, null);
            }

            if(!more){
                client.close();
                console.log("Returning data climb images...");
                return callback(null, content);
            }
            else{
                content += content + " ";
            }
        });
    },

    climb_links : function(callback){
        var e = new events.EventEmitter();
        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        client.invoke("climb_links", function(err, content, more){
            if(err){
                return callback(err, null);
            }

            if(!more){
                client.close();
                console.log("Returning data climb links...");
                return callback(null, content);
            }
            else{
                content += content + " ";
            }
        });
    }
}

exports = module.exports = Climber;
