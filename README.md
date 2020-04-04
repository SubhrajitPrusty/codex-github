# codex-github [![](https://img.shields.io/badge/codex-github-blue.svg?style=for-the-badge&display=inline-block)](http://codex-github.herokuapp.com)
Contributions of Codex members on Github 

[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FSubhrajitPrusty%2Fcodex-github%2Fbadge%3Fref%3Dmaster&style=for-the-badge)](https://actions-badge.atrox.dev/SubhrajitPrusty/codex-github/goto?ref=master)

# Resources Used

![](https://img.shields.io/badge/python-flask-green.svg?style=for-the-badge&display=inline-block&logo=python)
![](https://img.shields.io/badge/%E2%86%91_Deploy_to-Heroku-7056bf.svg?style=for-the-badge&display=inline-block&logo=heroku)
![](https://img.shields.io/badge/MongoDB-3.6-brightgreen.svg?style=for-the-badge&display=inline-block&logo=mongodb)
![](https://img.shields.io/badge/html-5-blue.svg?style=for-the-badge&display=inline-block&logo=html5)
![](https://img.shields.io/badge/css-3-green.svg?style=for-the-badge&display=inline-block&logo=css3)

# Build and Deploy

## API Setup

- Create an OAuth app on Github
- Set environment value `CLIENT_ID` as the `client_id` of the OAuth app
- Set environment value `CLIENT_SECRET` as the `client_secret` of the OAuth app

## Database Setup

- Create a MongoDB server. I've used [MLab](https://www.mlab.com/)
- Set environment value `MONGODB_URI` to the MongoDB server url
- Create a collection `members`

## Members setup

- Add the members you want to show in [users.json](./static/users.json)
- Run `python update.py`
- Wait for it to populate the database

## Run the app and deploy

- Install all dependencies `pip install -r requirements.txt`
- Run `python app.py`
- Browse to `localhost:5000`
- Deploy to your preferred platform. I've used heroku.

## Updating and maintainance

- Create a scheduler to run `python update.py` every hour. (If it is run more than once an hour, you can get rate limited)
- Everytime you add a new name to the list, it is safer to manually run `python update.py` \
  rather than wait for it to update at the next schedule
