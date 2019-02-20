from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
url="https://www.apple.com/itunes/charts/songs/"
conn=urlopen(url)
print(conn)
raw_data=conn.read()
page_content=raw_data.decode("utf8")
print(page_content)
soup=BeautifulSoup(page_content,"html.parser")
ul=soup.find("ul","")
li_list=ul.find_all("li")
new_list=[]
for li in li_list:
    h3=li.h3
    a=h3.a
    name=a.string
    h4=li.h4
    a=h4.a
    artists=a.string
    news={
        "name":name,
        "artists":artists,
    }
    new_list.append(news)
pyexcel.save_as(records=new_list,dest_file_name="music.xlsx")
print(new_list)
dl=YoutubeDL()
options={
    "default_search":"ytsearch",
    "max_download":1
}
dl=YoutubeDL(options)
for i in range(len(new_list)):
    a=new_list[i]["name"]
    b=new_list[i]["artists"]
    c=a+b
    dl.download([str(c)])

