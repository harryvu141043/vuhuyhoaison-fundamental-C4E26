from db import food_collection,user
from bson import ObjectId

def add(name,price):
    new_food={}
    new_food["name"]=name
    new_food["price"]=price
    food_collection.insert_one(new_food)

def get(query):#fitler,limit=5,skip=10
    food_list=food_collection.find(query)#lazy loading        #many
    return food_list 

def get_by_id(id):
    f=food_collection.find_one({"_id":ObjectId(id)})
    return f

def delete_by_id(id):
    food_collection.find_one({"_id":ObjectId(id)})

def update_by_id(id,name,price):
    query={"_id":ObjectId(id)}
    updater={"$set":{"price":price},
    "$set":{"name":name},}
    food_collection.find_one_and_update(query,updater)
def find_by_username(username):
    u=user.find_one({"username":username})
    if u==None:
        return "KO có user này"
    return u


if __name__=="__main__":
    # query={"_id":ObjectId("5c812d3ed007f90e38a64fd9")}
    # updater={  "$set":{  "price":1000 }  }#$inc(tang),$dec(giam),$set(change),$unset(break)
    # food_collection.find_one_and_update(query,updater)
    # print(*get({}),sep="\n")
    
    # food_collection.delete_one({"_id":ObjectId("5c812d38d007f90e38a64fd7")})
    # f=get_by_id("5c812d38d007f90e38a64fd7")
    # if f!=None:
    #     print(f["name"])
    # print(f)
    # while True:
    #     new_food={}
    #     n=input("name:")
    #     p=str(input("price:"))
    #     add(n,p)
    #     food_collection.insert_one(new_food)
    #     o=input("stop(y/n):?")
    #     if o=="n":
    
    #          break
    # def get():

    #     food_list=food_collection.find()
    #     return food_list
    #food_list=get()
    #1
    # q=food_list[0]
    # print(q["name"])
    # print(q["price"])
    #2
    for food in get({"_id":ObjectId("5c812d3ed007f90e38a64fd9") }):
        print(food)



    