import requests
import json

response_resource = requests.get('https://trips-48955.firebaseio.com/trips.json')

with open('get_headers_d.json', 'w') as f:
    json.dump(dict(response_resource.headers), f, sort_keys=True, indent=2)

with open('get_content_d.json', 'w') as f:
    json.dump(response_resource.json(), f, sort_keys=True, indent=2)
