prices={
    "bannana":4,
    "apple":2,
    "orange":1.5,
    "pear":3
    }
stock={
    "bannana":6,
    "apple":0,
    "orange":32,
    "pear":15
}
l=[]
for i in prices:
    print(i)
    print("prices",":",prices[i])
    print("stock",":",stock[i])
    print("Total:",":",prices[i]*stock[i])
    l.append(prices[i]*stock[i])
    s=sum(l)
print("Total of all:",s)

    

