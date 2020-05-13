"""
In this script Matplotlib is utilized to plot three functions:
	1) y = x
	2) y = exp(x)
	3) y = x! , x element N
all functions are mapped to x^x scale.
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

#define functions
first_function = lambda x: x

second_function = lambda x: m.exp(x)

third_function = lambda x: m.factorial(x)

#define function for scaling to x^x
map_to_xx_scale = lambda f, x: f**(1/x)

def main():
	#compute all x values
	x1 = np.arange(0.1, 10.1, 0.1)
	x2 = np.arange(0.1, 10.1, 0.1)
	x3 = np.arange(1, 11, 1)

	#compute all y values
	y1 = [map_to_xx_scale(first_function(x), x) for x in x1] 
	y2 = [map_to_xx_scale(second_function(x), x) for x in x2]
	y3 = [map_to_xx_scale(third_function(x), x) for x in x3]

	#create all plots
	plt.figure(1)
	plt.title('function 1')
	plt.xlabel('x')
	plt.ylabel('x^(1/x)')
	plt.plot(x1, y1)

	plt.figure(2)
	plt.title('function 2')
	plt.xlabel('x')
	plt.ylabel('exp(x)^(1/x)')
	plt.plot(x2, y2)

	plt.figure(3)
	plt.title('function 3')
	plt.xlabel('x')
	plt.ylabel('x!^(1/x)')
	plt.plot(x3, y3)
	
	plt.show()

if __name__ == '__main__':
	main()