


import requests

#passing the entire response so that it can be used for deletion function as the token is supposed to be temporary
def create(user_name,password):
    payload='{"scopes": ["admin:public_key", "admin:repo_hook", "delete_repo", "repo", "user"], "note": "codex-github"}'
    response=requests.post('https://api.github.com/authorizations',data=payload,auth=(user_name, password))
    return response.json()



# node link looks like https://api.github.com/authorizations/220896353
def delete(user_name,password,node_link)
    response=requests.delete(node_link, auth=(user_name, password))
    return response.json()



