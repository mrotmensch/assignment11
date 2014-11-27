from exception import *
import sys
import os
import re
import numpy as np
import pandas as pd


#Check input is int
def valid_int(input):
	#The regular expression of integer
	if re.match(r"^\d+$", input) == None:
		raise IntegerErr("Invalid number of trials")
	#The number of trials must be greater than zero
	elif int(input) <= 0:
		raise IntegerErr("Number should be greater than zero")
	return True

#Check position is in the right format
def valid_position(input):
	#The regular expression of a list of positions
	if re.match(r"^\[(\d+\,)*\d+\]$", input) == None:
		raise PositionErr("Invalid shares")
	return True

#Initialize the list of position
def init_position(position):
	#Parse the list of positions
	pos = position.split(",")

	pos[0] = pos[0].replace("[", "")
	pos[-1] = pos[-1].replace("]", "")

	#Return the structured data
	return [int(i) for i in pos]

#Compute the mean and std of each position
def stats_results(position, results):
	#Create a empty dataframe
	df = pd.DataFrame(index=position, columns=["mean", "std"])
	#Calculate the mean and std
	df["mean"] = [np.mean(results[p]) for p in position]
	df["std"] = [np.std(results[p]) for p in position]

	return df

#Terminate the program
def terminate():
	print "\nProgram terminated"
	sys.exit(0)


