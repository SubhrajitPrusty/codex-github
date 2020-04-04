import requests
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()

cid = os.environ.get('CLIENT_ID')
csecret = os.environ.get('CLIENT_SECRET')


class Member():

	def __init__(self, u):
		self.username = u
		self.name = ""
		self.avatar = ""
		self.bio = ""
		self.followers = 0
		self.following = 0
		self.REPOS_URL = f"https://api.github.com/users/{u}/repos"
		self.repos = []
		self.nRepos = 0
		self.totalCommits = 0

	def fetch(self):
		self.getUser()
		self.getAllCommits()

	def printData(self):
		print("Name :", self.name)
		print("Username :", self.username)
		print("Avatar :", self.avatar)
		print("Bio :", self.bio)
		print("Public Repos :", self.nRepos)
		print("Followers :", self.followers)
		print("Following :", self.following)
		print("Total Commits :", self.totalCommits)

	def getUser(self):
		try:
			payload = {
				"client_id": cid,
				"client_secret": csecret
			}

			USER_API = "https://api.github.com/users/{}".format(self.username)
			r = requests.get(USER_API, params=payload)
			print(r, f"FETCHING {self.username}", USER_API)

			if r.status_code == 404:
				raise NameError
			elif r.status_code == 403:
				raise Exception("Rate limit exceeded")
			else:
				userdata = json.loads(r.text)
				self.avatar = userdata['avatar_url']
				self.name = userdata['name'] if userdata['name'] is not None else self.username
				self.REPOS_URL = userdata['repos_url']
				self.nRepos = userdata['public_repos']
				self.bio = userdata['bio']
				self.followers = userdata['followers']
				self.following = userdata['following']

				payload['per_page'] = 100
				page_count = (self.nRepos//100) + 1	

				for i in range(1,page_count+1):
					payload['page'] = i
					r = requests.get(self.REPOS_URL, params=payload)

					if r.status_code == 200:
						print(r, f"FETCHING {self.REPOS_URL}")

						rep = r.json()
						for rs in rep:
							print(rs['name'])
							self.repos.append(rs['name'])
					else:
						print(r.reason)
						break

			return self.avatar, self.name, self.REPOS_URL, self.repos, self.nRepos
		except NameError:
			print("User not found")
		except Exception as e:
			print("Error: ", e)

	def getRepoData(self, repo):
		payload = {
			"client_id": cid,
			"client_secret": csecret
		}

		STATS_URL = "https://api.github.com/repos/{}/{}/stats/contributors".format(self.username, repo)

		r = requests.get(STATS_URL, params=payload)
		if r.status_code == 202:
			r = requests.get(STATS_URL, params=payload)
		# print(r)

		if r.status_code == 403:
			print("RATE LIMITED")
			sys.exit(1)

		if len(r.text) == 0:
			return -1

		stats = json.loads(r.text)
		total = [0]
		for st in stats:
			if st['author']:
				if st['author']['login'].lower() == self.username.lower():
					total.append(int(st['total']))
					break

		if sum(total) != 0:
			return sum(total)
		else:
			return -1

	def getAllCommits(self):
		totalCont = [0]
		for rs in self.repos:
			c = self.getRepoData(rs)
			if c != -1:
				totalCont.append(c)
		self.totalCommits = sum(totalCont)

		if self.totalCommits != 0:
			return self.totalCommits
		else:
			return -1
