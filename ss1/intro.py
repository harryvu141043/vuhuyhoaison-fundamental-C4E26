yob_str=(input('mời bạn nhập:')).isdigit()
if yob_str.isdigit() :
    yob=int(yob_str)
    age=2019-yob
    print(age)
else:
    print("you must enter a number")

