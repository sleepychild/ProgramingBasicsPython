import requests
import json

with open('new_trip.json', 'r') as f:
    post_data = json.load(f)

response_resource = requests.post('https://trips-48955.firebaseio.com/trips.json', json=post_data)

with open('post_headers.json', 'w') as f:
    json.dump(dict(response_resource.headers), f, sort_keys=True, indent=2)

with open('post_content.json', 'w') as f:
    json.dump(response_resource.json(), f, sort_keys=True, indent=2)
