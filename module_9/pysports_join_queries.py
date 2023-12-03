import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(host="localhost",
user="root2"
passwd="root"
db="pysports")
try
    if connection.is_connected():
	    cursor = connection.cursor()
	    cursor.execute ("select database();")
	    db = cursor.fetchone()
	    print("You're connected to database: ", db)

except Error as e:
	print("Error while connecting to MySQL", e)
finally
	if connection.is_connected():
        cursor.close()
        connection.close()
	    print("MySQL connection is closed")