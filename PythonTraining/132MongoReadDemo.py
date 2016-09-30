from pymongo import MongoClient

client = MongoClient()
db = client.test
cursor = db.restaurants.find({})
for document in cursor:
    print(document)
    
print("====================================================================")
#finds documents whose borough field equals "Manhattan".
cursor1 = db.restaurants.find({"borough": "Manhattan"})
for document1 in cursor1:
    print(document1)