var c = require('climber');
climber = new c(5050);

climber.climb('wolf', function(err, data){
  if(err){
      console.log(err);
  }

  console.log(data);
  //climber.close();
});
