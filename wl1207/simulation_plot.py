import matplotlib.pyplot as plt
from investment_simulation import investmentSimulation

def simulationPlot(position, num_trials):
	
	"""
	This function will plot simulation for given position and num_trials.
	"""
	
	daily_ret = investmentSimulation(position, num_trials)
	
	p = plt.figure()
	plt.hist(daily_ret,100,range=[-1,1],color = 'red')
	plt.title('Histogram of Daily Return with position {}'.format(position))
	plt.xlabel('daily return')
	p.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))
	p.clf()
