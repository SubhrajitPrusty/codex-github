from bs4 import BeautifulSoup as bs4
import requests
import json
import os
from datetime import datetime
from pytz import timezone

def contrib(username):
    
	link = "http://www.github.com/"+username+"?tab=overview" #&from="+codexstart+"&to="+date

	url = requests.get(link)
	soup = bs4(url.content,"html.parser")
	
	bigtext = soup.find("h2",{"class":"f4 text-normal mb-2"})

	if(len(bigtext) > 0):
		bigtext = " ".join([x.strip() for x in bigtext.text.split("\n")]).strip()
	else:
		bigtext = ""

	events = soup.findAll("span",{"class":"float-left"})	
	cont = []

	for ev in events:
		cont.append(" ".join([x.strip() for x in ev.text.split("\n")]).strip())

	cont = "\n".join(cont)
	# print(cont)

	profile = soup.find("meta",{"property":"og:image"})
	photo = profile.get("content").split("?")[0]
	# print(photo)

	return (bigtext, cont.strip(), photo)

json_file_path = os.path.join('static', "users.json")

def regen():
	users = open(json_file_path,"r+")
	userstext = users.read()
	j = json.loads(userstext)

	print("Fetching contribution data... This may take some time...")

	for mem in j['members']:
		content = contrib(mem['username'])
		mem['bigtext'] = content[0]
		mem['contrib'] = content[1]
		mem['photo'] = content[2]
	users.close()

	zone = timezone("Asia/Kolkata")
	t = datetime.now(zone)
	localtime = t.strftime("%T %D")
	j['time'] = localtime
	os.rename(json_file_path,json_file_path+".bak")

	users = open(json_file_path,"w")
	users.write(str(json.dumps(j,indent=4,sort_keys=False)).replace("\'",'\"'))
	users.close()


regen()