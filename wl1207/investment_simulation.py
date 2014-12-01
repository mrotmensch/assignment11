import numpy as np
from exception_class import inValidInputException

def investmentSimulation(position, num_trials):
		
	"""
	In this function, we simulate the investment with the following properties:
	51% of the time win, and the value would double.
	49% of the time lose, and the value would be lost.
	We could either make a single $1000 investment, or 1000 $1 investments (or something between) by inputting 
	different position.
	   
	The function receives two integers: position and num_trials;
	and return a list of daily_ret.
	
	"""
	
	if not (isinstance(position,int) and isinstance(num_trials,int)):
		raise inValidInputException('Function receives inputs not in a valid format, please check again. ')
	
	invest = 1000
	cumu_ret = []
	daily_ret = []
	position_value = invest/position
	
	for trial in range(num_trials):
		
		isWin = np.random.uniform(size = position)>0.49 # In each trial, the possibility of winning is 51%. 
		cumu_ret.append(isWin.sum()*position_value*2)
		daily_ret.append((cumu_ret[trial]/1000.)-1)
	
	return daily_ret
	
