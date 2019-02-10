yob_str=input("year of birth?:")
if not yob_str.isdigit():
    print("Uhuh,not OK")
yob=int(yob_str)
age=2018-yob
print(age)
