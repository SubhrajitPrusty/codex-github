import requests
import json
import os
import sys
from pymongo import MongoClient
from userdata import Member

dburl = os.environ["MONGODB_URI"]

client = MongoClient(dburl)

db = client.get_default_database()

members = db.members

users_json = os.path.join("static", "users.json")

with open(users_json, "r+") as usernames:
    usernames = json.loads(usernames.read())
    # print(usernames)
    for u in usernames:
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

        if None in ud.values():
            m.fetch()

        members.update_one(
            {
                "username": ud["username"]
            },
            {
                "$set": ud
            },
            upsert=False)

for mem in members.find():
    print(mem)
