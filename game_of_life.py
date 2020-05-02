"""
implementation of the game of life
"""
import numpy as np
import random as r
import time as t

def check_surroundings(pos, array):
	"""
	checks how many of the eight surrounding fields in an array to a given
	position pos contain the value '1'

	"""
	counter = 0
	x_pos = pos[0]
	y_pos = pos[1]
	for i in [-1, 0, 1]:
		if array[x_pos+1][y_pos+i] == 'X':
			counter += 1
	for i in [-1, 0, 1]:
		if array[x_pos-1][y_pos+i] == 'X':
			counter += 1
	for i in [-1, 1]:
		if array[x_pos][y_pos+i] == 'X':
			counter += 1
	return counter

def alive(pos, array):
	"""
	checks if a cell in an array is 'alive' that means that the value is
	'X'
	array: array containing values
	pos: tupel with x and y position inside array 
	"""
	x = pos[0]
	y = pos[1]
	if array[x][y] == 'X':
		return True
	else:
		return False

def all_dead(Game_Of_Life):
	x_dim = Game_Of_Life.x_dim
	y_dim = Game_Of_Life.y_dim
	board = Game_Of_Life.board
	for x in range(x_dim):
		for y in range(y_dim):
			if board[x][y] == 'X':
				return False
	return True

class Game_Of_Life():
	"""
	this class is the main program it contains the board and a function
	which can update the board
	"""
	def __init__(self, x_dim, y_dim):
		"""
		initializes the board with random values like 'X' (alive) or
		' ' (dead) 
		x_dim and y_dim specifies the dimensions of the board.
		"""
		self.x_dim = x_dim
		self.y_dim = y_dim
		self.board = np.zeros([x_dim+2, y_dim+2], dtype=object) # to prevent boundary errors array[-1]
		self.print_board = np.empty([x_dim+2, y_dim+2])
		for y in range(y_dim+2): 
			for x in range(x_dim+2):
				if x == 0 or y == 0 or x == x_dim+1 or y == y_dim+1:
					self.board[x][y] = '.' # . for boarder
				else:
					self.board[x][y] = r.choices([' ','X'], [0.9, 0.1])[0]
					#random start values with propabilties
					#choices returns a list therefore [0] is needed

	def move(self):
		"""
		this function implements the 3 rules of the game:
			1. Each living cell with less than two living neighbors
			   dies.
			2. Each living cell with more than four living neighbors
			   dies.
			3. Each dead cell with exactly three living neighbors
			   becomes alive by reproduction.
		"""
		for y in range(1, self.y_dim+1): 
			for x in range(1, self.x_dim+1):
				population = check_surroundings((x,y), self.board)
				if alive((x,y), self.board) and population < 2:
					self.board[x][y] = ' ' #cell dies
				if alive((x,y), self.board) and population > 4:
					self.board[x][y] = ' '
				if alive((x,y), self.board) is False and population == 3:
					self.board[x][y] = 'X'

def main():
	"""
	initializes and runs a 'game of life' and animates the process in 
	the terminal.
	"""
	np.set_printoptions(linewidth=160) # for proper printing to terminal
	
	test = Game_Of_Life(20, 20)
	
	for steps in range(30):
		print(chr(27) + "[2J") # cleares the terminal window
		print(test.board)
		t.sleep(1)
		test.move()
		if all_dead(test):
			break

main()











