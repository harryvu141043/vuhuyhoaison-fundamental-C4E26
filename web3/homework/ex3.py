import matplotlib.pyplot as plt 
from ex1 import db
food_collection=db["customers"]
foodlist=food_collection.find()
ads=[]#1938
events=[]#3902
wom=[]#1132
for food in foodlist:
    #print(food["ref"])
    if food["ref"]=="ads":
        ads.append(food["ref"])
    elif food["ref"]=="events":
        events.append(food["ref"])
    else:
        wom.append(food["ref"])
a=len(ads)
b=len(events)
c=len(wom)
s=a+b+c
data = [a/s,b/s,c/s]
smart_phone = ["ads", "events", "wom"]
colors = ["#ecf0f1", "#3498db", "#e67e22"]
 
plt.pie(data, labels=smart_phone, colors=colors, autopct='%1.1f%%', startangle=-90, pctdistance=0.9, labeldistance=1.2)
 
# make sure pie is a circle and not an oval
plt.axis("equal")
plt.show()
