
from pymongo import MongoClient

connection_string = "mongodb+srv://form:formtest2023cmvDL@clusterghostcode.lrc32zr.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

print(client.list_database_names())

db = client.capstone

collection = db.form
x = {"Test1": "test hola"}
insert = collection.insert_one(x)

if insert.inserted_id:
    print("done")
else:
    print("failed")