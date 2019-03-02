from flask import Flask
menu=Flask(__name__)
m=["com", "pho xao", "bun cha"]
print(str(m))
p=[]
@menu.route("/")
def home():
    return "hello"
@menu.route("/menu")
def n():
    return " ".join(m)
@menu.route("/food/<int:x>")
def l(x):
    return m[x]
if __name__=="__main__":
    menu.run(debug=True, port=6990)
