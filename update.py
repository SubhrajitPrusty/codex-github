import os
import re
from loguru import logger
from userdata import Member
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
dburl = os.environ.get("DB_URI")

try:
    client = MongoClient(dburl, retryWrites=False)
    db = client.get_default_database()

    members = db.members
    telegram = db.telegram_members

    # users_json = os.path.join("static", "users.json")

    # with open(users_json, "r+") as user_file:
    # usernames = json.loads(user_file.read())
    usernames = [x['github_username'] for x in telegram.find()]

    # update db and insert if not present
    for u in usernames:
        if members.count_documents(
                {"username": re.compile(u, re.IGNORECASE)}) >= 0:
            m = Member(u)
            m.fetch()
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

            members.update_one({"username": ud["username"]},
                               {"$set": ud},
                               upsert=True)

    db_usernames = [x['username'] for x in members.find()]

    for u in db_usernames:
        reg = re.compile(u, re.IGNORECASE)
        if not any([reg.match(x) for x in usernames]):
            members.delete_one({"username": u})
            logger.debug(f"Removed {u}")

    for mem in members.find():
        pass
        # logger.debug(mem)

except ConnectionError:
    logger.debug("Could not connect to database")
except Exception as e:
    if type(e).__name__ == 'PyMongoError':
        logger.debug("Could not connect to database")
    else:
        logger.debug("Error: ", e)
