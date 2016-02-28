import requests

from constants import *
from postwebhook import main as create_hook

def register_webhook():
    url = 'https://api.ciscospark.com/v1/webhooks/'

    headers = {'Content-type': 'application/json',
               'Authorization': 'Bearer {}'.format(token) }

    # Delete any active hooks
    resp = requests.get(url, headers=headers)
    active_hooks = resp.json()['items']
    for hook in active_hooks:
        if hook['name'] == 'Cheer Bot':
            hook_id = hook['id']
            requests.delete(url + '{}'.format(hook_id), headers=headers)

    # Create new webhook
    create_hook()
