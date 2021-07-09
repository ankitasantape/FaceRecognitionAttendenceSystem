import mysql.connector as mysql
db = mysql.connect(host= 'localhost',user='root',passwd='Ankita$99')
cursor = db.cursor()
cursor.execute("CREATE DATABASE DATA1")
