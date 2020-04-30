import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def collatz_sequence(an):
	if an % 2 == 0:
		next = an/2
	elif an % 2 == 1:
		next = 3*an+1
	#print(next)
	return next

def analysis(min_a0,max_a0):
	steps_to_termination=[]
	biggest=0
	for a0 in range(min_a0, max_a0):
		steps=0
		an = collatz_sequence(a0) #first an must be computed before loop
		while an != 1: #generates new 'an' until it is equal to 1: sequence terminates
			steps+=1 #counts the steps
			an = collatz_sequence(an)
			if an > biggest: #get the biggest an
				print(f'Neuer Maximaler Wert: {an} a_0: {a0} in Schritt: {steps}')
				biggest = an
			if steps > 10000: #to prevent infinite loop 
				#print(f'steps exceed 10000 for a0={a0} possible divergence')
				break
		#if steps < 10000:
			#print(f'a0 = {a0} termininated at {steps} steps')
		steps_to_termination.append(steps) #save how many steps were needed
	
	max_steps = max(steps_to_termination)
	a0_belongs_to_max_steps = steps_to_termination.index(max_steps)
	print(f'a0={a0_belongs_to_max_steps} took the most steps with {max_steps} steps!')
	print(f'biggest value of an at any point was {biggest}')

	return steps_to_termination

def main():
	print('a)')
	steps_to_termination = analysis(1,5000)
	
	plt.figure(1)
	plt.plot(np.arange(1, 5000, 1), steps_to_termination) #plots how many steps were needed to terminate
	plt.title('a0 in [1,5000]')
	plt.xlabel('a0')
	plt.ylabel('steps before termination')
	
	print('b)')
	steps_to_termination = analysis(-4999, 0)

	plt.figure(2)
	plt.plot(np.arange(-4999, 0, 1), steps_to_termination) #plots how many steps were needed to terminate
	plt.title('a0 in [-4999,-1]')
	plt.xlabel('a0')
	plt.ylabel('steps before termination')
	plt.show()
	
if __name__ == '__main__':
	main()