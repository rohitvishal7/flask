from pymongo import MongoClient

client = MongoClient()
db = client.test

result = db.restaurants.remove({"borough": "Manhattan"})
print result;