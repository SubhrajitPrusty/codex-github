from django.shortcuts import render
from django.http import HttpResponse


from django.contrib.staticfiles.templatetags.staticfiles import static

import json
import os


# Create your views here.

def index(request):
	json_file_path = os.path.join('static', "users.json")
	jtext = open(json_file_path,"r")
	j = json.load(jtext)
	members = j['members']
	context = {"members":members}
	jtext.close()
	return render(request, 'user.html', context)