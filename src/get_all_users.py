import requests
import datetime
import os
import json
import time

def handler(pd: "pipedream"):
    access_token = pd.steps["get_access_token"]['$return_value']
    base_url = os.environ['base_url']
    user_endpoint = 'user'
    app_id = os.environ['app_id']
    app_key = os.environ['app_key']
    headers = {'app_id' : app_id, 'app_key' : app_key, 'access_token' : access_token}

    all_users = []
    page = 1
    total_pages = 1
    while page <= total_pages:
        print('Getting users from page ' + str(page) + '...')
        # Delay to avoid query rate limit of 12 API calls/minute.
        if (page % 11 == 0):
            time.sleep(60)
        response = requests.get(base_url + user_endpoint, headers=headers, params={'page': page})
        if response.status_code == requests.codes.ok:
            response_json = response.json()
            total_pages = response_json["total_pages"]
            all_users += response_json["result"]
            page += 1
        elif response.status_code == requests.codes.too_many_requests:
            pd.flow.exit('Too many requests--Rate limit exceeded! Cancelling workflow...')
            return
        else:
            print(str(response.status_code))
            pd.flow.exit('An error occurred! Cancelling workflow...')
            return
    return all_users
