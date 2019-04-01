from flask import Flask, jsonify
from predict_week import predict_week
from threading import Thread
from json import loads, dumps
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>RAIN</h1><p>This site is a prototype API for weather prediction.</p>"


@app.route('/predict/week', methods=['GET'])
def week():
    def do_work():
        json_obj = loads(dumps(predict_week()))
        url = 'http://sofe3720.ml/predictions'
        headers = {'content-type': 'application/json'}
        # print(dumps(json_obj))
        resp = requests.post(url, data=dumps(json_obj), headers=headers)
        print(resp.text)

    thread = Thread(target=do_work)
    thread.start()
    # return flask.jsonify({'data': predict_week()})
    return jsonify({'status': 200, 'message': 'We out here!'})


app.run()
