var c = require('../climber');
climber = new c(5050);

console.log("climbing in general");

climber.climb('wolf', function(err, data){
  if(err){
      return;
  }

  console.log(data);
});

console.log("climbing images");

climber.climb_images(function(err, data){
  if(err){
      return;
  }

  console.log(data);
});

console.log("climbing links");

climber.climb_links(function(err, data){
  if(err){
      return;
  }
  
  console.log(data);
});
