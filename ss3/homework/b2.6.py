
sheep=[5,7,300,90,24,50,75]
print("Hello my name is Sơn and these are my chip sizes")
print(sheep)
print("Now my biggest sheep has size",max(sheep),"let's shear it")
sheep[sheep.index(max(sheep))]=8
print("After shearing,here is my flock")
print(sheep)
m=0
for i in range(3):
    m+=1
    print("Month",m)
    print("One month has passed,now here is my flock")
    if m==3:
        for k in range(7):
            sheep[k]=sheep[k]+50
        print(sheep)
        s=sum(sheep)
        print("My flock has size in total:",s)
        print("I would get",s,"* 2$ =",s*2,"$")
        break
    for j in range(7):
        sheep[j]=sheep[j]+50
    print(sheep)
    print("Now my biggest sheep has size",max(sheep),"let's shear it")
    sheep[sheep.index(max(sheep))]=8
    print("After shearing,here is my flock")
    print(sheep)
    
