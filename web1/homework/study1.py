from flask import Flask,redirect
from os import readlink
p=Flask(__name__)
i={
    "name":"Vũ Huy Hoài Sơn",
    "Work":"CODER AT TECHKIDS",
    "School":"FPT UNIVERSITY",
    "Even your dog or your crush":"code",
}
k=[]
v=[]
kv=[]
@p.route("/")
def home():
    return ""
@p.route("/aboutme") 
def a():
    for l in i:
        k.append(l)
        v.append(i[l])
    for q,w in zip(k,v):
        kv.append(q+":"+w)
    return "; ".join(kv)
@p.route("/school")
def b():
    return redirect("http://techkids.vn",302)
if __name__=="__main__":
    p.run(debug=True, port=5000)
