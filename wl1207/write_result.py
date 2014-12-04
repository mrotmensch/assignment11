import numpy as np
from investment_simulation import investmentSimulation

def writeRes(positions, num_trials):
	
	"""
	This function will write results produced in investmentSimulation function into a text file.
	"""
	
	results = open('results.txt','w')
	
	for position in positions:
	
		daily_ret = investmentSimulation(position,num_trials)
		mean = np.mean(daily_ret)
		std = np.std(daily_ret)
		results.write('{}	mean:{},std:{} \n'.format(position,mean,std))
	
	results.close()