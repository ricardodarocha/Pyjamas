import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#fitting function
def func(x, a, b):
    return a*np.exp(b*x)

xData = np.array([1,2,3,4,5])
yData = np.array([1,9,50,200,1200])

popt, pcov = curve_fit(func, xData, yData)
a, b = popt
print(popt)

yCurve = func(xData, a,b)
print(yCurve)

plt.plot(xData, yData, 'bo', label='experiment')
plt.plot(xData, yCurve, 'r.', label='fit')
plt.show()