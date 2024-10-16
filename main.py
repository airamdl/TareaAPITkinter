import json

import requests

response = requests.get("https://dummyjson.com/products")
print(response.status_code)
print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())