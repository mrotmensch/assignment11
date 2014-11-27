import sys
import os
import numpy as np

#Simulation
def investment(position, num_trials):
	#Initialize a dictionary for return value
	result = {}
	#for each position do the simulation of investment
	for pos in position:

		position_value = 1000 / pos

		cumu_ret = []
		for i in range(num_trials):
			#Randomly generate the outcomes of the series of investment which is
			#either zero with prob=.49 or doubled with prob=.51,
			#and then sum them up 
			cumu_ret.append(np.sum(np.random.choice([0, 2*position_value], \
				pos, p=[0.49, 0.51])))
		#Normalize
		result[pos] = np.array(cumu_ret)/1000.0 - 1

	return result


