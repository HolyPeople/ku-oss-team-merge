import requests
import json


def parse(msg):
    request_data = {'userkey': 'userkey',
                    'text': msg}
    url = 'localhost:8000/api/message'
    res = requests.post(url, json=json.dumps(request_data))
    if res.status_code != 200:
        raise Exception(9999, 'error')

    data = json.loads(res.text)
    intent = data['intents'][0]['intent']
    entities = {}
    for entity in data['entities']:
        entities[entity['entity']] = entity['values'][0]['value']

    return {'intent': intent, 'entities': entities}
