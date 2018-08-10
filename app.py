from flask import Flask, url_for, render_template
import json
import os 

json_file_path = os.path.join('static', "users.json")

jtext = open(json_file_path,"r")
j = json.load(jtext)
members = j['members']
localtime = j['time']
context = {"members":members,"localtime":localtime}

jtext.close()

# print(context)

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
	return render_template('index.html',context=context)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)