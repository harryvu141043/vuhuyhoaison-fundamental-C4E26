from flask import Flask
about=Flask(__name__)

Users = {
	"huy" :{
			"name" :"Nguyen Quang Huy" ,
			"age" : 29
       },
"tuananh" : {
			"name" : "Huynh Tuan Anh",
			"age" : 22
       }
}
k=[]
v=[]
kv=[]
@about.route("/")
def home():
    return "HELLO"
@about.route("/user/<username>")
def a(username):
    if username in Users:
        k.clear()
        v.clear()
        kv.clear()
        for i in Users[username]:
            kv.clear
            k.append(i)
            v.append(str(Users[username][i]))
        
        for q,w in zip(k,v):
            kv.append(q+":"+w)
            
        return "; ".join(kv)
    else:
        return "User not found"
    
            

if __name__=="__main__":
    about.run(debug=True, port=2001)
