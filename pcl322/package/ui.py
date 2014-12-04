import sys
import os
from utility import *
from exception import *

#Read number of trials from user
def read_number_of_trials():

	while True:
		try:
			#Read from standard input
			num_trials = raw_input("Please enter the number of trials ")
			#Check if valid, if not, an err will be raised
			valid_int(num_trials)
			break
		#Input not a integer
		except IntegerErr as err:
			print err
		#Interrupt involved
		except KeyboardInterrupt:
			terminate()

	return int(num_trials)


#Read position from user
def read_position():

	while True:
		try:
			#Read from standard input
			position = raw_input(\
			"Please enter the list of the number of shares (e.g. [1,10,100,1000]) "\
			).replace(" ", "")
			#Check if valid, if not, an err will be raised
			valid_position(position)
			break
		#input not in the right format
		except PositionErr as err:
			print err
		#Interrupt involved
		except KeyboardInterrupt:
			terminate()
			
	return init_position(position)

