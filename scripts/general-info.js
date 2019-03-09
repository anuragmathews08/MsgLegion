(function(){
    var {PythonShell} = require('python-shell');


    PythonShell.run('./python/general.py',null,function(err,results){
          if(err) throw err;
          console.log("general info of admin: ");
          console.log('results :',results);
          document.getElementById("admin-name").innerHTML= results[0];
          document.getElementById("admin-mail").innerHTML= results[1];
          document.getElementById("admin-business").innerHTML= "Business : "+results[2];
          document.getElementById("msg-count").innerHTML = results[4];
          document.getElementById("cust-count").innerHTML = results[3];
    });    

})(); 
   