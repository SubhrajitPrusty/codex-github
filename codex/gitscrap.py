from bs4 import BeautifulSoup as bs4
import requests
import json
import os
import time

def contrib(username):

	link = "http://www.github.com/"+username+"?tab=overview" #&from="+codexstart+"&to="+date

	url = requests.get(link)

	soup = bs4(url.text,"html.parser")

	btags = soup.findAll("button")
	tags = [tag for tag in btags if tag.findChild("span",{"class":"float-left"})]
	
	cont = ""

	for tag in tags:
		tagStrLis = str(tag.getText()).split("\n")
		tagStr = " ".join([x.strip() for x in tagStrLis]).strip()
		cont+=tagStr+'; '
	
	return cont.strip()

json_file_path = os.path.join("static","users.json")

users = open(json_file_path,"r+")
userstext = users.read()
j = json.loads(userstext)

print("Fetching contribution data... This may take some time...")

for x in j['members']:
	y = contrib(x['username'])
	x['contrib'] = y
users.close()

localtime = time.asctime(time.localtime(time.time()))
j['time'] = localtime
os.remove(json_file_path)

users = open(json_file_path,"w")
users.write(str(j).replace("\'",'\"'))
users.close()