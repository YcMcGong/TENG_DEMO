import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn import svm
import pickle
"""
This is the main program to train the CNN

"""
#Define values
path = './Training_Data/'
n_class = 2
batch_size = 432#90*4
number_of_epoch = 90
subject_list = ['double_tap','long_blow']
final_layer_size = 100

def window_avg(data, resolution):
    output = []
    length = len(data)
    gap = int(length/resolution)
    for i in range(resolution):
        output.append(max(data[i*gap:(i+1)*gap-1]))
    return output
            
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

def Data_Import(path):
    data = []
    labels = []
    label_number = 0
    for subject in subject_list:
        with open (path + subject, 'rb') as fp:
            itemlist = pickle.load(fp)
        labelslist = np.ones(len(itemlist),dtype=int)*label_number
        data.extend(itemlist)
        labels.extend(labelslist)
        label_number = label_number + 1
    # data = np.log(np.add(data,0.01))
    data = np.log(np.subtract(data,2))
    data[np.isnan(data)] = 0
    data_train, data_test, label_train, label_test = train_test_split(data, labels, test_size=0.05)
    return data_train, data_test, label_train, label_test

# Reading Data
np.seterr(all='ignore') #disable warning
# data_train, data_test, label_train, label_test = Data_Import(path)
data_train, data_test, label_train, label_test = Data_Import(path)
# plt.plot(data[190])
# plt.show()
data_train_features = []
data_test_features = []
number_of_feature = 3

for i in range(len(data_train)):
    data_train_features.append(get_peak_number(data_train[i],number_of_feature))

for i in range(len(data_test)):
    data_test_features.append(get_peak_number(data_test[i],number_of_feature))

data_train = np.reshape(data_train_features,(-1,number_of_feature))
data_test = np.reshape(data_test_features,(-1,number_of_feature))
clf = svm.SVC()
clf.fit(data_train, label_train)
print(clf.score(data_test,label_test))

with open('SVC.pkl', 'wb') as f:
    pickle.dump(clf, f)