# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request
import urllib, json
import requests
app = Flask (__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/analysis/sentiment", methods=['GET'])
def sentiment_analysis():
	title = request.args.get("t")
	hashtag = request.args.get("h")
	total_reviews = 0
	positive_reviews = 0
	negative_reviews = 0
	neutral_reviews = 0
	#JSON de la respuesta
	json_result = {}
	#Conectar con el microservicio del dataset
	url_review = urllib.urlopen("http://localhost:8081/db/reviews")
	#Leer los reviews recibidos
	json_review = url_review.read()
	#Convertir en json los reviews obtenidos
	review = json.loads(json_review)
	#Enviar a analizar los reviews del dataset al servicio de analisis de sentimiento y recibimos el resultado
	res = requests.post('http://localhost:8082/text/analysis', json=review)
	#Lo convertimos en un json
	result = json.loads(res.text) # Dataset analizado
	#Accedemos a los atributos del json
	total_reviews += int(result['total reviews'])
	positive_reviews += int(result['positive'])
	negative_reviews += int(result['negative'])
	neutral_reviews += int(result['neutral'])
	#Conectar con el microservicio de Twitter
	url_tweet = urllib.urlopen('http://localhost:8083/tweets?h='+hashtag)
	#Leer los tweets recibidos
	json_tweets = url_tweet.read()
	#Convertir en json los tweets obtenidos
	tweets = json.loads(json_tweets)
	#Enviar a analizar los tweets del json de twitter al servicio de analisis de sentimientos de twitter y recibimos el resultado
	res_tweets = requests.post('http://localhost:8082/text/analysis', json=tweets)
	#Lo convertimos en un json
	result_tweets = json.loads(res_tweets.text)
	# Accedemos a los valores del json
	total_reviews += int(result_tweets['total reviews'])
	positive_reviews += int(result_tweets['positive'])
	negative_reviews += int(result_tweets['negative'])
	neutral_reviews += int(result_tweets['neutral'])
	# Conectar con el microservicio de OMDB
	url_omdb = urllib.urlopen("http://localhost:8084/information?t=" + title)
	# Leer la respuesta de OMDB
	json_omdb = url_omdb.read()

	print json_omdb

	# Convertir en json la respuesta
	omdb = json.loads(json_omdb)
	json_result['positive'] = positive_reviews
	json_result['negative'] = negative_reviews
	json_result['total'] = total_reviews
	json_result['neutral'] = neutral_reviews
	json_result['omdb'] = omdb
	#regresamos una respuesta
	return render_template("status.html", result=json_result)
	

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8080))
	app.debug = True
	app.run(host='0.0.0.0', port=port)