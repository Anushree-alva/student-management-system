from pymongo import MongoClient

client = MongoClient("mongodb+srv://anushree23uca017_db_user:xVkkQMtuW4VZUXWn@cluster0.dkck7ba.mongodb.net/?appName=Cluster0")

db = client["student_db"]
collection = db["students"]

data = {
    "name": "Anushree",
    "roll": "101",
    "course": "BCA"
}

collection.insert_one(data)

print("✅ Data inserted successfully")