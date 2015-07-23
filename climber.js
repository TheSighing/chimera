var zmq = require('zmq');

/*
Rewrite to be the connection to client.js and to be node js syntax for this below
from core import Client

if __name__ == '__main__':
    c = Client()
    c.connect('tcp://localhost:1234')

    for line in sys.stdin:
        tweet_str = line.strip()
        print c('process', tweet_str)*/


//TODO: List
// SWITCH THE ZERORPC OUT FOR JUST BASE ZMQ

//var x = 0;
//requester.on("message", function(reply) {
//  console.log("Received reply", x, ": [", reply.toString(), ']');
//  x += 1;
//  if (x === 10) {
//    requester.close();
//    process.exit(0);
//  }
//});
//
//requester.connect("tcp://localhost:5555");
//
//for (var i = 0; i < 10; i++) {
//  console.log("Sending request", i, '…');
//  requester.send("Hello");
//}
//
//process.on('SIGINT', function() {
//  requester.close();
//});






// var zmq = require("zmq"),
// // async = require('async'),
// // // events = require('events')
// exec = require('child_process').exec;
// //TODO: List
// // SWITCH THE ZERORPC OUT FOR JUST BASE ZMQ
//
// console.log("Starting...");
//
// // Start python server from this file as a child process to query against.
// exec('nodemon --exec \"python -v\" ./climber.py', function(err, stdout, stderr){
//   //Handle errors??
//   //Start communication and such???
//   if(err){
//     return callback(err);
//   }
//
//   console.log("Initializing route...");
// });
//
// function Climber(port){
//   this.port = port;
// }
//
// Climber.prototype = {
//   climb : function(topic, callback){
//     var e = new events.EventEmitter();
//     var client = new zerorpc.Client();
//     client.connect('tcp://127.0.0.1:' + this.port);
//
//     client.invoke("climb", topic, function(err, content, more){
//       console.log("climb climb climb");
//       if(err){
//         return callback(err, null);
//       }
//
//       if(!more){
//         client.close();
//         console.log("Returning data climb...");
//         return callback(null, content);
//       }
//       else{
//         //console.log(content);
//         content += content + " "
//       }
//     });
//   },
//   climb_images : function(callback){
//     var e = new events.EventEmitter();
//     var client = new zerorpc.Client();
//     client.connect('tcp://127.0.0.1:' + this.port);
//
//     client.invoke("climb_images", function(err, content, more){
//       if(err){
//         callback(err, null);
//       }
//
//       if(!more){
//         client.close();
//         console.log("Returning data climb images...");
//         return callback(null, content);
//       }
//       else{
//         content += content + " "
//       }
//     });
//   },
//   climb_links : function(callback){
//     var e = new events.EventEmitter();
//     var client = new zerorpc.Client();
//     client.connect('tcp://127.0.0.1:' + this.port);
//
//     client.invoke("climb_links", function(err, content, more){
//       if(err){
//         return callback(err, null);
//       }
//
//       if(!more){
//         client.close();
//         console.log("Returning data climb links...");
//         return callback(null, content);
//       }
//       else{
//         content += content + " "
//       }
//     });
//   }
// }
//
// exports = module.exports = Climber;
