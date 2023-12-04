import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
user="root",
passwd="BlueDemon1234!@#",
db="pysports")

cursor = connection.cursor()

query = "UPDATE player SET player_id = '21' WHERE player_id = '021'"

sql1 = "UPDATE player SET player_id = '21' WHERE player_id = '021'"
sql2 = "UPDATE player SET team_id = '001' WHERE first_name = 'Smeagol'"

cursor.execute(sql1)
cursor.execute(sql2)
connection.commit()

print(cursor.rowcount, "record(s) affected")

connection.close()