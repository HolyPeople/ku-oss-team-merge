from flask import Flask, request

app = Flask(__name__)


@app.route('/dialog')
def hello_world():
    data = request.json
    if "apiKey" in data:
        print(data["apiKey"])
        if data["apiKey"] == "Hello, World":  # TODO: replace api key to jwt(javascript wep token)
            if "message" in data:
                return data['message']
    return {"status": 404, "msg": "error"}


if __name__ == '__main__':
    app.run()
