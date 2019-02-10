pwd=input("Enter your password:")
while (len(pwd)<=8) or pwd.isalpha() or pwd.isupper() or pwd.islower() or pwd.isdigit :
    print("Not ok")
    if (len(pwd)<=8):
        print("Password length must be greater than 8")
    if (pwd.isalpha()):
        print("password must contain number")   
    if pwd.islower() or pwd.isupper():
        print("password must contain both upper and lower characters")
    pwd=input("Enter your password:")

