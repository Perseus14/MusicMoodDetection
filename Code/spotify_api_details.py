import json
import os
import pickle

#CLIENT_ID = 'd14ba39b349b4ac6a80b13395085d263'
#CLIENT_KEY = '3e650409792b4d6a9abacb5e10a706e0'
#REDIRECT_URI = 'localhost:3000'
#USERNAME = 'percy_coder_vlabs1'

Moods = ['Peaceful','Upbeat','Happy','Tender','Romantic','Sensual','Energizing','Chill','Cool','Heartbreaking','Aggressive','Sad']

spotify_playlists_id = {'Peaceful':'37i9dQZF1DX0x36cwEyOTG','Upbeat':'37i9dQZF1DWSf2RDTDayIx','Tender':'37i9dQZF1DXarebqD2nAVg','Romantic':'37i9dQZF1DX50QitC6Oqtn','Sensual':'37i9dQZF1DWVGy1YP1ojM5','Energizing':'37i9dQZF1DWT6anPZiHuxz','Cool':'37i9dQZF1DWUI1rlvkdQnb','Swagger':'37i9dQZF1DWSlw12ofHcMM','Aggressive':'37i9dQZF1DX4eRPd9frC1m','Happy':'37i9dQZF1DXdPec7aLTmlC','Sad':'37i9dQZF1DX7qK8ma5wgG1','Chill':'37i9dQZF1DX4WYpdgoIcn6','Heartbreaking':'37i9dQZF1DWXxauMBOQPxX'}

def download_playlist():
	for i in range(len(Moods)):
		command = 'curl -X "GET" "https://api.spotify.com/v1/playlists/'+spotify_playlists_id[Moods[i]] + '" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQD8hG5rHiR6AzWJda6Qh3ooNUXerFjwIO76QepeKT8r5q3Mjfc_UJfSGg0zVWnmlcd3Y2TMYCP8knc-CqQS52GfYakswBUe-l13GwKrZhveTCsFmVxX4NonsOdNLsbGlMwIXD19r_7JOE0_9llKQEsrPbWo6xnpAg" > out_'+Moods[i]
		os.system(command)
		#print Moods[i], command,'\n\n\n'	

#download_playlist()

map_tracks_to_mood = {}	
for mood in Moods:
	track_list_details = []
	with open('../Data/out_'+mood,'r') as fin:
		json_output = json.loads(fin.read())	
	
	track_list_json = json_output['tracks']['items']
	for track in track_list_json:
		artist_names = []
		name = track['track']['name']
		artists_json = track['track']['artists']
		preview_url = track['track']['preview_url']
		popularity = int(track['track']['popularity'])
		image_url = track['track']['album']['images'][0]['url']
		for artist in artists_json:
			artist_names.append(artist['name'])
		track_list_details.append((name,artist_names,preview_url,image_url,popularity))	
	track_list_details = sorted(track_list_details, key = lambda x: x[-1], reverse=True)
	map_tracks_to_mood[mood] = track_list_details	

with open('../models/mood_model_py2.pkl','wb') as fin:	
	pickle.dump(map_tracks_to_mood, fin, protocol=pickle.HIGHEST_PROTOCOL)	
