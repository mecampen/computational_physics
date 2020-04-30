import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def collatz_sequence(an):
	"""
	the function computes the next term of the collatz sequence given a 
	last term as arguement.
	an: start value or last value of the sequence 
	"""
	if an % 2 == 0:
		next = an/2
	elif an % 2 == 1:
		next = 3*an+1
	#print(next)
	return next

def analysis(min_a0,max_a0):
	"""
	the analysis function examines the behaviour of the collatz sequence
	for different starting values. The Steps needed for termination are 
	saved in an array 'steps_to_termination'. 
	If the number of steps exceeds 10000 steps it is assumed that the 
	sequence does not terminate. The maximal value the sequence reached 
	at any point, the biggest number of steps and which start value
	belongs to that is printed to the terminal.
	Finally the array 'steps_to_termination' is returned in the end.
	
	min_a0: the smallest start value to be examined
	max_a0: the biggest start value to be examined
	"""
	steps_to_termination=[]
	biggest=0
	for a0 in range(min_a0, max_a0):
		steps=0
		an = collatz_sequence(a0) #first an must be computed before loop
		while an != 1: #generates new 'an' until it is equal to 1: sequence terminates
			steps+=1 #counts the steps
			an = collatz_sequence(an)
			if an > biggest: #get the biggest an
				biggest = an
			if steps > 10000: #to prevent infinite loop 
				break
		steps_to_termination.append(steps) #save how many steps were needed
	
	max_steps = max(steps_to_termination)
	a0_belongs_to_max_steps = steps_to_termination.index(max_steps)
	print(f'a0={a0_belongs_to_max_steps} took the most steps with {max_steps} steps!')
	print(f'biggest value of an at any point was {biggest}')

	return steps_to_termination

def main():
	"""
	In this function the analysis function is run and the outcome is 
	portrayed with a Plot utilizing matplotlib.
	The analyis is run for positive start values until 5000. Also it 
	is run for negative start numbers from -4999 to -1.
	"""
	print('a)')
	steps_to_termination = analysis(1,5000)
	
	plt.figure(1)
	plt.plot(np.arange(1, 5000, 1), steps_to_termination)
	#plots how many steps were needed to terminate
	plt.title('a0 in [1,5000]')
	plt.xlabel('a0')
	plt.ylabel('steps before termination')
	
	print('b)')
	steps_to_termination = analysis(-4999, 0)

	plt.figure(2)
	plt.plot(np.arange(-4999, 0, 1), steps_to_termination)
	#plots how many steps were needed to terminate
	plt.title('a0 in [-4999,-1]')
	plt.xlabel('a0')
	plt.ylabel('steps before termination')
	plt.show()
	
if __name__ == '__main__':
	main()