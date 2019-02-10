n=int(input("mời bạn nhập:"))
s=0
for i in range(1,n+1,1):
    if n%i==0:
        s+=1
if s==2:
    print("đây là số nguyên tố")
else:
    print("đây ko phải số nguyên tố.")