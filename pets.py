import pymongo as pm

connection_to_db = pm.MongoClient("mongodb://localhost:27017/")
db = connection_to_db["pets"]
pet_collection = db["pet_collection"]

pet = {
    "name": "Asia",
    "breed": "Husky"
}
result = pet_collection.insert_one(pet)

print("Inserted id: ", result.inserted_id)