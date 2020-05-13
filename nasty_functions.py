import matplotlib.pyplot as plt
import numpy as np
import math as m

func1 = lambda x: -m.log(m.sqrt(abs(m.sin(x))))
func2 = lambda x: m.exp(-1 / (x**10))

def main():
	x1 = np.arange(-10, 10, 0.1)
	y1 = [func1(x) for x in x1]

	x2 = np.arange(-1/2, 1/2, 0.01)
	y2 = [func2(x) for x in x2]

	plt.figure(1)
	plt.plot(x1, y1)
	plt.title('first function')
	
	plt.figure(2)
	plt.semilogy(x2, y2)
	plt.title('second function')

	plt.show()

if __name__ == '__main__':
	main()