import requests
import json

def fine_dust():
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
    data = {
        'ServiceKey': u'Bg9wG6ZtD1EtaCBxSTLokN2O8rZHfUhW+YQLayYHZjpxwOhyng3U/MkAR0vff8ynNiXT2v9o56hvIpyhI73Tgg==',
        'stationName': '광진구',
        'dataTerm': 'month',
        'numOfRows': '100',
        'ver': '1.3',
        '_returnType': 'json'
        }
    return json.loads(requests.get(url, params=data).text)['list']

def particular_fine_dust(dataTime):
    for i in range(1, 101):
        if fine_dust()[i]['dataTime'] == dataTime:
            return fine_dust()[i]['pm10Value']
        else:
            return fine_dust()[0]['pm10Value']

if __name__ == "__main__" :
    for li in fine_dust():
        print(li)
    # print(particular_fine_dust('2019-12-07 04:00'))
