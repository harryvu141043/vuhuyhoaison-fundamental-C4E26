favorite=["death note","netflix","teaching"]
m=1
n=0
for i in favorite:
    print(m,i.capitalize(),sep=".")
    m+=1
while True:
    index=input("Position you want to update:")
    
    if index is int:
        if 0<=index-1<len(favorite):
            
        elif index not is int:
            print("Không có số thứ tự này")
        break
    else:
        print("nhập sai")
items=input("Your replacing favorite:")
favorite[index]=items

for j in  favorite:
    print(n+1,".",favorite[n].capitalize())
    n+=1
