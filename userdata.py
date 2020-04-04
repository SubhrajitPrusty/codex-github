import os
import sys
import json
import requests
from loguru import logger
from dotenv import load_dotenv
from logentries import LogentriesHandler

load_dotenv()

cid = os.environ.get('CLIENT_ID')
csecret = os.environ.get('CLIENT_SECRET')
LOGENTRIES_TOKEN = os.environ.get('LOGENTRIES_TOKEN')

LH = LogentriesHandler(LOGENTRIES_TOKEN)
logger.add(LH, level='DEBUG', format='{name}:{function}:{line} - {message}')

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
		logger.debug("Name :", self.name)
		logger.debug("Username :", self.username)
		logger.debug("Avatar :", self.avatar)
		logger.debug("Bio :", self.bio)
		logger.debug("Public Repos :", self.nRepos)
		logger.debug("Followers :", self.followers)
		logger.debug("Following :", self.following)
		logger.debug("Total Commits :", self.totalCommits)

	@logger.catch
	def getUser(self):
		try:
			payload = {
				"client_id": cid,
				"client_secret": csecret
			}

			USER_API = "https://api.github.com/users/{}".format(self.username)
			r = requests.get(USER_API, params=payload)
			logger.debug(f"{r} FETCHED {self.username} {USER_API}")

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
						logger.debug(f"{r} FETCHING {self.REPOS_URL}")

						rep = r.json()
						for rs in rep:
							# logger.debug(rs['name'])
							self.repos.append(rs['name'])
					else:
						logger.error(f'Request failed {r.reason}')
						break

			self.nRepos = len(self.repos)
			logger.debug(f"no of repos : {len(self.repos)}")
		except NameError:
			logger.error("User not found")
		except Exception as e:
			logger.error("Error: ", e)
			raise e

	@logger.catch
	def getRepoData(self, repo):
		payload = {
			"client_id": cid,
			"client_secret": csecret
		}

		STATS_URL = "https://api.github.com/repos/{}/{}/stats/contributors".format(self.username, repo)

		r = requests.get(STATS_URL, params=payload)
		if r.status_code == 202:
			logger.debug(f'Request redirected, retrying: {STATS_URL}')
			r = requests.get(STATS_URL, params=payload)
		# logger.debug(r)

		if r.status_code == 403:
			logger.error("RATE LIMITED")
			sys.exit(1)

		if len(r.text) == 0:
			logger.error(f'No response {STATS_URL}')
			return 0

		stats = r.json()
		total = [0]
		for st in stats:
			if st['author']:
				if st['author']['login'].lower() == self.username.lower():
					total.append(int(st['total']))
					break

		logger.debug(total)
		if sum(total) != 0:
			return sum(total)
		else:
			return 0

	def getAllCommits(self):
		totalCont = [self.getRepoData(repo) for repo in self.repos]
		self.totalCommits = sum(totalCont)