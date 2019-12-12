from flask import Flask, request
from Service import sensor_data, nlg, nlp, toast

app = Flask(__name__)


@app.route('/dialog')
def dialog():
    data = request.args
    print(data)
    if "apiKey" in data:
        print(data["apiKey"])
        if data["apiKey"] == "Hello, World":  # TODO: replace api key to jwt(javascript wep token)
            if "message" in data:
                parse_data = nlp.parse(data['message'])
                return nlg.recognize_intent(parse_data)
    return {"status": 404, "msg": "error"}


@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.json
    if "type" in data:  # type is humidity or temperature
        if data['type'] == 'temp_humi':
            sensor_data.post('temperature', data['data']['temperature'])
            sensor_data.post('humidity', data['data']['humidity'])
        elif data['type'] in ['window']:  # TODO: add FCM for Toast message
            toast.send_to_topic(data['data'])
        else:
            return "error"
    return data


if __name__ == '__main__':
    app.run(host="192.168.0.5")

