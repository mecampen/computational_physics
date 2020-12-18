import numpy as np
import matplotlib.pyplot as plt
from fft import fft

def lp_filter(Fx, w1):
	"""
	low pass filter. All values above w1 get removed
	Fx: Array of values (optained by FT)
	w1: determines the magnitude of filtered values
	"""
	N = len(Fx)
	for n in range(N):
		if Fx[n]>w1:
			Fx[n] = 0
	return Fx

def hp_filter(Fx, w0):
	"""
	high pass filter. All values below w0 get removed
	Fx: Array of values (optained by FT)
	w0: determines the magnitude of filtered values
	"""
	N = len(Fx)
	for n in range(N):
		if Fx[n]<w0:
			Fx[n] = 0
	return Fx

def bp_filter(Fx, w0, w1):
	"""
	high pass filter. All values below w0 get removed
	Fx: Array of values (optained by FT)
	w0: determines the magnitude of filtered values
	w1: determines the magnitude of filtered values
	"""
	N = len(Fx)
	for n in range(N):
		if Fx[n]<w0 or Fx[n]>w1:
			Fx[n] = 0
	return Fx

def main():
	X = [-2, 2]
	N = 128
	w1 = 10
	w0 = 1

	f = lambda x: 1 if abs(x)<1 else 0
	xdom = np.linspace(X[0], X[1], N)
	fx = [f(x) for x in xdom]

	Fx = fft(fx)
	Fx = lp_filter(Fx, w1)
	fxa = 1/N*np.array(fft(Fx))
	
	Fx = fft(fx)
	Fx = hp_filter(Fx, w0)
	fxb = 1/N*np.array(fft(Fx))
	
	Fx = fft(fx)
	Fx = bp_filter(Fx, w0, w1)
	fxc = 1/N*np.array(fft(Fx))

	#plot
	plt.plot(xdom, fxc)
	plt.show()

if __name__ == '__main__':
	main()