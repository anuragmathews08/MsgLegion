document.getElementById("log-out").addEventListener("click",function(e){
    e.preventDefault();
    var {PythonShell} = require('python-shell');

    PythonShell.run('./python/logout.py',null,function(err,results){
          if(err) throw err;
          console.log('results :',results);
          if(results[0][0] == 1){
            location.href = "./index.html";
          }
          
    });
});