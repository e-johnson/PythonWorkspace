from matplotlib import pyplot as plt 
from sklearn.datasets import load_iris
import numpy as np 

data = load_iris() 
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target]
plength = features[:,2]
#use numpy operations to get setosa features
is_setosa = (target == 0) 

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print ('Maximum of setosa: {0}.'.format(max_setosa))
print ('Minimum of others: {0}. '.format(min_non_setosa))

#if features[:,2] < 2: print 'Iris Setosa'
#else: print 'Iris Virginica or Iris Versicolour'

features_notsetosa = features[~is_setosa]
labels = labels[~is_setosa]
virginica = (labels == 'virginica') 

best_acc = -1.0
th = 0
for fi in xrange(features_notsetosa.shape[1]): 
	# Generate all possible threshold for this feature
	thresh = features_notsetosa[:, fi].copy()
	thresh.sort()
	#Test all thresholds
	for t in thresh: 
		pred = (features_notsetosa[:,fi] > t) 
		acc = (pred == virginica).mean()
		if acc > best_acc: 
			best_acc = acc
			best_fi = fi
			best_t = t 
			th = t
			
			
print "best acc %s" % best_acc

print "best threshold %s" % th
		

