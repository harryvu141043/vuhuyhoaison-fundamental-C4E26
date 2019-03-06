from flask import Flask,render_template,request
app = Flask(__name__)
items=[
    {"model":"vision 110cc",
    "dailyfee":"29990000",
    "image":"https://hondaxemay.com.vn/wp-content/uploads/2018/10/450x250_xe-1_450x250_acf_cropped.png",
    "year":"2018",
    }
]
@app.route("/")
def home():
    return render_template("menubike.html",item_list=items)
@app.route("/new_bike",methods=["GET","POST"])
def add():
    if request.method=="GET":
        return render_template("ex1.html")
    elif request.method=="POST":
        form=request.form
        a=form["model"]
        b=form["dailyfee"]
        c=form["image"]
        d=form["year"]
        new_item={
            "model":a,
            "dailyfee":b,
            "image":c,
            "year":d,
        }
    
        items.append(new_item)
        return str(items)
if __name__=="__main__":
    app.run(debug=True, port=20000)
