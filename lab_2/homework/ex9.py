def get_even_list(s):
    new=[]
    for i in list(s):
        if i%2==0:
            new.append(i)
    print(new)
    return new
