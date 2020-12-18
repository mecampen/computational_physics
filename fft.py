"""
"""
import numpy as np
import matplotlib.pyplot as plt


omega = lambda p, q: np.exp((2.0 * np.pi * 1j * q) / p)

def fft(x):
   n = len(x)
   if n == 1:
      return x
   else:
      Feven = fft([x[i] for i in range(0, n, 2)])
      Fodd = fft([x[i] for i in range(1, n, 2)])
 
      combined = [0] * n
      for m in range(int(n/2)):
         combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
         combined[m + int(n/2)] = Feven[m] - omega(n, -m) * Fodd[m]
 
      return combined

def main():
	N = 128
	X = [0, 1]
	delta = (X[1]-X[0]) / N

	f_a = lambda x: np.sin(2*np.pi*x)
	f_b = lambda x: 1
	f_c = lambda x: np.exp(-(x-(1/2))**2)
	f_d = lambda x: x
	
	favec = [f_a(X[0] + j*delta) for j in range(N)]
	fbvec = [f_b(X[0] + j*delta) for j in range(N)]
	fcvec = [f_c(X[0] + j*delta) for j in range(N)]
	fdvec = [f_d(X[0] + j*delta) for j in range(N)]

	F_a = fft(favec)
	F_b = fft(fbvec)
	F_c = fft(fcvec)
	F_d = fft(fdvec)

	#plot
	X_domain = np.linspace(X[0], X[1], N)
	plt.figure(1)
	plt.plot(X_domain, F_a)
	plt.figure(2)
	plt.plot(X_domain, F_b)
	plt.figure(3)
	plt.plot(X_domain, F_c)
	plt.figure(4)
	plt.plot(X_domain, F_d)
	plt.show()
	
if __name__ == '__main__':
	main()