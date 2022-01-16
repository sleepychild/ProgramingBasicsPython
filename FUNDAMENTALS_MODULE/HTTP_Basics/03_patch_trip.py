import requests
import json

with open('patch_trip.json', 'r') as f:
    post_data = json.load(f)

with open('post_content.json', 'r') as f:
    post_id = json.load(f)

response_resource = requests.patch(f'https://trips-48955.firebaseio.com/trips/{post_id["name"]}.json', json=post_data)

with open('patch_headers.json', 'w') as f:
    json.dump(dict(response_resource.headers), f, sort_keys=True, indent=2)

with open('patch_content.json', 'w') as f:
    json.dump(response_resource.json(), f, sort_keys=True, indent=2)
