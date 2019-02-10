"""item1="phở xào"
item2="Ghẹ"
item3="Sò huyết"
item4="Cháo"
item5="Cơm rang"""""
items=["Ghẹ","Sò huyết","Cháo"]
print(items)
items.append("Cơm rang")
print(*items,sep="\n")
"""items.pop(1)
print(items)"""
i=int(input("Index:"))
new_value=input("New value:")
items[i]=new_value
print(items)

