


import requests
import json
#passing the entire response so that it can be used for deletion function as the token is supposed to be temporary
def create(user_name,password,client_id,client_secret):
    payload={"client_secret":client_secret, "scopes": ["admin:org", "admin:org_hook", "admin:public_key", "admin:repo_hook", "repo", "user"], "note": "codex-github"}
    url='https://api.github.com/authorizations/clients/'+client_id
    response=requests.put(url, data=json.dumps(payload), auth=(user_name, password))
    return response.json()



# url looks like https://api.github.com/authorizations/340896353
def delete(user_name,password,url):
    response=requests.delete(url, auth=(user_name, password))
    return response.status_code



