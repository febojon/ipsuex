from pymongo import MongoClient

# Create a MongoClient object
client = MongoClient()

# Access a database
db = client.mydatabase

# Access a collection
collection = db.mycollection

# Perform operations on the collection
# For example, insert a document
document = {"name": "John", "age": 30}
result = collection.insert_one(document)
