q=["If x=8,then what is the value of 4(x+3)?:"]
a=[[35,36,40,44]]
a0=a[0]
print(*q,sep="")
for i in range(len(a0)):
    print(i+1,".",a0[i])
n=int(input("your choice:"))
if n==4:
    print("Bingo")
else:
    print(":(")    