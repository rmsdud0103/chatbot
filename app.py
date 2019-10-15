from flask import Flask, request, jsonify
import sys
app = Flask(__name__)

@app.route('/sayhello', methods=['POST'])
def Hello():
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText":{
                    "text" : "안녕~"
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)