import requests
import json 

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    headers = {'content-type': 'application/json'}
    if id is not None:
        data  = {'id': id} 
    json_data = json.dumps(data)
    resp = requests.get(url = URL, headers=headers, data=json_data)
    data = resp.json()
    print(data)

get_data()

def post_data():
    data = {
        'name': 'pushma',
        'roll': 189,
        'city': 'nisarga'
    }
    headers = {'content-type': 'application/json'}

    json_data = json.dumps(data)
    resp = requests.post(url = URL, headers=headers, data=json_data)
    data = resp.json()
    print(data)
post_data()

def update_data():
    data = {
        'id': 2,
        'name': 'Pooja T',
        'roll': 76,
        'city': 'HassanKarnataka'
    }

    json_data = json.dumps(data)
    resp = requests.put(url = URL, data=json_data)
    data = resp.json()
    print(data)
# update_data()

def delete_data():
    data = {
        'id': 1
    }

    json_data = json.dumps(data)
    resp = requests.delete(url = URL, data=json_data)
    data = resp.json()
    print(data)
# delete_data()




