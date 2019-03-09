from pymongo import MongoClient
uri="mongodb+srv://sonvu:he141043@cluster0-lux1l.mongodb.net/test?retryWrites=true"

#mongodb+srv://sonvu:<password>@cluster0-lux1l.mongodb.net/test?retryWrites=true
#1.connect
client=MongoClient(uri)

#2.get database
db=client.test
# #3 collection
food_collection=db["food"] #collection

# #4.create a new document
# new_food={
#     "name":"bun cha",
#     "price":25000,
# }
# #document

# #5.insert new document into collection
# food_collection.insert_one(new_food)
#6.close connection
def close():
    client.close()



