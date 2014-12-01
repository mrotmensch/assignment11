import sys
from investment_simulation import investmentSimulation
from write_result import writeRes
from simulation_plot import simulationPlot

def main():
	
	"""In the main function, we will first receive input positions and num_trials from the user.
	   We will write the result into a text file and save histogram into pdf file.
	   If there is any invalid format or cannot open the text file or pdf file, the program will raise exception.
	"""
	while True:
		try:
			input_positions = raw_input('Give a list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]? Input quit to exit. \n')
			input_num_trials = raw_input('How many times you want to randomly repeat the test? Input quit to exit. \n')
		except(KeyboardInterrupt,EOFError):
			print 'Process exit.'
			sys.exit()
			
		if (input_positions == 'quit' or input_num_trials == 'quit'):
			print 'Program exit.'
			sys.exit()
		
		try:
			positions = [int(x) for x in input_positions.strip('[]]').split(',')]
			num_trials = int(input_num_trials)
		
			print 'Write result into a text file.'
			writeRes(positions, num_trials)
			
			print 'Plot and save in pdf.'
			for position in positions:
				simulationPlot(position, num_trials)
				
		except(KeyboardInterrupt,EOFError):
			print "Program exit."
			sys.exit()
				
		
if __name__ == "__main__":
	main()