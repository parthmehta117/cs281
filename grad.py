
from scipy import stats
import numpy as np
import random
import matplotlib.pyplot as plt
import plotly.plotly as py


# Init different epsilon values  
epsilon2 = 4 
epsilon3 = 3 
epsilon4 = 2
epsilon5 = 0.5


# Problem 1 
def f(x):
	return np.cos(x) + x**2 + np.exp(x)

# Problem 2
def grad_f(x):
	return -np.sin(x) + 2*x + np.exp(x)

# Problem 3
def grad_check(x,epsilon):
	def f_plus(x, eps):
		return np.cos(x + eps) + (x+ eps)**2 + np.exp(x+ eps)
	return (f_plus(x,epsilon) - f_plus(x,-epsilon))/(2*epsilon)


fig = plt.figure()
ax1 = fig.add_subplot(111)

##Init Y axis arrays
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

# Generate equally spaced points on X axis
x = np.linspace(-2, 10.0, num=100)

# Input function results 
for i in range(100):
	y1.append(grad_f(x[i]))
	y2.append(grad_check(x[i],epsilon2))
	y3.append(grad_check(x[i],epsilon3))
	y4.append(grad_check(x[i],epsilon4))
	y5.append(grad_check(x[i],epsilon5))
	i += 1


# Plot all approximations 
ax1.scatter(x,y1,color='green',s=20,edgecolor='none')
ax1.scatter(x,y2,color='red',s=5,edgecolor='none')
ax1.scatter(x,y3,color='red',s=10,edgecolor='none')
ax1.scatter(x,y4,color='red',s=15,edgecolor='none')
ax1.scatter(x,y5,color='red',s=20,edgecolor='none')
ax1.set_ylim([-2,10])
ax1.set_xlim([-2,2])
plt.show()

