from flask import Flask, request
from Service import sensor_data

app = Flask(__name__)


@app.route('/dialog')
def dialog():
    data = request.json
    if "apiKey" in data:
        print(data["apiKey"])
        if data["apiKey"] == "Hello, World":  # TODO: replace api key to jwt(javascript wep token)
            if "message" in data:
                return data['message']
    return {"status": 404, "msg": "error"}


@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.json
    if "type" in data:  # type is humidity or temperature
        sensor_data.post(data['type'], data['value'])
    return data


if __name__ == '__main__':
    app.run()
