import pickle
import requests
import os, errno

PKL_MODEL = '../models/mood_model.pkl'

Moods = ['Peaceful','Upbeat','Happy','Tender','Romantic','Sensual','Energizing','Chill','Cool','Heartbreaking','Aggressive','Sad']

#A dictionary of mood and track_details, (a tuple containing name of track, list of artists, preview_url, image_url and popularity) which is already sorted by popularity
map_tracks_to_mood = pickle.load(open(PKL_MODEL,'rb'))

def make_dirs(directory):
	try:
		os.makedirs(directory)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

def store_media(url,name,MOOD_RES_FOLDER):
	resp = requests.get(url,stream=True)
	file_type = resp.headers['Content-Type'].split('/')[-1]
	if(resp.ok):		
		with open(os.path.join(MOOD_RES_FOLDER,name+'.'+file_type),'wb') as fin:
			fin.write(resp.content)	

def recommender(mood,n=5):
	track_details = map_tracks_to_mood[mood]
	track_len = len(track_details)
	n = min(n, track_len) 					#Check if n > no. of tracks, if yes return the entire contents
	ind = 0
	count = 0
	recommended_tracks = []
	
	#First fill with tracks that has preview_url, if not possible fill with ones without urls in descending order of popularity (already_sorted)
	while(count<n and ind<track_len):
		_,_,url,_,_ = track_details[ind]
		if(url):
			recommended_tracks.append(track_details[ind])
			count+=1
		ind+=1
		
	if(count!=n):
		ind = 0
		while(count<n and ind<track_len):
			_,_,url,_,_ = track_details[ind]
			if(not url):
				recommended_tracks.append(track_details[ind])
				count+=1
			ind+=1	
	return recommended_tracks

#Testing
RESULT_FOLDER = 'results'	
for mood in Moods:
	results = recommender(mood,100)

	MOOD_RES_FOLDER = os.path.join(RESULT_FOLDER,mood)
	make_dirs(MOOD_RES_FOLDER)
	
	for tracks in results:
		name = tracks[0]
		img_url = tracks[3]
		mp3_url = tracks[2]
		if(img_url):
			store_media(img_url,name,MOOD_RES_FOLDER)
		if(mp3_url):	
			store_media(mp3_url,name,MOOD_RES_FOLDER)
		
		
					
					 
