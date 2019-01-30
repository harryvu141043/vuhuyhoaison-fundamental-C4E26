import math
print("ĐÂY LÀ CHƯƠNG TRÌNH GIẢI PHƯƠNG TRÌNH BẬC 2 ax^2+bx+c=0:")
a=float(input("Mời bạn nhập giá trị hệ số a:"))
b=float(input("Mời bạn nhập giá trị hệ số b:"))
c=float(input("Mời bạn nhập giá trị hệ số c:"))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình này sẽ có dạng 0=0 nên phương trình sẽ có vô số nghiệm.")
        else:
            print("Phương trình này sẽ có dạng",c,"=","0","nên phương trình này vô nghiệm.")
    else:
        print("Phương trình sẽ có dạng",b,"x","+",c,"=","0")
        x=-c/b
        print("Nên phương trình này có nghiệm","x","=",x,".")
else:
    print("Phương trình này sẽ có dạng",a,"x^2","+",b,"x","+",c,"=","0",".")
    delta=(b*b)-(4*a*c)
    if delta<0:
        print("Nên phương trình này sẽ vô nghiệm.")
    elif delta==0:
       x=-b/(2*a)
       print("Nên phương trình này có nghiệm kép x1=x2=",x)
    elif delta>0:
        x1=(-b+(math.sqrt(delta)))/4*a
        x2=(-b-(math.sqrt(delta)))/4*a
        print("Nên phương trình này sẽ có hai nghiệm phân biệt là:")
        print("-nghiệm thứ nhất là x1=",x1)
        print("-nghiệm thứ hai là x2=", x2)
    else:
        print("Nên phương trình này có vô số nghiệm.")
