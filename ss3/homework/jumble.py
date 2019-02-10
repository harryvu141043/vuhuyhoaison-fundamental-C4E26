import random
n=[["c","h","a","m","p","i","o","n"],["m","e","t","i","c","u","l","o","u","s"],["h","e","x","a","g","o","n"]]
random.shuffle(n)
for i in n:
    random.shuffle(i)
    print(*i)
    s=input("Your answer:")
    if "champion"==''.join(i) or ''.join(i)=="meticulous" or ''.join(i)=="hexagon":
        continue
    if list(s)==i:
        if s=="champion" or s=="meticulous" or s=="hexagon":
            print("Hura")
            continue
        else:
            print(":)")
            while True:
                b=input("Your answer:")
                if len(list(b))==len(i) and max(list(b))==max(i) and min(list(b))==min(i) and ''.join(i)!=b :
                    print("Hura")
                    break
                else:
                    print(":)")
    if not list(s)==i:
        if len(list(s))==len(i) and max(list(s))==max(i) and min(list(s))==min(i):
            print("Hura")
            continue
        else:
            print(":)")
            while True:
                a=input("Your answer:")
                if len(list(a))==len(i) and max(list(a))==max(i) and min(list(a))==min(i):
                    print("Hura")
                    break
                else:
                    print(":)")



          
  
    

    

    
    

   
                   


