from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
k=input("mời nhập:")
url="https://wind.waqi.info/nsearch/full/{}?n=4".format(k)
conn=urlopen(url)
raw_data=conn.read()
page_content=raw_data.decode("utf8")
soup=BeautifulSoup(page_content,"html.parser")
p=json.loads(page_content)
l=p["results"]

for i in l:
    if i["s"]["t"] is not None:
        
        print("location:",i["s"]["n"][0])
        print("time:",i["s"]["t"][0])
        print("AQI:",i["s"]["a"])
        print("*"*30)


