from flask import Flask, Response, jsonify
import json
import os
import time
import requests


import middleware
from zipfile import ZipFile

api_key     = "6dce3d8c333806792bdc5074fd53d1ea"
city        = "granada"
language    = "ES"
lat = "37.18817"
lon = "-3.60667"
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&lang=%s" % (city,api_key,language)
# "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=37.18817&lon=-3.60667&dt=3&appid=6dce3d8c333806792bdc5074fd53d1ea"


app = Flask(__name__)
app.wsgi_app = middleware.LoggerMiddleware(app.wsgi_app)


@app.route("/servicio/v3/prediccion/test",methods=['GET'])
def test():
    response = Response("Test Api V3", status=200)
    response.headers['Content-Type']='application/json'
    return response

@app.route("/servicio/v3/prediccion/24horas",methods=['GET'])
def hours_24():
    response = requests.get(url)
    response = Response(json.dumps(json.loads(response.text)), status=200)
    #response = Response(json.dumps(predict_weather(24)), status=200)
    return response


@app.route("/servicio/v3/prediccion/48horas",methods=['GET'])
def hours_48():
    response = requests.get(url)
    response = Response(json.dumps(json.loads(response.text)), status=200)
    #response = Response(json.dumps(predict_weather(48)), status=200)
    return response

@app.route("/servicio/v3/prediccion/72horas",methods=['GET'])
def hours_72():
    response = requests.get(url)
    response = Response(json.dumps(json.loads(response.text)), status=200)
    #response = Response(json.dumps(predict_weather(72)), status=200)
    return response

@app.after_request
def after(response):
    response.headers['Content-Type']='application/json'
    return response