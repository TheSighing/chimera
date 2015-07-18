var zerorpc = require("zerorpc"),
async = require('async'),
events = require('events')
exec = require('child_process').exec;

//TODO: List
// or some other way to have the python zerorpc server available

// Start python server from this file as a child process to query against.
exec('nodemon --exec \"python -v\" ./climber.py', function(err, stdout, stderr){
  //Handle errors??
  //Start communication and such???
  if(err){
    callback(err);
    return;
  }
});

function Climber(port){
  this.port = port;
}

Climber.prototype = {
  climb : function(topic, callback){
    var e = new events.EventEmitter();
    var client = new zerorpc.Client();
    client.connect('tcp://127.0.0.1:' + this.port);

    client.invoke("climb", topic, function(err, content, more){
      if(err){
        callback(err, null);
      }

      if(!more){
        client.close();
        callback(null, content);
      }
      else{
        content += content + " "
      }
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
        callback(null, content);
      }
      else{
        content += content + " "
      }
    });
  },
  climb_links : function(callback){
    var e = new events.EventEmitter();
    var client = new zerorpc.Client();
    client.connect('tcp://127.0.0.1:' + this.port);

    client.invoke("climb_links", function(err, content, more){
      if(err){
        callback(err, null);
      }

      if(!more){
        client.close();
        callback(null, content);
      }
      else{
        content += content + " "
      }
    });
  }
}

exports = module.exports = Climber;
