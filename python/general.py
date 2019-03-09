import mysql.connector

def general():
  mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="Twillio")
  file = open('creds.txt','r')
  value = file.read()
  file.close()
  ident =  str(value)
  mycursor=mydb.cursor()
  admin_info=("SELECT adminName,Email,Bussiness FROM admin WHERE adminID = '"+ident+"' ")
  mycursor.execute(admin_info)
  result = mycursor.fetchall()
  for i in result:
    print(result[0][0])
    print(result[0][1])
    print(result[0][2])


  custmorCount=("SELECT count(*)FROM customer WHERE adminID = '"+ident+"' ")
  mycursor.execute(custmorCount)
  custCount = mycursor.fetchall()
  print(custCount[0][0])
          
  msgCount=("SELECT count(*)FROM msghistory WHERE adminID = '"+ident+"' ")
  mycursor.execute(msgCount)
  messageCount = mycursor.fetchall()
  print(messageCount[0][0])
  mydb.close()

general()
            
