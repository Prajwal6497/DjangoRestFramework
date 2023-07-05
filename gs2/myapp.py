import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Sonam',
    'roll': 101,
    'city': 'Shimoga'
}
#convert python object to json
json_data = json.dumps(data)

response = requests.post(url=URL, data=json_data)

data = response.json()
