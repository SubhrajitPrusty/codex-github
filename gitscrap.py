from bs4 import BeautifulSoup as bs4
import requests
import datetime

codexstart = "2017-09-15"
date = str(datetime.date.today())
username = input("Enter github username : ")

link = "http://www.github.com/"+username+"?tab=overview&from="+codexstart+"&to="+date

url = requests.get(link)

soup = bs4(url.text,"html.parser")

tags = soup.findAll("span",{"class":"float-left"})

print(username,":")

for tag in tags:
	tagStrLis = str(tag.getText()).split("\n")
	tagStr = " ".join([x.strip() for x in tagStrLis]).strip()
	print(tagStr)