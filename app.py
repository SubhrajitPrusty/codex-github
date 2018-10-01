from flask import Flask, url_for, render_template
import json
import os 
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient

def getContent():
	dburl = os.environ['MONGODB_URI']

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
	return render_template('index.html',context=content)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	http_server = WSGIServer(('',port),app)
	http_server.serve_forever()
	# app.run(host='0.0.0.0', port=port)
