import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn import svm
import pickle

# Look up list to translate activity number from integer to the name of activity
activity_list = ['double_tap','long_blow']

# Load the trained model
with open('SVC.pkl', 'rb') as f:
    clf = pickle.load(f)

# Get features
def get_peak_number(sequence, number_of_feature):
    peak = max(np.abs(sequence))
    peak_detection_ratio = 0.5
    peak_detection_thres = peak * peak_detection_ratio
    step = int(len(sequence)/number_of_feature)
    features = []
    for i in range(number_of_feature):
        number_of_peak = sum((np.abs(sequence[i*step:(i+1)*step-1])>peak_detection_thres).astype(int))
        features.append(number_of_peak)     
    return features

# Look up name of activity
def dict_look_up(activity_number_int):
    return activity_list[activity_number_int]
    
# Classifier main function
def classify_data(data, number_of_feature):
    features = get_peak_number(data, number_of_feature)
    activity_number = clf.predict(features)

    return dict_look_up(activity_number)