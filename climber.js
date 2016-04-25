'use strict'

var spawn = require('child_process').spawn;

var zerorpc = require("zerorpc"),
async = require('async'),
events = require('events');
var climberpy = null;

function Climber(port, options){
    this.port = port;
    this.options = typeof options !== 'undefined' ? options : null;

    climberpy = spawn('python', ['climber.py']);
}

// TODO: Make this check if python script climber.py is runnign before initiating another spawn of it.
Climber.prototype = {
    climb : function(topic, callback){

        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        client.invoke("climb", topic, this.options, function(err, content, more){
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

    climb : function(callback){

        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        client.invoke("climb", null, this.options, function(err, content, more){
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

    climb_images : function(topic, callback){

        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        client.invoke("climb_images", topic, this.options, function(err, content, more){
            if(err){
                callback(err, null);
            }

            if(!more){
                client.close();
                // climberpy.kill('SIGHUP');
                return callback(null, content);
            }
            else{
                content += content;
            }
        });
    },

    climb_images : function(callback){

        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        client.invoke("climb_images", null, this.options, function(err, content, more){
            if(err){
                callback(err, null);
            }

            if(!more){
                client.close();
                // climberpy.kill('SIGHUP');
                return callback(null, content);
            }
            else{
                content += content;
            }
        });
    },

    climb_links : function(topic, callback){

        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        client.invoke("climb_links", topic, this.options, function(err, content, more){
            if(err){
                return callback(err, null);
            }

            if(!more){
                client.close();
                console.log("Returning data climb links...");
                return callback(null, content);
            }
            else{
                content += content;
            }
        });
    },

    climb_links : function(callback){

        var client = new zerorpc.Client();
        client.connect('tcp://127.0.0.1:' + this.port);

        client.invoke("climb_links", null, this.options, function(err, content, more){
            if(err){
                return callback(err, null);
            }

            if(!more){
                client.close();
                console.log("Returning data climb links...");
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
