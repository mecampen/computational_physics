"""
implementation of a turing machine blueprint so it is easy to implement
a specific turing machine and test it out.
m symbols to write on the tape
n+1 internal states of the head
"""

class Turing_Machine():
	def __init__(self, init_head_state = 'A', tape=[0,0,0], head_pos=1):
		self.tape = tape
		self.head_state = init_head_state
		self.head_pos = head_pos
		self.head_pos_tape = tape.copy() # for display purposes only
		self.head_pos_tape[head_pos] = init_head_state

	def move_head_right(self):
		"""
		moves the head to the right on the tape.
		Optionally adds another list item if head would come close to
		end. 
		"""
		if len(self.tape) <= self.head_pos+2:
			self.tape.append(0)
			self.head_pos_tape.append(0)
		self.head_pos += 1
		self.head_pos_tape[self.head_pos] = self.head_state # move the head on the tape
		self.head_pos_tape[self.head_pos-1] = 0 # deletes old head position
	
	def move_head_left(self):
		"""
		moves the head to the left on the tape.
		Optionally adds another list item if head would come close to
		end. 
		"""
		if self.head_pos-2 <= 0:
			self.tape.insert(0,0) #to prevent reaching left end
			self.head_pos_tape.insert(0,0)
			self.head_pos_tape[self.head_pos] = 0
			self.head_pos += 1 # because new entry on left was created
		self.head_pos -= 1
		self.head_pos_tape[self.head_pos] = self.head_state # move the head on the tape
		self.head_pos_tape[self.head_pos+1] = 0 # deletes old head position

	def update_head_state(self, new_state):
		self.head_state = new_state
		self.head_pos_tape[self.head_pos] = new_state

	def write(self, symbol):
		self.tape[self.head_pos] = symbol

	
	def print_machine(self):
		print('----------------------------------------------------------------')
		print(f'head position: {self.head_pos_tape}')
		print(f'tape         : {self.tape}')
		print('----------------------------------------------------------------')


def example_machine():
	"""
	implementation of a simple turing machine following this schema:
	
	   | A   | B 
	_______________
	0  | 1LB | 1RA
	_______________
	1  | 0LB | 1RHALT
	The machine terminates if the heads assumes the state HALT
	"""
	example_machine = Turing_Machine(init_head_state='A')
	example_machine.print_machine()
	steps = 0

	while example_machine.head_state is not 'HALT':
		if example_machine.head_state is 'A':
			if example_machine.tape[example_machine.head_pos] == 0:
				example_machine.write(1)
				example_machine.move_head_left()
				example_machine.update_head_state('B')
				example_machine.print_machine()
				steps += 1
				continue
			if example_machine.tape[example_machine.head_pos] == 1:
				example_machine.write(1)
				example_machine.move_head_right()
				example_machine.update_head_state('A')
				example_machine.print_machine()
				steps += 1
				continue
		if example_machine.head_state is 'B':
			if example_machine.tape[example_machine.head_pos] == 0:
				example_machine.write(1)
				example_machine.move_head_right()
				example_machine.update_head_state('A')
				example_machine.print_machine()
				steps += 1
				continue
			if example_machine.tape[example_machine.head_pos] == 1:
				example_machine.write(1)
				example_machine.move_head_right()
				example_machine.update_head_state('HALT')
				example_machine.print_machine()
				steps += 1
				continue
	print(f'machine terminated after {steps} steps')

example_machine()
