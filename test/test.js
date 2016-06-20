var c = require('../climber');
climber = new c(5050, {"depth" : 1});

climber.climb({topic: 'wolf'}, function(err, data){
  if(err){
      console.log(err);
  }

  console.log("))))))))))))))))))))))))");
  // console.log(data);
  console.log("))))))))))))))))))))))))");
});


climber.climb({}, function(err, data){
  if(err){
      console.log(err);
  }

  console.log("))))))))))))))))))))))))");
  //console.log(data);
  console.log("))))))))))))))))))))))))");
  climber.close();
});


// climber.climb_images(function(err, data){
//    if(err){
//        console.log(err);
//   }
//
//   console.log(data);
//   //climber.close();
// });
