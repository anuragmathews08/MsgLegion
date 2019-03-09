import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Twillio")
def msghistory():
    file = open('creds.txt','r')
    value = file.read()
    file.close()
    id= str(value)
    mycursor=mydb.cursor()
    showhistory=("select msgbody,date from msghistory where adminID ='"+id+"' ")
    mycursor.execute(showhistory)
    result = mycursor.fetchall()
    msgCount=("SELECT count(*)FROM msghistory WHERE adminID = '"+id+"' ")
    mycursor.execute(msgCount)
    messageCount = mycursor.fetchall()


    if messageCount[0][0] > 0:
          for i in range(0,messageCount[0][0]):
            for j in range(0,2):
              print(result[i][j])


    mydb.close()

msghistory()  

         
              
        
