from pymongo import MongoClient

client = MongoClient()
db = client.test
print db