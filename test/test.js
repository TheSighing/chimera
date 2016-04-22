var c = require('../climber');
climber = new c(5050, {"depth" : 1});

// climber.climb('wolf', function(err, data){
//   if(err){
//       console.log(err);
//   }
//
//   console.log(data);
//   //climber.close();
// });

climber.climb_images('wolf', function(err, data){
   if(err){
       console.log(err);
  }

  console.log(data);
  //climber.close();
});
