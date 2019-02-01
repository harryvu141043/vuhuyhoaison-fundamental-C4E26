weight=float(input("mời bạn nhập cân nặng(kg):"))
đv=input("Bạn muốn dùng đơn vị chiều cao là gì(cm/m)?:")
if đv =="cm":
    height=float(input("Mời bạn nhập chiều cao(cm):"))
    bmi=weight/((height/100)**2)
    if bmi < 16:
        print("Severely underweight.")
    elif 16<=bmi<18.5:
        print("Underweight.")
    elif 18.5<=bmi<25:
        print("Normal.")
    elif 25<=bmi<30:
        print("overweight.")
    else:
        print("obese.")
elif đv =="m":
    height=float(input("Mời bạn nhập chiều cao(m):"))
    bmi=weight/((height)**2)
    if bmi < 16:
        print("Severely underweight.")
    elif 16<=bmi<18.5:
        print("Underweight.")
    elif 18.5<=bmi<25:
        print("Normal.")
    elif 25<=bmi<30:
        print("overweight.")
    else:
        print("obese.")
print("kết thúc chương trình")