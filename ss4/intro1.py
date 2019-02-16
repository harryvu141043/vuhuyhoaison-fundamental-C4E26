p0={#unordered
    "name":"H.Duc",
    "age":24,
    "location":"Hai Phong",
    "status":False,
    "favs":["books","movies","music"],
}

p1={
    "name":"Hoàng",
    "age":21,
    "location":"Hà nội",
    "status":"suyt",
}
p2={
    "name":"Sơn",
    "age":19,
    "location":"Hưng yên",
    "status":True,
}
p_list=[
    {
    "name":"H.Duc",
    "age":24,
    "location":"Hai Phong",
    "status":False,
    "favs":["books","movies","music"],
    },
    {
    "name":"Hoàng",
    "age":21,
    "location":"Hà nội",
    "status":"suyt",
    }
    ,
    p2,
] 
print(p_list)

#print(p_list)
#print(p_list[1])
p=p_list[0]


print(p['location'])



