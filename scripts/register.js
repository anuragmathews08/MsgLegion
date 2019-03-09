document.getElementById("regForm").addEventListener("submit",function(e){
    e.preventDefault();
    var name = document.getElementById("name").value;
    var business = document.getElementById("business").value;
    var email = document.getElementById("email").value;
    var pass = document.getElementById("password").value;
    console.log("Email: ", email);
    console.log("Password: ", pass);
    console.log("Name: ", name);
    console.log("Business: ", business);

    var {PythonShell} = require('python-shell');

    var options = {
        mode: 'text',
        args: [name,business,email,pass]
    }

    PythonShell.run('./python/register.py',options,function(err,results){
          if(err) throw err;
          console.log("Admin Added");
          console.log('results :',results[0][0]);
          if(results[0][0]==1){
              document.getElementById("success").style.display="block";
              document.getElementById("name").innerHTML="";
              document.getElementById("business").innerHTML="";
              document.getElementById("email").innerHTML="";
              document.getElementById("password").innerHTML="";
          }
         
    });
});

