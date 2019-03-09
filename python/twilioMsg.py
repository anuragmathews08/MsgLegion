from twilio.rest import Client
import mysql.connector
import sys
mydb=mysql.connector.connect(host="localhost",database="Twillio",user="root",password="root")
file = open('creds.txt','r')
value = file.read()
file.close()
id = str(value)
def send(msg,num):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'ACd83b9c0c3f8ea7b99d7e6db64c6f8b54'
    auth_token = 'c1a1cf620a3a62f4ff8c64d4ff33a77b'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                  body = msg,
                                  from_='+13342593942',
                                  media_url='https://demo.twilio.com/owl.png',
                                  to='+91'+str(num)
                              )


    # print(message.sid)
    

def sendall():
    msg = sys.argv[1]
    mycursor= mydb.cursor()
    countcur = mydb.cursor()
    query = ("select custNumber from customer where adminID = '"+id+"'")
    count = ("select count(*) from customer where adminID = '"+id+"'")
    mycursor.execute(query)
    result = mycursor.fetchall()
    countcur.execute(count)
    num = countcur.fetchall()
    c = num[0][0]
    for i in range(0,c):
      number = result[i][0]
      send(msg,number)

    query2=("insert into msghistory (msgbody,adminID,date) values('"+msg+"','"+id+"',CURDATE())")
    cur=mydb.cursor()
    cur.execute(query2)
    mydb.commit()
    mydb.close()


sendall()
print("1")
