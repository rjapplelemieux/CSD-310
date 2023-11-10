import pymongo
from pymongo import MongoClient

# Connect to the MongoDB
client = MongoClient("mongodb+srv://admin:admin@cluster0.gdme2al.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

# Inserting three new student documents
post1 = {"_id": 1007, "first_name": "Alice", "last_name": "Smith"}
post2 = {"_id": 1008, "first_name": "Bob", "last_name": "Johnson"}
post3 = {"_id": 1009, "first_name": "Charlie", "last_name": "Williams"}

#collection.insert_one(post1)

collection.insert_many([post1, post2, post3])