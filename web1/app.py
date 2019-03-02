from flask import Flask

app = Flask(__name__)
#Bind route to view function
@app.route("/")#trang chu
def home():#view function
    print("C4E,hihi")
    return "C4E26"
@app.route("/myclass")
def myclass():
    return "C4E,SON,TUAN,..."
@app.route("/hi/<name>")
def hi_duc(name):
    return "hi "+name

if __name__=="__main__":
    app.run(debug=True, port=6969)


