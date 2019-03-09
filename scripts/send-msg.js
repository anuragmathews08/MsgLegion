document.getElementById("add-customer").addEventListener("submit",function(e){
    e.preventDefault();
    var message = document.getElementById("message").value;
    console.log("Message: ", message);

    var {PythonShell} = require('python-shell');

    var options = {
        mode: 'text',
        args: [message]
    }

    PythonShell.run('./python/twilioMsg.py',options,function(err,results){
          if(err) throw err;
          console.log("customer added");
          console.log('results :',results);
          if(results[0][0] == 1){
              document.getElementById("success").style.display="block";
          }
          
    });
});

