favorite=["death note","netflix","teaching"]
m=1
n=1
z=1
for i in favorite:
    print(m,i.capitalize(),sep=".")
    m+=1
s=input("xóa:")

if s.isdigit():
    x=int(s)
    favorite.pop(x-1)
    for j in favorite:
        print(n,j.capitalize(),sep=".")
        n+=1
else:
    f=str(s)
    favorite.remove(f)
    for k in favorite:
        print(z,k.capitalize(),sep=".")
        z+=1

    
    
