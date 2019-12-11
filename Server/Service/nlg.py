import json

from . import sensor_data
import random
import requests

def recognize_intent(parse_data):
    print(parse_data['intent'])
    if parse_data['intent'] == '#Welcome':
        return welcome(parse_data['entities'])
    elif parse_data['intent'] == '#Temperature':
        return temperature(parse_data['entities'])
    elif parse_data['intent'] == '#Humidity':
        return humidity(parse_data['entities'])
    elif parse_data['intent'] == '#FineDust':
        return fine_dust(parse_data['entities'])
    else:
        return "잘 모르겠습니다."


def welcome(entities):
    greeting = ['안녕하십니까', '안녕하세요', '만나서 반갑습니다', '저는 머지입니다', '당신의 인공지능 비서 머지입니다.']
    return greeting[random.randint(0, len(greeting))]


def temperature(entities):
    data = sensor_data.get('temperature').order_by_key().get()
    key = list(data.keys())[0]
    return "현재 방안의 온도는 썹시" + str(data[key]['value']) + "도 입니다."


def humidity(entities):
    data = sensor_data.get('humidity').order_by_key().get()
    key = list(data.keys())[0]
    return "현재 방안의 습도는" + str(data[key]['value']) + "퍼센트 입니다."


def fine_dust(entities):
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
    location = '광진구'
    print(entities)
    if '@장소' in entities:
        location = entities['@장소']
    data = {
        'ServiceKey': u'Bg9wG6ZtD1EtaCBxSTLokN2O8rZHfUhW+YQLayYHZjpxwOhyng3U/MkAR0vff8ynNiXT2v9o56hvIpyhI73Tgg==',
        'stationName': location,
        'dataTerm': 'month',
        'numOfRows': '100',
        'ver': '1.3',
        '_returnType': 'json'
    }
    data = json.loads(requests.get(url, params=data).text)['list']
    return "현재 " + location \
           + "의 미세먼지 농도는 " \
           + data[0]['pm10Value'] \
           + ", 평균 " + data[0]['pm10Value24'] \
           + " 이고 초 미세먼지 농도는 " \
           + data[0]['pm25Value'] \
           + ", 평균 " + data[0]['pm25Value24'] + " 입니다."
