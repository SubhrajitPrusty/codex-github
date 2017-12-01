from django.shortcuts import render
from django.http import HttpResponse

# from django.contrib.staticfiles.templatetags.staticfiles import static
import json
import os
import time

# Create your views here.

def index(request):
	json_file_path = os.path.join('static', "users.json")
	jtext = open(json_file_path,"r")
	j = json.load(jtext)
	members = j['members']
	localtime = time.asctime(time.localtime(time.time()))
	context = {"members":members,"localtime":localtime}
	
	jtext.close()
	return render(request, 'user.html', context)