from db import food_collection

def add(name,price):
    new_food={}
    new_food["name"]=name
    new_food["price"]=price
    food_collection.insert_one(new_food)
def get():
    food_list=food_collection.find({"price":{"$lte":25000 }})#lazy loading        
    return food_list

if __name__=="__main__":
    # while True:
    #     new_food={}
    #     n=input("name:")
    #     p=str(input("price:"))
    #     add(n,p)
    #     food_collection.insert_one(new_food)
    #     o=input("stop(y/n):?")
    #     if o=="n":
    #
    #          break
    # def get():

    #     food_list=food_collection.find()
    #     return food_list
    food_list=get()
    #1
    # q=food_list[0]
    # print(q["name"])
    # print(q["price"])
    #2
    for food in food_list:
        print(food["name"])
        print(food["price"])



    