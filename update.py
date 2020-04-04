import requests
import json
import os
import sys
from pymongo import MongoClient
from userdata import Member
import re
from dotenv import load_dotenv

load_dotenv()
dburl = os.environ.get("MONGODB_URI")

try:
	client = MongoClient(dburl)
	db = client.get_default_database()

	members = db.members

	users_json = os.path.join("static", "users.json")

	with open(users_json, "r+") as user_file:
		usernames = json.loads(user_file.read())
		
		# update db and insert if not present
		for u in usernames:
			if members.count_documents({"username": re.compile(u, re.IGNORECASE)}) >= 0:
				m = Member(u)
				m.fetch()
				# m.printData()
				ud = {
					"name": m.name,
					"username": m.username,
					"avatar": m.avatar,
					"bio": m.bio,
					"nRepos": m.nRepos,
					"followers": m.followers,
					"following": m.following,
					"totalCommits": m.totalCommits
				}

				members.update_one({ "username": ud["username"]},
									{"$set": ud},
									upsert=True)

	db_usernames = [x['username'] for x in members.find()]

	for u in db_usernames:
		reg = re.compile(u, re.IGNORECASE)
		if not any([reg.match(x) for x in usernames]):
			members.delete_one({"username" : u})
			print(f"Removed {u}")

	for mem in members.find():
		print(mem)
		
except ConnectionError:
	print("Could not connect to database")
except Exception as e:
	if type(e).__name__=='PyMongoError':
		print("Could not connect to database")
	else:
		print("Error: ", e)