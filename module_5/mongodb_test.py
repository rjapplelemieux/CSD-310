import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.gdme2al.mongodb.net/?retryWrites=true&w=majority")
db = ["pytech"]
collection = db["students"]
print (db.list_collection_names)