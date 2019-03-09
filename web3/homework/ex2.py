import matplotlib.pyplot as plt 
from ex1 import db
food_collection=db["posts"]
new_food={
    "title":"Vũ Huy Hoài Sơn",
    "author":"C4E26",
    "content":"hồi mới vào code còn ko ra gì thế mà bây giờ mình đã đi đến đc đây r nhân tiện là các bạn khóa sau đọc bài này thì cố lên nhé",
 }
food_collection.insert_one(new_food)
