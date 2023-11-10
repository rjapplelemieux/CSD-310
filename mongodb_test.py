# import MongoClient
import pymongo
from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@cluster0.gdme2al.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Create a variable named db and assign it to the pytech database instance
db = client["pytech"]

#print the list of collections int eh 'pytech' database
print(db.list_collection_names)