import requests
import json

with open('post_content.json', 'r') as f:
    post_id = json.load(f)

response_resource = requests.delete(f'https://trips-48955.firebaseio.com/trips/{post_id["name"]}.json')

with open('delete_headers.json', 'w') as f:
    json.dump(dict(response_resource.headers), f, sort_keys=True, indent=2)

with open('delete_content.json', 'w') as f:
    json.dump(response_resource.json(), f, sort_keys=True, indent=2)
