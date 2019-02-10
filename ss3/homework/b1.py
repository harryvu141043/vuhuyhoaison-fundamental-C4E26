s=input("Welcome to our shop, what do you want (C, R, U, D)?:")
items=["T-Shirt"," Sweater"]
if s=="R" or "r":
    print(*items,sep=",")
elif s=="C" or "c":
    items.append("Jeans")
    print(*items,sep=",")
elif s=="U" or "u":
    items[1]="Skirt,Jeans"
    print(*items,sep=",")
elif s=="D" or "d":
    items[1]="Skirt"
    print(*items,sep=",")
else:
    print("sorry for our shop don't have this product")

