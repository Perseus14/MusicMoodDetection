from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pickle

PKL_MODEL = '../models/mood_audio_features_py2.pkl'

Moods = ['Peaceful','Upbeat','Happy','Tender','Romantic','Sensual','Energizing','Chill','Cool','Heartbreaking','Aggressive','Sad']
#Moods = ['Peaceful','Upbeat','Romantic','Sad']
Colors = ['#add8e6','#ff6600','#ffff00','#8080ff','#9932CC','#ff99ff','#ffa500','#4a708b','#49a19a','#191970','#ff0000','#808080']

mood_features = pickle.load(open(PKL_MODEL,'rb'))

fig = plt.figure()
ax = plt.axes(projection='3d')

for mood_id in range(len(Moods)):
	values = mood_features[Moods[mood_id]]
	dance_line = [val[0] for val in values]
	energy_line = [val[1] for val in values]
	valence_line = [val[2] for val in values]
	ax.scatter3D(dance_line, energy_line, valence_line, c=Colors[mood_id])

ax.set_xlabel('Danceability')
ax.set_ylabel('Energy Level')
ax.set_zlabel('Valence Level')

fig.savefig('3dplot.png')
fig.show()
