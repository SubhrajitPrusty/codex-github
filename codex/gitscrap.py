from bs4 import BeautifulSoup as bs4
import requests
import json
import os
from datetime import datetime
from pytz import timezone

def contrib(username):

	link = "http://www.github.com/"+username+"?tab=overview" #&from="+codexstart+"&to="+date

	url = requests.get(link)

	soup = bs4(url.text,"html.parser")

	green_tags = soup.findAll("span",{"class":"f6 text-green"})
	
	btags = soup.findAll("button")
	tags = [tag for tag in btags if tag.findChild("span",{"class":"float-left"})]
	
	cont = ""
	for tag in tags:
		tagStrLis = str(tag.getText()).split("\n")
		tagStr = " ".join([x.strip() for x in tagStrLis]).strip()
		cont+=tagStr+'; '
	
	for green in green_tags:
		greenStrLis = str(green.getText()).split("\n")
		greenStr = " ".join([x.strip() for x in greenStrLis]).strip()
		cont+=greenStr+'; '

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

zone = timezone("Asia/Kolkata")
t = datetime.now(zone)
localtime = t.strftime("%T %D")
j['time'] = localtimeP
os.remove(json_file_path)

users = open(json_file_path,"w")
users.write(str(j).replace("\'",'\"'))
users.close()