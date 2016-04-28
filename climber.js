'use strict'

var spawn = require('child_process').spawn;

var zerorpc = require("zerorpc"),
async = require('async'),
events = require('events');
var climberpy;

function Climber(port, options){
    this.port = port;
    this.options = typeof options !== 'undefined' ? options : null;
}

// TODO: Make this check if python script climber.py is runnign before initiating another spawn of it.
Climber.prototype = {
    climb : function(options, callback){
        var topic = null;
        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);
        climberpy = spawn('python', ['climber.py']);

        if("topic" in options){
            topic = options.topic;
            delete options.topic;
        }

        client.invoke("climb", topic, options, function(err, content, more){
            if(err){
                return callback(err, null);
            }

            if(!more){
                client.close();
                climber.close();
                return callback(null, JSON.parse(content));
            }
            else{
                content += content;
            }
        });
    },

    climb_images : function(options, callback){

        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);
        climberpy = spawn('python', ['climber.py']);

        if("topic" in options){
            topic = options.topic;
            delete options.topic;
        }

        client.invoke("climb_images", topic, options, function(err, content, more){
            if(err){
                callback(err, null);
            }

            if(!more){
                client.close();
                climber.close();
                return callback(null, content);
            }
            else{
                content += content;
            }
        });
    },

    climb_links : function(options, callback){

        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);
        climberpy = spawn('python', ['climber.py']);

        if("topic" in options){
            topic = options.topic;
            delete options.topic;
        }

        client.invoke("climb_links", topic, options, function(err, content, more){
            if(err){
                return callback(err, null);
            }

            if(!more){
                client.close();
                climber.close();
                return callback(null, content);
            }
            else{
                content += content;
            }
        });
    },

    close : function(){
        climberpy.kill('SIGHUP');
    }
};

exports = module.exports = Climber;
