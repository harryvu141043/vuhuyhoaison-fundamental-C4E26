from flask import Flask,render_template,request
app = Flask(__name__)
#Bind route to view function
items=[
    {"name":"com rang",
    "price":25000,
    },
    {"name":"pho bo",
    "price":30000,
    },
    {"name":"xoi xeo",
    "price":10000,
    }
]
@app.route("/")
def menu():
    return render_template("menu.html",item_list=items,user="sơn")
@app.route("/food/<int:i>")
def food(i):
    f=items[i]
    return render_template("food_detail.html",item=f)
@app.route("/add_food",methods=["GET","POST"])
def add_food():
    if request.method=="GET":
        return render_template("food_form.html")
    elif request.method=="POST":
        form=request.form
        n=form["name"]
        p=form["price"]
        new_item={
            "name":n,
            "price":p,
        }
        print(type(p))
        items.append(new_item)
        return p
if __name__=="__main__":
    app.run(debug=True, port=6969)


