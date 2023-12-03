import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
user="root",
passwd="BlueDemon1234!@#",
db="pysports")

cursor = connection.cursor()

sql = "INSERT INTO player (player_id, first_name, last_name) VALUES (%s, %s, %s)"
val = [
	("1", "Thorin", "Oakenshield"),
	("2", "Bilbo", "Baggins"),
	("3", "Frodo", "Baggins"),
	("4", "Saruman", "The White"),
	("5", "Angmar", "Witch-King"),
	("6", "Azog", "The Defiler")
]

cursor.executemany(sql, val)

connection.commit()

print(cursor.rowcount, "was inserted.")