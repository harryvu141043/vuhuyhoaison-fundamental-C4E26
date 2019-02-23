import random
import b1
x=random.randint(1,10)
y=random.randint(1,10)
pt=random.choice(["+","-","*","/"])
erorr=random.randint(-1,1)
r=b1.evaluate(x,y,pt)+erorr
s=f"{x}{pt}{y}={r}"
print(x)
t=x+y
k=x+y+erorr
print(s)
y=input("y/n:")
if erorr==0:
    if y=="y":
            print("yay")
    else:
        print("no")
        
else:
    if y=="y":
        print("no")
        
    else:
        print("yay")

    