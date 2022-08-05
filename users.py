import pymongo as pm

connection_database = pm.MongoClient("mongodb://localhost:27017")

db = connection_database['user']

user_collection = db["user_collection"]

user = {
    "user" : "Pepe",
    "start_date" : "02072022",
    "end_date" : "04072022"
}

result = user_collection.insert_one(user)


user_2 = {
    "user" : "Pablo",
    "start_date" : "04092022",
    "end_date" : "10102022"
}

result_2 = user_collection.insert_one(user_2)

query = user_collection.find_one(
    {"user": "Pablo"}
)

print(query)