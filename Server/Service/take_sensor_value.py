import requests
import json


def pm_dust():
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
    data = {
        'ServiceKey': u'Bg9wG6ZtD1EtaCBxSTLokN2O8rZHfUhW+YQLayYHZjpxwOhyng3U/MkAR0vff8ynNiXT2v9o56hvIpyhI73Tgg==',
        'stationName': '광진구',
        'dataTerm': 'month',
        'numOfRows': '5',
        'ver': '1.3',
        '_returnType': 'json'
        }
    return requests.get(url, params=data)
    # url = "?stationName=%EA%B4%91%EC%A7%84%EA%B5%AC&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey=%3D%3D&ver=1.3"
    # request = ul.Request(url)
    # response = ul.urlopen(request)
    # rescode = response.getcode()
    # if (rescode == 200):
    #     responseData = response.read()
    #     rD = xmltodict.parse(responseData)
    #     rDJ = json.dumps(rD)
    #     rDD = json.loads(rDJ)
    #
    #     w_data = rD["response"]["body"]["items"]["item"]
    #
    #     if (w_data["pm10Grade"] == '1'):
    #         pm10Grade = '좋음'
    #     elif (w_data["pm10Grade"] == '2'):
    #         pm10Grade = '보통'
    #     elif (w_data["pm10Grade"] == '3'):
    #         pm10Grade = '나쁨'
    #     elif (w_data["pm10Grade"] == '4'):
    #         pm10Grade = '매우나쁨'
    #     if (w_data["pm25Grade"] == '1'):
    #         pm25Grade = '좋음'
    #     elif (w_data["pm25Grade"] == '2'):
    #         pm25Grade = '보통'
    #     elif (w_data["pm25Grade"] == '3'):
    #         pm25Grade = '나쁨'
    #     elif (w_data["pm25Grade"] == '4'):
    #         pm25Grade = '매우나쁨'
    #
    # return """측정 시각  : %s<br/>미세먼지(PM10) 농도 : %s<br/>미세먼지(PM2.5) 농도 : %s<br/>미세먼지(PM10) 농도 : %s<br/>미세먼지(PM2.5) 농도 :
    #     %s\n" %(w_data["dataTime"], w_data["pm10Value"], w_data["pm25Value"], pm10Grade, pm25Grade) """


if __name__ == "__main__" :
    for li in json.loads(pm_dust().text)['list']:
        print(li)
