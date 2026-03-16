from pymongo import MongoClient

client = MongoClient("mongodb+srv://anushree23uca017_db_user:xVkkQMtuW4VZUXWn@cluster0.dkck7ba.mongodb.net/?appName=Cluster0")
db = client["student_db"]
collection = db["students"]

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll: ")
        course = input("Enter Course: ")

        collection.insert_one({
            "name": name,
            "roll": roll,
            "course": course
        })
        print("✅ Student Added")

    elif choice == "2":
        for s in collection.find():
            print(s)

    elif choice == "3":
        roll = input("Enter Roll to Update: ")
        new_course = input("Enter New Course: ")
        collection.update_one({"roll": roll}, {"$set": {"course": new_course}})
        print("✅ Updated")

    elif choice == "4":
        roll = input("Enter Roll to Delete: ")
        collection.delete_one({"roll": roll})
        print("✅ Deleted")

    elif choice == "5":
        break