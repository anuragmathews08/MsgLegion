import mysql.connector
import sys
def login():  
  mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="Twillio")
  email = sys.argv[1]
  password = sys.argv[2]
  mycursor = mydb.cursor()
  find_user = ("SELECT adminID FROM admin WHERE Email = '"+email+"' AND Pasword = SHA1('"+password+"')")
  mycursor.execute(find_user)
  results = mycursor.fetchall()


  if(len(results)==1):
    value = str(results[0][0]) 
    file = open('creds.txt','w')
    file.write(value)
    file.close()    
    mydb.close()
    print(results[0][0])
  
  
                 
 
login()

        
            

        
            
