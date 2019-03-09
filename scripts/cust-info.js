(function(){
    var {PythonShell} = require('python-shell');


    PythonShell.run('./python/custinfo.py',null,function(err,results){
          if(err) throw err;
          console.log("general info of admin: ");
          console.log('results :',results);
          console.log("javascript: ");
        //   for(x = 0; x<3; x++){
            //   console.log(results[0]);
        //   }

        if(results){
           
            getInfo(results);

          function getInfo(values){
              var count = 0;
              //   for first row of table
              var tr = document.createElement('tr');
                tr.setAttribute("id","table-data");
                for(i=0;i<3;i++){
                    var td = document.createElement('td');
                    td.innerHTML = values[count];
                    count++;
                    tr.appendChild(td);
                }
                document.getElementById("info-table").appendChild(tr);
                // creating rest of the rows
              for(;count<values.length;count++){
                var row = document.createElement('tr');
                for(i=0;i<3;i++){
                    var td = document.createElement('td');
                    td.innerHTML = values[count];
                    count++
                    row.appendChild(td);
                }
                document.getElementById("info-table").appendChild(row);                
                
              }

          }


        }
                    
    });    

})(); 
   