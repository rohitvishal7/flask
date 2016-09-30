from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.test

result = db.restaurants.insert(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

db.restaurants.insert(
    {
        "address": {
            "street": "3 Hirandani",
            "zipcode": "400079",
            "building": "100",
            "coord": [-13.9557413, 50.7720266]
        },
        "borough": "Indian",
        "cuisine": "Indian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 12
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Onkar",
        "restaurant_id": "42704620"
    }
)
