a=input("Mời bạn nhập:")
A={}
for i in a.lower():
    A[i]=A.get(i,0)+1
B=list(A.items())
B.sort()
for b,s in B:
    print(b,":",s)



    

        
        
        

    
