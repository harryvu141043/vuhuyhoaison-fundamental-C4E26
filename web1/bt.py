from flask import Flask
bt=Flask(__name__)
@bt.route("/")
def home():
    return "hello"
@bt.route("/add/<int:x>/<int:y>")
def add(x,y):
    s=x+y
    return str(s)
if __name__=="__main__":
    bt.run(debug=True, port=69)

