import mysql.connector

server = 'daksh.database.windows.net'
database = 'mydata_1'
username = 'daksh'
password = 'Daks123@'
driver= "{SQL Server}"
mydb = mysql.connector.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from attendance")

result = mycursor.fetchall()

for i in result:
    print(i)
