n=int(input("mời các bạn nhập:"))
s=n//2
l=(n-1)//2
if n%2==0:
    for i in range(s):
        print("x * ",end="")
else:
    for i in range(l):
        print("x * ",end="")
    print("x")

