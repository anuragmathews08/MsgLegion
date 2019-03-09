import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Twillio")
def custinfo():
    file = open('creds.txt','r')
    value = file.read()
    file.close()
    id= str(value)
    mycursor=mydb.cursor()
    showcustomer=("select custName,custMail,custNumber from customer where adminID ='"+id+"' ")
    mycursor.execute(showcustomer)
    result = mycursor.fetchall()
    custmorCount=("SELECT count(*)FROM customer WHERE adminID = '"+id+"' ")
    mycursor.execute(custmorCount)
    custCount = mycursor.fetchall()


    if custCount[0][0] > 0:
        for i in range(0,custCount[0][0]):
          for j in range(3):
            print(result[i][j])


    mydb.close()

custinfo()  

         
              
        
