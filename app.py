import os
import json
from flask import Flask, url_for, render_template, request
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient
from dotenv import load_dotenv
from fuzzywuzzy import fuzz

load_dotenv()

dburl = os.environ.get('MONGODB_URI')

client = MongoClient(dburl)
db = client.get_default_database()
members = db.members

def getContent():
    data = []

    for mem in members.find():
        data.append(mem)

    data = sorted(data, key=lambda k: k['totalCommits'])

    return data[::-1]


app = Flask(__name__, static_url_path='/static')

content = getContent()
total = sum([x['totalCommits'] for x in content])

@app.route("/")
def index():
    global content
    global total
    content = getContent()
    total = sum([x['totalCommits'] for x in content])
    return render_template('index.html', context=content, totalC=total, search=False)


@app.route("/search")
def searchMember():
    query = request.args.get("query")

    if query == "":
        return render_template('search.html', context=content, search=True, found=True)

    # print(query)
    sanitize = lambda x: x.lower() if x else " "
    ratios = [ { "ratio" : max([fuzz.partial_ratio(sanitize(x['name']), query.lower()), fuzz.partial_ratio(sanitize(x['username']), query.lower())]), "data": x } for x in content ]
    
    ratios = sorted(ratios, key=lambda k: k['ratio'])
    
    result = [ x['data'] for x in ratios if x['ratio'] > 60 ][::-1]

    found = len(result) != 0
    
    return render_template('search.html', context=result, search=True, found=found)


@app.route("/<username>")
def profile(username):
    try:
        user_details = [x for x in members.find({"username" : username})].pop()
        print(user_details)

        return render_template("profile.html", user=user_details)
    except IndexError:
        print(e)
        return "404"
    except Exception as e:
        raise e

    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('', port), app)
    print("Server ready:")
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")

