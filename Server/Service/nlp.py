import requests
import json


def parse(msg):
    request_data = {'userkey': 'userkey', 'text': msg}
    url = 'http://192.168.0.7:8000/api/message'
    res = requests.post(url, json=request_data)
    if res.status_code != 200:
        raise Exception(9999, 'error')

    data = json.loads(res.text)
    intent = data['intents'][0]['intent']
    entities = {}
    for entity in data['entities']:
        entities[entity['entity']] = entity['values'][0]['value']

    return {'intent': intent, 'entities': entities}
