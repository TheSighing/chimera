var c = require('./climber');
climber = new c(5050);

climber.climb('wolf', function(err, data){
  console.log(data);
});
