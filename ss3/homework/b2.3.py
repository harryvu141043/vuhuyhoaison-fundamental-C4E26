sheep=[5,7,300,90,24,50,75]
print("Hello my name is Sơn and these are my chip sizes")
print(sheep)
print("Now my biggest sheep has size",max(sheep),"let's shear it")
sheep[sheep.index(max(sheep))]=8
print("After shearing ,here is my flock")
print(sheep)
