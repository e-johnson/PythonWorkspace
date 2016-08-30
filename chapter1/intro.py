import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("web_traffic.tsv", delimiter = "\t")

print (data[:10]) 
print (data.shape)

x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x,y)
plt.title("Web traffic over the last month") 
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' %w for w in range(10)])
plt.autoscale(tight = True) 
plt.grid()


fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f1 = sp.poly1d(fp1)
fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting

f2p = sp.polyfit(x,y,2)
f2 = sp.poly1d(f2p)


f3p = sp.polyfit(x,y,100)
f3 = sp.poly1d(f3p)
#print(error(f2, x, y))

plt.plot(fx, f1(fx), linewidth=4)
plt.plot(fx, f2(fx), linewidth=4)
plt.plot(fx, f3(fx), linewidth=4) 

plt.legend(["d=%i" % f1.order], loc="upper left")

plt.legend(["d=%i" % f2.order], loc="upper left")


plt.legend(["d=%i" % f3.order], loc="upper left")
plt.show()

