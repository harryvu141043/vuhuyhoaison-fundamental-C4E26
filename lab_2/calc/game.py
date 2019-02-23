import random
while True:
    x=random.randint(1,10)
    y=random.randint(1,10)
    erorr=random.randint(-1,1)
    #s=f"{x}+{y}={r}""
    t=x+y
    k=x+y+erorr
    print(x,"+",y,"=",k)
    y=input("y/n:")
    if (t==k) and y=="y":
        print("yay")
    elif t==k and y=="n":
        print("no")
        break
    elif t!=k and y=="y":
        print("no")
        break
    elif t!=k and y=="n":
        print("yay")

        
