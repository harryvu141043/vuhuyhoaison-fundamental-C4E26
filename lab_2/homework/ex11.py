def is_inside(x,y):
    count=0
    for i in list(x):
        if i in list(y):
            count+=1
    if count==len(list(x)):
        print("True")
    else:
        print("False")
