#!flask/bin/python
import random

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/pm10pm2p5', methods=['GET'])
def get_pms():
    pm10 = '{"pm10":['
    pm2p5 = ',"pm2p5":['

    for i in range(10):
        pm10 += str(random.randint(0, 50)) + ','
        pm2p5 += str(random.randint(0, 50)) + ','

    pm10 += str(random.randint(0, 50)) + ']'
    pm2p5 += str(random.randint(0, 50)) + ']}'

    json_pm = pm10 + pm2p5
    print(json_pm)
    return json_pm


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def launch_backend():
    app.run(debug=True, host='0.0.0.0', port=8081)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
