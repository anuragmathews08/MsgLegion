document.getElementById("logForm").addEventListener("submit",function(e){
    e.preventDefault();
    var email = document.getElementById("email").value;
    var pass = document.getElementById("password").value;
    console.log("Email: ", email);
    console.log("Password: ", pass);

    var {PythonShell} = require('python-shell');

    var options = {
        mode: 'text',
        args: [email,pass]
    }

    PythonShell.run('./python/login.py',options,function(err,results){
          if(err) throw err;
          console.log("Email and password got in python");
          console.log('results :',results);
          if(results){
              location.href = "./general-info.html";
          }
          else{
              document.getElementById("error").innerHTML = "<p>Username and Password does not match</p>";
          }
    });
});

