from package.utility import *
from package.simulation import *
from package.exception import *
from package.io import *
from package.ui import *
from package.plot import *

if __name__ == "__main__":

	#Read the inputs from the user
	num_trials = read_number_of_trials()
	position = read_position()

	#Run simulation
	daily_ret =  investment(position, num_trials)

	#Calculate mean and std
	statsDataFrame =  stats_results(position, daily_ret)

	#Write results.txt
	if output_to_file(statsDataFrame, "results.txt") == False:
		terminate()

	#Plot
	plot_for_results(daily_ret, position)

	#Done
	print "Successfully completed"

