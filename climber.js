var zerorpc = require("zerorpc"),
async = require('async'),
events = require('events');

function Climber(port){
  this.port = port;
}

Climber.prototype = {
  climb : function(topic, callback){
    var e = new events.EventEmitter();
    var client = new zerorpc.Client();
    client.connect('tcp://127.0.0.1:' + this.port);

    client.invoke("climb", topic, function(err, content, more){
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
