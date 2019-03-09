import mysql.connector
import sys


mydb=mysql.connector.connect(host="localhost",database="Twillio",user="root",password="root")
def register():
    name = sys.argv[1]
    Business = sys.argv[2]
    Email = sys.argv[3]
    password = sys.argv[4]
    query="insert into admin(adminName,Email,Pasword,Bussiness) values('"+name+"','"+Email+"',SHA1('"+password+"'),'"+Business+"')"
    cur=mydb.cursor()
    cur.execute(query)
    mydb.commit()
    print("1")
    mydb.close()

register()

    

		
