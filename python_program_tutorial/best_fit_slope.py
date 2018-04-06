from statistics import mean 
import numpy as np
import matplotlib.pyplot as plt 
 

def best_fit_slope(xs,ys):
	m = ((mean(xs)*mean(ys)) - mean(xs*ys)) / ((mean(xs)**2) - mean(xs*xs))
	b = mean(ys) - m * mean(xs)
	return m, b

def squared_error(ys_orig, ys_line):
	return sum((ys_line - ys_orig)*(ys_line - ys_orig))

def coefficient_of_determination(ys_orig,ys_line):
	y_mean_line = [mean(ys_orig) for y in ys_orig]
	squared_error_regr = squared_error(ys_orig, ys_line)
	squared_error_y_mean = squared_error(ys_orig,y_mean_line)
	return 1 - (squared_error_regr/squared_error_y_mean)


xs =np.array([1,2,3,4,5], dtype = np.float64)
ys =  np.array([5,4,6,5,6], dtype = np.float64)
m, b = best_fit_slope(xs,ys)
regression_line = [(m*x)+b for x in xs]

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

predict_x = 7 
predict_y = (m*predict_x)+b

#print(predict_y)

#print (m, b) 
plt.scatter(xs,ys,color = '#003F72')
plt.plot(xs,regression_line)
plt.show()


