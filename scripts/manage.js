document.getElementById("add-customer").addEventListener("submit",function(e){
    e.preventDefault();
    var name = document.getElementById("cust-name").value;
    var phone = document.getElementById("phone").value;
    var email = document.getElementById("email").value;
    console.log("Name: ", name);
    console.log("Password: ", phone);
    console.log("Email: ", email);


    var {PythonShell} = require('python-shell');

    var options = {
        mode: 'text',
        args: [name,phone,email]
    }

    PythonShell.run('./python/addcust.py',options,function(err,results){
          if(err) throw err;
          console.log("customer added");
          console.log('results :',results);
          if(results[0][0] == 1){
              document.getElementById("cust-name").innerHTML = "";
              document.getElementById("phone").innerHTML = "";
              document.getElementById("email").innerHTML = "";
              document.getElementById("success").style.display="block";
          }
          
    });
});

