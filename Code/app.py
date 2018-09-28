from __future__ import division
from flask import Flask, render_template, send_file, make_response, request, redirect, url_for
import numpy as np
import pandas as pd
import pickle
import music_recommender

app = Flask(__name__)

Moods = ['Peaceful','Upbeat','Happy','Tender','Romantic','Sensual','Cool','Energize','Chill','Aggressive','Heartbreak','Sad']


@app.route('/')
def my_form():
    return render_template("index.html", moods=Moods)

@app.route('/Peaceful', methods=['GET','POST'])
def Peaceful():
	tracks = music_recommender.recommender('Peaceful')
	return render_template("mood.html", mood='Peaceful', tracks = tracks)


@app.route('/Upbeat', methods=['GET','POST'])
def Upbeat():
	tracks = music_recommender.recommender('Upbeat')
	return render_template("mood.html", mood='Upbeat',  tracks = tracks)

@app.route('/Happy', methods=['GET','POST'])
def Happy():
	tracks = music_recommender.recommender('Happy')
	return render_template("mood.html", mood='Happy',  tracks = tracks)

@app.route('/Tender', methods=['GET','POST'])
def Tender():
	tracks = music_recommender.recommender('Tender')
	return render_template("mood.html", mood='Tender', tracks =  tracks)

@app.route('/Romantic', methods=['GET','POST'])
def Romantic():
	tracks = music_recommender.recommender('Romantic')
	return render_template("mood.html", mood='Romantic', tracks =  tracks)

@app.route('/Sensual', methods=['GET','POST'])
def Sensual():
	tracks = music_recommender.recommender('Sensual')
	return render_template("mood.html", mood='Sensual', tracks =  tracks)

@app.route('/Cool', methods=['GET','POST'])
def Cool():
	tracks = music_recommender.recommender('Cool')
	return render_template("mood.html", mood='Cool', tracks =  tracks)

@app.route('/Energize', methods=['GET','POST'])
def Energize():
	tracks = music_recommender.recommender('Energizing')
	return render_template("mood.html", mood='Energizing', tracks =  tracks)

@app.route('/Chill', methods=['GET','POST'])
def Chill():
	tracks = music_recommender.recommender('Chill')
	return render_template("mood.html", mood='Chill', tracks =  tracks)

@app.route('/Aggressive', methods=['GET','POST'])
def Aggressive():
	tracks = music_recommender.recommender('Aggressive')
	return render_template("mood.html", mood='Aggressive', tracks =  tracks)

@app.route('/Heartbreak', methods=['GET','POST'])
def Heartbreak():
	tracks = music_recommender.recommender('Heartbreaking')
	return render_template("mood.html", mood='Heartbreaking', tracks =  tracks)

@app.route('/Sad', methods=['GET','POST'])
def Sad():
	tracks = music_recommender.recommender('Sad')
	return render_template("mood.html", mood="Sad", tracks =  tracks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8890, debug=True)
