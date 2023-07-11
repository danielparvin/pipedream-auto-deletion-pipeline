import os
import requests

def handler(pd: "pipedream"):
    base_url = os.environ['base_url']
    request_token_endpoint = 'oauth2/requestToken'
    authorization_code = os.environ['authorization_code']
    payload = {'authorization_code' : authorization_code}
    app_id = os.environ['app_id']
    app_key = os.environ['app_key']
    headers = {'app_id' : app_id, 'app_key' : app_key}

    response = requests.post(base_url + request_token_endpoint, headers=headers, params=payload)
    access_token = response.json()["access_token"]
    return access_token