import requests


def send_to_topic(msg):
    url = "https://fcm.googleapis.com/fcm/send"
    data = {
        "notification": {
            "title": "창문 열림 감지 센서",
            "body": msg
        },
        "to": "/topics/alert",
        "priority": "high",
        "data": {
            "urlLink": "Test"
        }
    }
    headers = {'Content-Type' : 'application/json; UTF-8', 'Authorization': 'key=AAAAwEKhE3E:APA91bE_iolYfM0OeSZZX45CREUh2F9R8Dtr-iWsn7P87a8rNOklDuDdaWGFmRXAlvyfGoqhr8tkF4YzMtUWHzKaMgJHSAZVwcXZngYq_vCCYt17FGNViC-hy1LRGqmOWb40VaJR3hgy'}
    requests.post(url, headers=headers, json=data)