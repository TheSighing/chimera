'use strict'

var spawn = require('child_process').spawn;

var events = require('events')
var eventEmitter = new events.EventEmitter();

var zerorpc = require("zerorpc"),
async = require('async'),
events = require('events');
var climberpy;
var children = [];

function Climber(port, options){
    this.port = port;
    this.options = typeof options !== 'undefined' ? options : null;
}

// TODO: Make this check if python script climber.py is runnign before initiating another spawn of it. `pgrep -f climber.py`
Climber.prototype = {
    climb : function(options, callback){
        climberpy = spawn('python', ['climber.py']);
        console.log("spawned a process");

        children.push(climberpy.pid);

        var topic = null;
        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        if("topic" in options){
            console.log(options.topic);
            topic = options.topic;
            delete options.topic;
        }
        else{
            console.log("No topic set.");
        }

        client.invoke("climb", topic, options, function(err, content, more){
            if(err){
                return callback(err, null);
            }

            if(!more){
                client.close();
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
                return callback(null, content);
            }
            else{
                content += content;
            }
        });
    },

    close : function(){
        console.log("Closing time.");

        children.forEach(function(child){
            console.log(child);
            child.kill();
        })
    }
};

exports = module.exports = Climber;
