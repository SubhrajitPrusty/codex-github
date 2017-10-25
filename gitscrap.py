from bs4 import BeautifulSoup as bs4
import requests
import datetime
import json

def contrib(username):

	codexstart = "2017-09-15"
	date = str(datetime.date.today())

	link = "http://www.github.com/"+username+"?tab=overview&from="+codexstart+"&to="+date

	url = requests.get(link)

	soup = bs4(url.text,"html.parser")

	btags = soup.findAll("button")
	tags = [tag for tag in btags if tag.findChild("span",{"class":"float-left"})]
	
	cont = ""

	for tag in tags:
		tagStrLis = str(tag.getText()).split("\n")
		tagStr = " ".join([x.strip() for x in tagStrLis]).strip()
		cont+=tagStr+"\n"
	
	return cont


# print(contrib("dibyasonu"))

users = open("users.json","r+")
userstext = users.read()
j = json.loads(userstext)
for x in j['members']:
	y = contrib(x['username'])
	x['contrib'] = y


users.seek(0)
users.write(str(j).replace("\'",'\"'))