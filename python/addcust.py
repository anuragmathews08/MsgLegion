import mysql.connector
import sys
mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Twillio")
def addcust():
    file = open('creds.txt','r')
    value = file.read()
    file.close()
    id= str(value)
    custname=sys.argv[1]
    custphoneNo=sys.argv[2]
    custemail=sys.argv[3]

    mycursor=mydb.cursor()
    customer= ("INSERT INTO customer(custName,custNumber,custMail,adminID) VALUES('"+custname+"','"+custphoneNo+"','"+custemail+"','"+id+"')")
    mycursor.execute(customer)
    mydb.commit()
    print("1")
    mydb.close()


addcust()

