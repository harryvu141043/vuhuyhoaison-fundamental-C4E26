favorite=["death note","netflix","teaching"]
m=1
n=1
for i in favorite:
    print(m,i.capitalize(),sep=".")
    m+=1
value=str(input("xóa:"))
favorite.remove(value)
for j in favorite:
    print(n,j.capitalize(),sep=".")
    n+=1
