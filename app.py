import flask
from predict_week import predict_week
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>RAIN</h1><p>This site is a prototype API for weather prediction distant reading of science fiction novels.</p>"

@app.route('/predict/week', methods=['GET'])
def week():
    return json.dumps(predict_week())
    

app.run()