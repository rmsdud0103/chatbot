# -*- encoding: utf-8 -*-

import requests
import pandas as pd
from flask import Flask, request, jsonify, json, make_response, render_template

df = pd.read_excel('ERS.xlsx', sheet_name='Sheet1')    #엑셀 시트 데이터를 읽고 df에 저장
df2 = pd.read_excel('ERS.xlsx', sheet_name='Sheet2')    

app = Flask(__name__)
def ERS_00(parameter):
    row = df[df['에러코드'].isin([parameter])]    #parameter와 일치하는 행 데이터로 추출
    data = row.to_dict('split')                    #dataframe을 dictonary로 변환
    res1= "에러코드명은 "+data['data'][0][0]+" 입니다."    #각 데이터별 응답 
    res2= "메세지 : "+data['data'][0][1]
    res3= "설명 : "+data['data'][0][2]
    res4= "조치사항 : "+data['data'][0][3]
    res = {
        'fulfillmentMessages': [{
            'text': {'text': [res1]}},{
            'text': {'text': [res2]}},{
            'text': {'text': [res3]}},{
            'text': {'text': [res4]}
        }]}    #dialogflow webhook response api 코드에 해당
    return res
def ERS_01(parameter):
    row = df2[df2['에러코드'].isin([parameter])]    #parameter와 일치하는 행 데이터로 추출
    data = row.to_dict('split')                    #dataframe을 dictonary로 변환
    res1= "에러코드명은 "+data['data'][0][0]+" 입니다."    #각 데이터별 응답 
    res2= "메세지 : "+data['data'][0][1]
    res3= "설명 : "+data['data'][0][2]
    res4= "조치사항 : "+data['data'][0][3]
    res = {
        'fulfillmentMessages': [{
            'text': {'text': [res1]}},{
            'text': {'text': [res2]}},{
            'text': {'text': [res3]}},{
            'text': {'text': [res4]}
        }]}    #dialogflow webhook response api 코드에 해당
    return res

@app.route('/')
def home():
    return 'hello'
@app.route('/test')
def test():
    return render_template('test.html')
    
@app.route('/image', methods=['GET','POST'])
def img():
    return render_template('img.html')

@app.route('/webhook', methods=['GET','POST'])    #dialogflow webhook
def webhook():
    req=request.get_json(silent=True, force=True)
    try:
        action= req.get('queryResult').get('action')        
        parameter= req.get('queryResult').get('parameters').get('ERS_00')
        parameter2= req.get('queryResult').get('parameters').get('ERS_01')
    except AttributeError:
        return 'json error'
    if action == 'ERS00':
        res = ERS_00(parameter)
    elif action == 'ERS01':
        res = ERS_01(parameter2)
    else:
        res = '에러코드를 정확하게 입력해주세요'
        
    return make_response(jsonify(res))
    
if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)