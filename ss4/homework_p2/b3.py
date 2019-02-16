q=["If x=8,then what is the value of 4(x+3)?:","Jack scored these marks in 5 math tests:49,81,72,66 and 52.what is the mean?:"]
a=[[35,36,40,44],["about 55","about 65","about 75","about 85"]]
ad=[44,"about 65"]
dic={
    q[0]:a[0],
    q[1]:a[1],
}
m=0
count=0
for i in dic:
    print(i)
    for j,t in enumerate(dic[i],1):
        print(j,".",t)
    n=int(input("Your choice:"))
    if n <= len(dic[i]) and n==dic[i].index(ad[m])+1:
        print("Bingo")
        count+=1
    else:
        print(":(")
    m+=1
print("You correctly answer",count,"of 2 question.")
#c2:
dic0={}
count=0
for i in range(len(q)):
    dic0[q[i]]=a[i]
    print(q[i])
    for j,t in enumerate(dic0[q[i]],1):
        print(j,".",t)
    n=int(input("Your choice:"))
    if n <= len(dic0[q[i]]) and n==dic0[q[i]].index(ad[i])+1:
        print("Bingo")
        count+=1
    else:
        print(":(")
print("You correcly answer",count,"of",i+1,"question")
    
    

        