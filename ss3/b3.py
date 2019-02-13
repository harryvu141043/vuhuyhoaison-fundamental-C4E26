so=["I","II","III"]
favorite=["neflix","redbull","kkk"]
m=0
#for i in so:
    #print(i,".",(favorite[m]))
    #m+=1
print(*zip(so,favorite))
#c2:
for s,f in zip(so,favorite):
    print(s,".",f)
