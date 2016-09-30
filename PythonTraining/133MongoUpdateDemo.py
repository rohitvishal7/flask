from pymongo import MongoClient

client = MongoClient()
db = client.test
result = db.restaurants.update(
    {"restaurant_id": "42704620"},
    {"$set": {"address.street": "East 31st Street"}}
)
print result