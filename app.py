import json
import os

from flask import Flask, url_for, render_template, request
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient
from dotenv import load_dotenv
from fuzzywuzzy import fuzz

load_dotenv()

def getContent():
    dburl = os.environ.get('MONGODB_URI')

    client = MongoClient(dburl)

    db = client.get_default_database()

    members = db.members

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
    ratios = [ { "ratio" : fuzz.partial_ratio(x['name'].lower(), query.lower()), "data": x } for x in content ]
    
    ratios = sorted(ratios, key=lambda k: k['ratio'])
    
    result = [ x['data'] for x in ratios if x['ratio'] > 60 ][::-1]

    found = len(result) != 0
    
    return render_template('search.html', context=result, search=True, found=found)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()
