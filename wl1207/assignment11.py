import sys
import numpy as np
from investment_simulation import investmentSimulation
from write_result import writeRes
from simulation_plot import simulationPlot
from exception_class import invalidInputFormat, writeInTextException, saveInPdfException

def main():
	
	"""In the main function, we will first receive input positions and num_trials from the user.
	   We will write the result into a text file and save histogram into pdf file.
	   If there is any invalid format or cannot open the text file or pdf file, the program will raise exception.
	"""
	
	while True:
		
		"""
		Receive input from user. If the parameters are not given in a valid format, it will raise exception later. 
		For example, input_positions is only allowed in format like '[1,2,3,4,5]',
		either '(1,2,3,4,5]' or '(1,2,3,4,5)' will raise exception.
		And input_num_trials should be a positive number. If a negative received, we would use its absolute value.
		"""
		
		try:
			input_positions = raw_input('Give a list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]? Input quit to exit. \n')
			input_num_trials = raw_input('How many times you want to randomly repeat the test? Input quit to exit. \n')
		except(KeyboardInterrupt,EOFError):
			print 'Program exit. '
			sys.exit()
		
		if (input_positions == 'quit' or input_num_trials == 'quit'):
			print 'Program exit.'
			sys.exit()
		
		try:
			positions = [np.abs(int(x)) for x in input_positions.strip('[]').split(',')]
			num_trials = np.abs(int(input_num_trials))
		except:
			raise invalidInputFormat('Please input in given format. ')
		
		
		try:
			print 'Write result into a text file.'
			try:
				writeRes(positions, num_trials)
			except:
				raise writeInTextException('Fail to write in a text file. Please check. ')
			
			print 'Plot and save in pdf.'
			try:
				for position in positions:
					simulationPlot(position, num_trials)
			except:
				raise saveInPdfException('Fail to save in a pdf. Please check. ')
				
		except(KeyboardInterrupt,EOFError):
			print "Program exit."
			sys.exit()
				
		
if __name__ == "__main__":
	main()