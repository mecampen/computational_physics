import math as m
import numpy as np
import matplotlib.pyplot as plt

def faculty(N):
	"""
	this function calculates and returns the falculty for argument N
	"""
	res = 1
	for n in range(N):
		res *= (n + 1)
	return res

def sin_series(x,N):
	"""
	compute the value of sinus using its series.
	x: the argument of sin(x)
	N: how many terms of the series should be computed
	"""
	res = x #value of the first term of the series
	for n in range(1,N+1):
		res = res + (-1)**n/faculty(2*n+1)*x**(2*n+1)
	return res

def log_series(x,N):
	"""
	compute the value of the logarithm using its series.
	x: the argument of log(x)
	N: how many terms of the series should be computed
	"""
	res = x-1 #value of the first term of the series
	for n in range(2,N+1):
		res = res + (-1)**(n+1)/n*(x-1)**n
	return res

def main():
	"""
	the difference between the series value and the exact value 
	according to math module are compared for different numbers of 
	terms N. This change of error is portrayed using matplotlib.
	"""
	x=1
	error=[]
	N_values= np.arange(1,9)
	for N in range(1,9):
		error.append(abs(sin_series(x,N)-m.sin(x)))
	plt.figure(1)
	plt.plot(N_values, error) 
	plt.title('a) absolut error of sinus series after N terms (x=1)')
	plt.xlabel('N')
	plt.ylabel('absolut error')

	x=3/2
	error=[]
	for N in range(1,9):
		error.append(abs(log_series(x,N)-m.log(x)))
	x_values= np.arange(1,9)
	plt.figure(2)
	plt.plot(N_values, error)
	plt.title('b) absolut error of log series after N terms (x=3/2)')
	plt.xlabel('N')
	plt.ylabel('absolut error')

	x=3
	error=[]
	for N in range(1,9):
		error.append(abs(log_series(x,N)-m.log(x)))
	x_values= np.arange(1,9)
	plt.figure(3)
	plt.plot(N_values, error)
	plt.title('b) absolut error of log series after N terms (x=3)')
	plt.xlabel('N')
	plt.ylabel('absolut error')
	plt.show()


if __name__ == '__main__':
	main()