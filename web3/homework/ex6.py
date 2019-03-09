
from ex4 import food_collection
food_list=food_collection.find(
    {
     "length": {"$lt":1000},"continent":"S. America"
    }
)
for food in food_list:
    print(food["name"])