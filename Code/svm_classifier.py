import sys, os
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
import pickle

PKL_MODEL = '../models/mood_audio_features_py2.pkl'

Moods = ['Peaceful','Upbeat','Happy','Tender','Romantic','Sensual','Energizing','Chill','Cool','Heartbreaking','Aggressive','Sad']
Colors = ['#add8e6','#ff6600','#ffff00','#8080ff','#9932CC','#ff99ff','#ffa500','#4a708b','#49a19a','#191970','#ff0000','#808080']

mood_features = pickle.load(open(PKL_MODEL,'rb'))

x_list = []
y_list = []
for mood_id in range(len(Moods)):
	x_list+=mood_features[Moods[mood_id]]
	y_list+=[mood_id]*len(mood_features[mood])

x,y = np.array(x_list), np.array(y_list)
X_train, X_test, y_train, y_test = train_test_split(x, labels, test_size = 0.2, random_state=0)

param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001, 0.00001, 10]}
 
# Make grid search classifier
clf_grid = GridSearchCV(svm.SVC(), param_grid, verbose=1)

# Train the classifier
clf_grid.fit(X_train, y_train)
clf_predictions = clf_grid.predict(X_test)

print("Accuracy: {}%".format(clf.score(X_test, y_test) * 100 ))

with open('../models/svm_classifier_py2.pkl','wb') as fin:	
	pickle.dump(clf_grid, fin, protocol=pickle.HIGHEST_PROTOCOL)
