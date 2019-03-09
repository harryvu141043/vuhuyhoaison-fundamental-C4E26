
from ex4 import food_collection
food_list=food_collection.find({"continent":"Africa"})
for food in food_list:
    print(food["name"])
