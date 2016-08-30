from matplotlib import pyplot as plt 
from sklearn.datasets import load_iris
import numpy as np

# load the data with load_iris
data = load_iris()
print type(data)
features = data['data']
feature_names = data['feature_names']
target = data['target']

for t, marker, c in zip(xrange(3), ">ox", "rgb"): 
	#plot each class with different colored markers
	plt.scatter(features[target == t,0], 
							features[target == t, 1], 
							marker = marker, 
							c = c) 
	plt.show()
	
	# first classifier