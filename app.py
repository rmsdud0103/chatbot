# -*- encoding: utf-8 -*-

import requests
from flask import Flask, request, jsonify, json, make_response

app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello~'

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    req=request.get_json(silent=True, force=True)
    try:
        action= req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'
    
    if action =='screen':
        res= {'fulfillmentText': 'ActiveX 가 정상적으로 설치 또는 등록되지 않았습니다. 설치 여부 및 재설치를 하시기를 바랍니다.'}
    elif action =='reportviewer':
        res= {'fulfillmentText': 'dll 파일이 존재하는 경우에 발생하여 오류 대화상자의 메시지에 파일명을 확인하고 대응하시기 바랍니다.'}
    else:
        res= {'fulfillmentText': '무슨말인지 잘 모르겠어요 '}
    return make_response(jsonify(res))

if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)