from flask import Flask, jsonify
import random
import datetime

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/json', methods=['POST'])
def json():
    return jsonify(hello='world')


@app.route('/lotto', methods=['POST'])
def lotto():
    random_lotto = random.sample(range(1, 46), 6)
    random_lotto.sort()
    random_lotto = list(map(str, random_lotto))
    random_num = ','.join(random_lotto)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": random_num + " 행운을 빌어요"
                    }
                }
            ]
        }
    }

    return jsonify(response)


@app.route('/time', methods=['POST'])
def time_now():
    now = datetime.datetime.now()

    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "현재 시간은 " + nowDatetime
                    }
                }
            ]
        }
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
