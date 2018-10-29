import os
import sys

from dotenv import load_dotenv
from flask import Flask, url_for, render_template
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient

import update

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


@app.route("/")
def index():
    content = getContent()
    total = sum([x['totalCommits'] for x in content])
    return render_template('index.html', context=content, totalC=total)


if __name__ == '__main__':
    if sys.argv and '--update' in sys.argv:
        update.main()
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()
