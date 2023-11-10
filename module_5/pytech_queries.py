import pymongo
from pymongo import MongoClient

# Connect to the MongoDB
client = MongoClient("mongodb+srv://admin:admin@cluster0.gdme2al.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

results = collection.find({})

for x in results:
    print(x)