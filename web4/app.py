from flask import Flask,render_template,request
from db import food_collection
import food
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("food_open.html")
@app.route("/food_list")
def a():
    #Get all food:1.function? 2.write function?
    all_food=food.get({})
    #Render:food+HTML
    
    

    #Return
    return render_template("food_list.html",item_list=all_food)
@app.route("/food/<id>")
def food_detail(id):
    f=food.get_by_id(id)
    return render_template("food_detail.html",item=f)
@app.route("/add_food",methods=["GET","POST"])
def add_food():
    if request.method=="GET":
        return render_template("food_form.html")
    elif request.method=="POST":
        form=request.form
        n=form["name"]
        p=form["price"]
        food.add(n,p)
        foodt=food_collection.find_one({"name":n})
        return render_template("food_finished.html",m=n,k=p,i=foodt)
if __name__=="__main__":
    app.run(debug=True, port=1234)
